import logging
import asyncio
import struct
from contextlib import suppress
from random import randint

from typing import Optional

from pyvkteamsipros.alias import Alias
from pyvkteamsipros.constant import G_reconnect_period, G_settings, G_self_alias, ConnectionsList, G_incoming_handlers
from pyvkteamsipros.icrc32 import calculate_icrc32
from pyvkteamsipros.io import IStream
from pyvkteamsipros.ipros.enums import ConnState, ConnFlags
from pyvkteamsipros.maps_ctlr import MapsController
from pyvkteamsipros.packet import Packet, Request, Reply
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


def select_srv_by_key(svcname: str, key: Optional[bytes | str]):
    if svcname not in MapsController.maps:
        raise Exception("{} uninit".format(svcname))
    if isinstance(key, str):
        key = key.encode(encoding="utf-8")
    return MapsController.maps[svcname].srv_by_bkr(calculate_icrc32(key) if key else randint(0, 0xFFFFFFFF))


async def read_packet(r):
    hdr = await r.read(12)
    if hdr == bytes():
        return None
    msg, length, sync = IStream(hdr).getIproHdr()
    body = await r.readexactly(length)
    return Packet(msg, sync, body)


def get_conn_by_host_port(host, port):
    for cn in ConnectionsList.connections:
        if cn.host == host and cn.port == port and cn.state != ConnState.FINISH:
            return cn


def get_conn_by_alias(alias):
    for cn in ConnectionsList.connections:
        if cn.alias == alias and cn.state != ConnState.FINISH:
            return cn


def reset_self_alias(s):
    G_self_alias = Alias(s)
    log.info("self: {}".format(G_self_alias))


def self_alias():
    assert G_self_alias
    return G_self_alias


async def connection(host, port, svcname=None):
    cn = get_conn_by_host_port(host, port)
    if cn is None:
        cn = Conn(host, port)
        ConnectionsList.connections += [cn]

        if svcname in G_settings and G_settings[svcname].on_init_async:
            await G_settings[svcname].on_init_async(cn)

    return cn


async def send(svcname, req: Request, timeout: int) -> Reply:
    assert select_srv_by_key
    srv = select_srv_by_key(svcname, req.key)
    cn = await connection(srv.host, srv.port, svcname)
    return await cn.send(req, timeout)


async def sendto(host, port, req: Request, timeout: int) -> Reply:
    cn = await connection(host, port)
    return await cn.send(req, timeout)


async def send_noreply(svcname, req: Request):
    assert select_srv_by_key
    req.noreply = True
    srv = select_srv_by_key(svcname, req.key)
    cn = await connection(srv.host, srv.port, svcname)
    return await cn.send(req, 0)


async def shutdown():
    await asyncio.gather(*[conn.shutdown() for conn in ConnectionsList.connections])


async def reconnect(host, port, svcname):
    await asyncio.sleep(G_reconnect_period)

    conn = get_conn_by_host_port(host, port)
    if conn in ConnectionsList.connections:
        ConnectionsList.connections.remove(get_conn_by_host_port(host, port))

    await connection(host, port, svcname)


def reconnect_cn(cn: "Conn"):
    if cn.alias and cn.alias.svc:
        asyncio.get_event_loop().create_task(reconnect(cn.host, cn.port, cn.alias.svc))
