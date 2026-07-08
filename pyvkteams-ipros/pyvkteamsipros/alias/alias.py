import re
import logging
from pyvkteamsipros.io import IStream, OStream


alias_re = re.compile(r"(.*)\.(.*)\.(.*)")
log = logging.getLogger(__name__)


class Alias:
    def __init__(self, s: str):
        m = alias_re.match(s)
        if m is None:
            raise Exception("invalid alias: {}".format(s))
        self.svc, self.host, self.conf = m.groups()

    def __repr__(self):
        return "{}.{}.{}".format(self.svc, self.host, self.conf)

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        return str(self) == str(other)

    @classmethod
    def load(cls, istr: IStream):
        return cls("{}.{}.{}".format(istr.getStr(), istr.getStr(), istr.getStr()))

    def dump(self) -> bytes:
        out = OStream()
        out.putLps(self.svc)
        out.putLps(self.host)
        out.putLps(self.conf)
        return out.data
