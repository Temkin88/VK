import asyncio

from pyvkteamsipros import alias, ctlr, icrc32, io, ipros, map, packet, constant


__version__ = "0.0.1"
__all__ = ["alias", "ctlr", "icrc32", "io", "ipros", "map", "packet"]

from pyvkteamsipros.constant import G_incoming_handlers
from pyvkteamsipros.maps_ctlr import MapsController

from pyvkteamsipros.packet import Request

G_incoming_handlers["ctlr"] = ctlr.utils.incoming_handler


async def send(svcname: str, key: bytes, msg: int, data: bytes, timeout=5):
    if svcname not in MapsController.maps:
        await ctlr.utils.subscribe(svcname)

    return await ipros.utils.send(svcname, Request(key, msg, data), timeout)


async def listen(ip, port, request_cb):
    async def init_ctlr(cn):
        ctlr.init(cn.host, cn.port)
        await ctlr.utils.join(ip, port)

    server = ipros.Server(request_cb)
    await ctlr.utils.join(ip, port)
    constant.G_settings["ctlr"].on_init_async = init_ctlr
    constant.G_settings["ctlr"].on_shutdown = ipros.utils.reconnect_cn
    return await asyncio.start_server(server, ip, port)
