import socket
import struct

from pyvkteamsipros.io.objects import MsgId, Rid


class IStream(object):
    def __init__(self, data):
        self.data = data
        self.dlen = len(data)
        self.offset = 0

    def __str__(self):
        return str(self.data)

    def __unpack(self, fmt):
        r = struct.unpack_from(fmt, self.data, self.offset)
        self.offset += struct.calcsize(fmt)
        return r

    def getBlob(self, length):
        return self.__unpack("<{0}s".format(length))[0]

    def getAll(self):
        return self.getBlob(self.inAvail())

    def getMsgId(self):
        _id = self.getU64()
        return MsgId(_id)

    def getRid(self):
        return Rid.fromU64(self.getU64())

    def getIproHdr(self):
        return self.getU32(), self.getU32(), self.getU32()

    def getU8(self):
        return self.__unpack("B")[0]

    def getU16(self):
        return self.__unpack("<H")[0]

    def getU16n(self):
        return self.__unpack(">H")[0]

    def getU32(self):
        return self.__unpack("<L")[0]

    def getU64(self):
        return self.__unpack("<Q")[0]

    def getLps(self):
        length = self.getU32()
        return IStream(self.__unpack("<{0}s".format(length))[0])

    def getStr(self):
        return str(self.getLps().data, encoding="utf8")

    def getTlv(self):
        return self.getU32(), self.getLps()

    def Tlvs(self):
        while self.inAvail():
            tag = self.getU32()
            val = self.getLps()
            yield tag, val

    def tlvForeach(self, cbmap):
        while self.inAvail():
            t, v = self.getTlv()
            if t in cbmap:
                cbmap[t](v)

    def Lpss(self):
        while self.inAvail():
            lps = self.getLps()
            yield lps

    @staticmethod
    def decode_varint(data):
        res = 0
        i = 0
        while True:
            res <<= 7
            res |= data[i] & 0x7F
            if not data[i] & 0x80:
                break
            i = i + 1
        return res, i + 1

    def getVarInt(self):
        v, off = self.decode_varint(self.data[self.offset :])
        self.offset += off
        return v

    def getVarIntLps(self):
        length = self.getVarInt()
        return IStream(self.__unpack("<{0}s".format(length))[0])

    def getVarIntLpsNum(self):
        length = self.getVarInt()
        r = IStream(self.__unpack("<{0}s".format(length))[0])

        if length == 2:
            return r.getU16()

        if length == 4:
            return r.getU32()

        if length == 8:
            return r.getU64()

    def getIPv4(self):
        return [self.getU8(), self.getU8(), self.getU8(), self.getU8()]

    def getMishasFuckingInt(self):
        isize = self.getU8()
        if isize == 0:
            return 0
        elif isize == 1:
            return self.getU8()
        elif isize == 2:
            return self.getU16()
        elif isize == 3:
            return self.getU16() + self.getU8() * 65536
        elif isize == 4:
            return self.getU32()
        raise Exception("invalid MishasFuckingInt")

    def getTlvset(self):
        tlvset = {}

        while self.inAvail():
            t, v = self.getTlv()
            tlvset[t] = v

        return tlvset

    def inAvail(self):
        return self.dlen - self.offset


class OStream:
    def __init__(self, data: bytes = b""):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __pack(self, fmt, *args):
        self.data += struct.pack(fmt, *args)
        return self

    def putU8(self, num):
        return self.__pack("B", num)

    def putMsgId(self, mid):
        return self.putU64(int(mid))

    def putU16(self, num):
        return self.__pack("<H", num)

    def putU16n(self, num):
        return self.__pack(">H", num)

    def putU32(self, num):
        return self.__pack("<L", num)

    def putI32(self, num):
        return self.__pack("<l", num)

    def putRid(self, _type, _id):
        return self.putU64(int(Rid(_type, _id)))

    def putChatId(self, _id):
        return self.putRid(2, _id)

    def putMchatHdr(self, _type, _id):
        return self.putReqId().putRid(_type, _id).putOrigin()

    def putU64(self, num):
        return self.__pack("<Q", num)

    def putLps(self, data):
        if isinstance(data, str):
            data = bytes(data, encoding="utf8")
        self.putU32(len(data))
        return self.putBlob(data)

    def putBlob(self, data):
        if isinstance(data, str):
            data = bytes(data, encoding="utf8")
        return self.__pack("<{0}s".format(len(data)), data)

    def putTlv(self, tag, data):
        self.putU32(tag)
        return self.putLps(data)

    def putTlvU32(self, tag, n):
        self.putU32(tag)
        return self.putLps(OStream().putU32(n).data)

    def putTlvU8(self, tag, n):
        self.putU32(tag)
        return self.putLps(OStream().putU8(n).data)

    def putIPkt(self, msg, data):
        if isinstance(data, str):
            data = bytes(data, encoding="utf8")
        self.putU32(msg)
        self.putU32(len(data))
        self.putU32(0)
        return self.putBlob(data)

    def putISPkt(self, msg, key, data):
        paylo = OStream().putLps(key).putBlob(data)

        self.putU16(msg)
        self.putU16(1)
        self.putU32(len(paylo.data))
        self.putU32(0)
        return self.putBlob(paylo.data)

    def putIPv4(self, addr):
        if isinstance(addr, list):
            assert len(addr) == 4
            addr = ".".join([str(o) for o in addr])

        self.putBlob(socket.inet_aton(addr))

    def encloseLps(self):
        return OLps(self)

    def encloseCLps(self):
        return OCLps(self)

    def putReqId(self):
        return self

    def putOrigin(self):
        return self


class OLps(OStream):
    def __init__(self, ostream):
        super(OLps, self).__init__()
        self.ostream = ostream

    def __enter__(self):
        return self

    def __exit__(self, exception, value, traceback):
        if exception:
            return False

        self.ostream.putLps(self.data)


class OCLps(OLps):
    def __init__(self, ostream):
        super(OCLps, self).__init__(ostream)
        self.lpsCount = 0

    def putLps(self, data):
        super(OCLps, self).putLps(data)
        self.lpsCount += 1

    def __exit__(self, exception, value, traceback):
        self.data = struct.pack("<L", self.lpsCount) + self.data
        super(OCLps, self).__exit__(exception, value, traceback)
