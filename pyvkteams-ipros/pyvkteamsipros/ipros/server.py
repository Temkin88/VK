import asyncio
import logging

from pyvkteamsipros.alias import Alias
from pyvkteamsipros.constant import G_self_alias
from pyvkteamsipros.io import IStream
from pyvkteamsipros.ipros.connection import Conn
from pyvkteamsipros.ipros.incoming_request import IncomingRequest
from pyvkteamsipros.ipros.utils import read_packet
from pyvkteamsipros.packet import Packet

log = logging.getLogger(__name__)


class Server:
    def __init__(self, request_cb):
        self.request_cb = request_cb

    async def __call__(self, reader, writer):
        peer = "someone"
        try:
            writer.write(Packet.hello(G_self_alias, Conn.default_flags).dump())
            hello = await read_packet(reader)
            peer = Alias.load(IStream(hello.body).getLps())
            log.info("{} connected".format(peer))
            while True:
                p = await read_packet(reader)
                if p is None:
                    break
                await asyncio.get_event_loop().create_task(self.request_cb(IncomingRequest(p, peer, writer)))
        finally:
            log.info("{} disconnected".format(peer))
