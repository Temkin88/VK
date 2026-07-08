from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from pyvkteamsipros.io import IStream

from pyvkteamsipros.alias import Alias
from pyvkteamsipros.map.enums import Tag, Role


class Srv:
    @classmethod
    def none(cls):
        return cls()

    def __init__(self, istr: Optional["IStream"] = None):
        self.alias = Alias("none.a.none")
        self.ip = [0, 0, 0, 0]
        self.host = "0.0.0.0"
        self.port = 0
        self.role = "main"
        self.node_id = -1

        if istr:
            self.alias = Alias(istr.getStr())
            tset = istr.getTlvset()
            self._parse_bind(tset[Tag.SRV_BIND])
            self.role = Role.by_id(tset[Tag.SRV_ROLE].getU32())
            self.node_id = tset[Tag.SRV_NODE].getU32()

    def _parse_bind(self, istr: "IStream"):
        self.ip = istr.getIPv4()
        self.host = ".".join([str(i) for i in self.ip])
        self.port = istr.getU16n()

    def __repr__(self):
        return "{}/{} ({}) = {}:{}".format(self.node_id, self.alias, self.role, self.host, self.port)
