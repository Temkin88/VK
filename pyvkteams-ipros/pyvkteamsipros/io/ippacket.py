import struct

from pyvkteamsipros.io.streams import IStream


class IPacket(IStream):
    def __init__(self, msg, seq, proto, data):
        super(IPacket, self).__init__(data)
        self.proto = proto
        self.msg = msg
        self.seq = seq

    @staticmethod
    def create(hdr, data):
        _, proto, seq, msg = struct.unpack_from("<L L 2L", hdr)
        return IPacket(msg, seq, proto, data)
