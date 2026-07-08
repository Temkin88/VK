import asyncio
import logging

from pyvkteamsipros.map import Map


log = logging.getLogger(__name__)


class MapsController:

    maps: dict[str, Map] = {}
    received_maps: dict[str, asyncio.Event] = {}

    def __contains__(self, item: str) -> bool:
        return item in self.received_maps

    def __delitem__(self, item: str):
        del self.received_maps[item]
