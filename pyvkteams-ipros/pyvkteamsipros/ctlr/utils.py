import logging
import asyncio

from pyvkteamsipros.alias import Alias
from pyvkteamsipros.ctlr.enums import MsgId, JoinTag, SrvFlag
from pyvkteamsipros.ctlr.incoming_handlers import IncomingHandlers
from pyvkteamsipros.maps_ctlr import MapsController
from pyvkteamsipros.io import OStream
from pyvkteamsipros.ipros import utils as ipros
from pyvkteamsipros.ipros.connection import Conn

from pyvkteamsipros.map.objects import Record
from pyvkteamsipros.packet import Request, Packet
from pyvkteamsipros.map.map import Map


log = logging.getLogger(__name__)


def _hp(h, p) -> str:
    return "{}:{}".format(h, p)


def init(host, port, self_alias=None):
    MapsController.maps = {}

    if self_alias:
        ipros.reset_self_alias(self_alias)
    m = Map()
    m.append(Record(0, host, port, Alias("ctlr.unknown.ctlr")))
    reset_map("ctlr", m)


def reset_map(svcname, new_map: "Map"):
    MapsController.maps.pop(svcname, None)
    MapsController.maps[svcname] = new_map


async def subscribe(svcname, timeout=5):
    log.info("subscribe to {}".format(svcname))

    maps_ctlr = MapsController()

    if svcname in maps_ctlr.received_maps:
        return await asyncio.wait_for(maps_ctlr.received_maps[svcname].wait(), timeout)

    maps_ctlr.received_maps[svcname] = asyncio.Event()
    try:
        resp = await ipros.send("ctlr", Request(svcname, MsgId.SBC, b""), 3)
        if resp.status != 200:
            raise Exception("Failed to subscribe to {} map: {}".format(svcname, resp))
        await asyncio.wait_for(maps_ctlr.received_maps[svcname].wait(), timeout)
    except asyncio.TimeoutError:
        log.error("timeout waiting for {} map".format(svcname))
        raise
    finally:
        del maps_ctlr.received_maps[svcname]


def join_request(ip, port):
    alias = ipros.self_alias()
    ostr = OStream()
    ostr.putIPv4(ip)
    ostr.putU16n(port)

    ostr.putTlv(JoinTag.HASH, "d4245e7c9152946211d0ae45892c7513b4537dc7")
    ostr.putTlvU32(JoinTag.FLAG, SrvFlag.CHECK | SrvFlag.PING | SrvFlag.KILL)
    ostr.putTlvU32(JoinTag.READY, 1)
    rq = Request(alias.svc, MsgId.JOIN, ostr.data)
    rq.key_prepend = False
    return rq


async def join(ip, port):
    return await ipros.send("ctlr", join_request(ip, port), 3)


async def incoming_handler(cn: Conn, p: Packet):
    for methname in dir(MsgId):
        if getattr(MsgId, methname) == p.msg:
            cb = getattr(IncomingHandlers, methname, None)
            if cb:
                await cb(cn, p)
