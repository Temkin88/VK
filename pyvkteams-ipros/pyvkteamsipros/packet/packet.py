from typing import Optional

from pyvkteamsipros.io import OStream, IStream
from pyvkteamsipros.alias import Alias
from pyvkteamsipros.packet.enums import ServiceMessages
from pyvkteamsipros.packet.utils import sg


class Packet:
    def __init__(self, msg, sync, body):
        self.msg = msg
        self.sync = sync
        self.body = body

    def dump(self):
        out = OStream()
        out.putU32(self.msg)
        out.putU32(len(self.body))
        out.putU32(self.sync)
        out.putBlob(self.body)
        return out.data

    @classmethod
    def hello(cls, alias: Alias, conn_flags: int):
        bd = OStream()
        bd.putLps(alias.dump())
        bd.putU32(conn_flags)
        return cls(ServiceMessages.HELLO, next(sg), bd.data)

    def compose_reply(self, status, reason, data) -> "Request":
        body = OStream()
        if data is None:
            data = bytes()
        body.putU32(status).putLps(reason).putBlob(data)
        r = Request(None, ServiceMessages.REPLY, body.data, sync=self.sync)
        r.noreply = True
        r.key_prepend = False
        return r

    def __repr__(self):
        return "0x{:04X}/{}".format(self.msg, self.sync)


class Request:
    def __init__(self, key: Optional[str], msg: int, data: bytes, sync: Optional[int] = None):
        self.key = key
        self.msg = msg
        self.data = data
        if sync is None:
            sync = next(sg)
        self.sync = sync
        self.key_prepend = True
        self.noreply = False

    def dump(self):
        keyed_body = OStream()
        if self.key_prepend:
            keyed_body.putLps(self.key)
        keyed_body.putBlob(self.data)

        return Packet(self.msg, self.sync, keyed_body.data).dump()

    def __repr__(self):
        return "0x{:04X}/{} len {}".format(self.msg, self.sync, len(self.data))


class Reply:
    def __init__(self, status, reason, body):
        self.status = status
        self.reason = reason
        self.body = body

    @classmethod
    def from_packet(cls, p: Packet):
        istr = IStream(p.body)
        return cls(istr.getU32(), istr.getLps().data, istr.getAll())

    def __repr__(self):
        return "{}[{}]".format(self.status, self.reason)
