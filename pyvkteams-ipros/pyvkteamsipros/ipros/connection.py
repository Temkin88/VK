import struct
import asyncio
import logging
from contextlib import suppress
from typing import Optional

from pyvkteamsipros.alias import Alias
from pyvkteamsipros.constant import G_incoming_handlers, G_settings, G_self_alias
from pyvkteamsipros.io import IStream
from pyvkteamsipros.ipros.utils import read_packet, reconnect
from pyvkteamsipros.packet import Packet, Reply
from pyvkteamsipros.ipros.enums import ConnFlags, ConnState
from pyvkteamsipros.packet.enums import ServiceMessages

log = logging.getLogger(__name__)


class Conn:
    max_queue_size = 10
    default_flags = ConnFlags.KEY | ConnFlags.STATUS | ConnFlags.REPLY2 | ConnFlags.RECONNECT | ConnFlags.CTLRCNG

    def __init__(self, host, port, alias=None):
        self.pending = {}
        self.host = host
        self.port = port
        if isinstance(alias, str):
            alias = Alias(alias)
        self.alias = alias
        self.reader = None
        self.reader_coro = None
        self.writer = None
        self.state = ConnState.NONE

        self.queue = asyncio.Queue(Conn.max_queue_size)
        self.writer_coro = asyncio.get_event_loop().create_task(Conn._do_write(self, self.queue))

    async def send(self, req, timeout) -> Optional[Reply]:
        if self.queue.full():
            return Reply(500, "{} queue overflow".format(self), None)

        if req.noreply:
            return await self.queue.put(req)

        self.pending[req.sync] = asyncio.get_event_loop().create_future()
        try:
            await self.queue.put(req)
            resp = await asyncio.wait_for(self.pending[req.sync], timeout)
        except asyncio.TimeoutError:
            log.error("request timeout {}".format(req))
            resp = Reply(500, "timeout", None)
            self._request_done(req.sync, resp)
        return resp

    async def shutdown(self):
        if self.state != ConnState.FINISH:
            if self.alias and self.alias.svc in G_settings and G_settings[self.alias.svc].on_shutdown:
                G_settings[self.alias.svc].on_shutdown(self)
            self.state = ConnState.FINISH
        if self.writer:
            self.writer.close()
        self.writer_coro.cancel()
        if self.reader_coro:
            self.reader_coro.cancel()
        with suppress(asyncio.CancelledError):
            await self.writer_coro
            if self.reader_coro:
                await self.reader_coro

    async def reply(self, req: Packet, status, reason, data: Optional[bytes] = None):
        if data is None:
            data = b""
        return await self.send(req.compose_reply(status, reason, data), 0)

    async def _do_write(self, queue):
        try:
            self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
            self.reader_coro = asyncio.get_event_loop().create_task(Conn._do_read(self))
            self.writer.write(Packet.hello(G_self_alias, Conn.default_flags).dump())

            while True:
                req = await queue.get()
                log.debug("<= {} {}".format(self, req))
                self.writer.write(req.dump())
        except asyncio.CancelledError:
            log.warning("{} writer shutdown".format(self))
            raise
        except OSError as x:
            log.error("{} writer OS error: {}".format(self, x))
        except Exception as x:
            log.exception("{} writer failure: {}".format(self, x))
        finally:
            syncs = list(self.pending.keys())
            for sync in syncs:
                self._request_done(sync, Reply(500, "cancelled", None))
            await self.shutdown()

    async def _do_read(self):
        try:
            while True:
                p = await read_packet(self.reader)
                if p is None:
                    log.warning("Connection closed by peer {}".format(self))
                    return await self.shutdown()
                await asyncio.get_event_loop().create_task(self._process(p))
        except asyncio.CancelledError:
            log.warning("{} reader shutdown".format(self))
            raise
        except OSError as x:
            log.error("{} reader error: {}".format(self, x))
        except struct.error:
            log.exception("protocol error with {}".format(self))
            await self.shutdown()
        except Exception as x:
            log.exception("{} reader failure: {}".format(self, x))

    async def _process(self, p):
        log.debug("=> {} {}".format(self, p))
        if p.msg == ServiceMessages.REPLY:
            self._request_done(p.sync, Reply.from_packet(p))
        elif p.msg == ServiceMessages.HELLO:
            self.alias = Alias.load(IStream(p.body).getLps())
            log.info("HELLO from {}".format(self.alias))
            self.state = ConnState.ESTABLISHED
        elif p.msg == ServiceMessages.RECONNECT:
            istr = IStream(p.body)
            self.alias = Alias.load(istr.getLps())
            host = ".".join(map(str, istr.getIPv4()))
            port = istr.getU16n()
            log.info("RECONNECT to {}:{}".format(host, port))
            await asyncio.get_event_loop().create_task(reconnect(host, port, self.alias.svc))
            self.state = ConnState.FINISH
            await self.shutdown()
        elif self.alias and self.alias.svc in G_incoming_handlers:
            await G_incoming_handlers[self.alias.svc](self, p)

    def __repr__(self):
        if self.alias:
            return repr(self.alias)
        return "{}:{}".format(self.host, self.port)

    def _request_done(self, sync, rep: Reply):
        if sync in self.pending:
            fut = self.pending[sync]
            if not fut.done():
                fut.set_result(rep)
            del self.pending[sync]
        else:
            log.error("unexpected reply {} from {}".format(sync, self))
