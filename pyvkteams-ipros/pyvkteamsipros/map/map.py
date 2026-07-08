import logging
import bisect
from typing import TYPE_CHECKING, Optional

from pyvkteamsipros.map.objects import Record, Srv, Node
from pyvkteamsipros.map.enums import Tag

if TYPE_CHECKING:
    from pyvkteamsipros.io import IStream


log = logging.getLogger(__name__)


class Map:
    def __init__(self, istr: "IStream" = None):
        self.type = ""
        self.node = {}
        self.srv = {}
        self.node_masters = {}
        self.bkrs = []

        if istr:
            istr.tlvForeach(
                {
                    Tag.MAP_TYPE: lambda v: setattr(self, "type", v.getU32()),  # Fuck you Python
                    Tag.MAP_NODE: lambda v: self._load_node(v),
                    Tag.MAP_SRV: lambda v: self._load_srv(v),
                    Tag.MAP_BKRS: lambda v: self._load_bkrs(v),
                }
            )
        res = []
        if not len(self.bkrs):
            for _, v in self.node_masters.items():
                res.append(Record(0, v.host, v.port, v.alias))
                break
        else:
            for bk in self.bkrs:
                srv = self.node_masters.get(bk[0], Srv.none())
                res.append(Record(bk[1], srv.host, srv.port, srv.alias))
        self.bkrs = res

    def append(self, r: Record):
        assert not self.bkrs and r.bkr_start == 0 or self.bkrs[-1].bkr_start < r.bkr_start
        self.bkrs.append(r)

    def srv_by_bkr(self, key) -> Record:
        keys = [r.bkr_start for r in self.bkrs]
        i = bisect.bisect_right(keys, key)
        if i == 0:
            raise Exception("search in empty map")
        return self.bkrs[i - 1]

    def srv_by_alias(self, alias) -> Optional[Srv]:
        if str(alias) not in self.srv:
            return None
        return self.srv[str(alias)]

    def _load_node(self, v):
        i = v.getU32()
        self.node[i] = Node(v)

    def _load_srv(self, v):
        srv = Srv(v)
        self.srv[str(srv.alias)] = srv
        log.debug("got srv: {}".format(srv))
        if srv.role == "main":
            self.node_masters[srv.node_id] = srv

    def _load_bkrs(self, v):
        v.getU64()
        bk = 0
        while v.inAvail():
            node_id = v.getVarInt()
            if node_id != 0:
                self.bkrs.append((node_id, bk))
            bk += 1 + v.getMishasFuckingInt()
        assert bk == 2**32
        self.bkrs.sort(key=lambda record: record[1])

    def dump_to(self, writer, prefix: str = ""):
        s = prefix
        for bkr in self.bkrs:
            s += f"\n{bkr}"
        writer(s)
