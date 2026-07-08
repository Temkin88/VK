import logging
from typing import Callable, Optional

from pyvkteamsipros.alias import Alias
from pyvkteamsipros.ctlr.enums import MsgId
from pyvkteamsipros.io import IStream, OStream
from pyvkteamsipros.map.map import Map
from pyvkteamsipros.ipros import utils as ipros
from pyvkteamsipros.maps_ctlr import MapsController
from pyvkteamsipros.packet import Request
from pyvkteamsipros.role_ctlr import RoleController

log = logging.getLogger(__name__)


role_changed_cb: Optional[Callable] = None


class IncomingHandlers:
    @staticmethod
    async def MAP(p):

        istr = IStream(p.body)
        mapname = str(istr.getLps().getAll(), encoding="utf8")
        m = Map(istr)
        m.dump_to(log.debug, "ctlr: got new map for {}".format(mapname))

        MapsController.maps.pop(mapname, None)
        MapsController.maps[mapname] = m

        if mapname in MapsController.received_maps:
            MapsController.received_maps[mapname].set()

        me = m.srv_by_alias(ipros.self_alias())
        if me and me.role != RoleController.current_role:
            if role_changed_cb is not None:
                role_changed_cb(RoleController.current_role, me.role)
            RoleController.current_role = me.role

    @staticmethod
    async def PING():
        return await ipros.send("ctlr", Request("", MsgId.PING, b""), 5)

    @classmethod
    async def FLIP(cls, cn, p):
        if len(p.body) == 0:
            log.error("abort flip")
            return

        dst = Alias.load(IStream(p.body).getLps())
        log.warning("start flip to {}".format(dst))
        await cn.reply(p, 200, "ok")
        return await cls.flop(dst)

    @staticmethod
    async def flop(dst: Alias):
        pkt = OStream()
        pkt.putLps(dst.dump())
        r = Request("", MsgId.FLOP, pkt.data)
        r.key_prepend = False
        return await ipros.send("ctlr", r, 3)
