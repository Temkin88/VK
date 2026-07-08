from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from pyvkteamsipros.io.streams import IStream
    from pyvkteamsipros.io.streams import OStream


istream: Optional["IStream"] = None
ostream: Optional["OStream"] = None


class MsgId:
    def __init__(self, u64_or_time, ctr=None):
        global istream, ostream

        if istream is None or ostream is None:
            from pyvkteamsipros.io.streams import IStream
            from pyvkteamsipros.io.streams import OStream

            istream = IStream
            ostream = OStream

        self.t = 0
        self.c = 0
        if ctr is None:
            if u64_or_time == -1:
                u64_or_time = 2 ^ 64 - 1

            istr = istream(ostream().putU64(u64_or_time).data)

            self.c = istr.getU32()
            self.t = istr.getU32()
        else:
            self.c = ctr
            self.t = u64_or_time

    def __hash__(self):
        return int(self)

    def __int__(self):
        return istream(ostream().putU32(self.c).putU32(self.t).data).getU64()

    def __str__(self):
        return str(int(self))

    def __cmp__(self, b):
        if int(self) < int(b):
            return -1
        elif int(self) > int(b):
            return 1
        else:
            return 0

    def __repr__(self):
        return str(self)

    def __eq__(self, b):
        return self.__cmp__(b) == 0

    def __ne__(self, b):
        return self.__cmp__(b) != 0

    def __le__(self, b):
        return self.__cmp__(b) < 0 or self.__cmp__(b) == 0

    def __lt__(self, b):
        return self.__cmp__(b) < 0

    def __ge__(self, b):
        return self.__cmp__(b) > 0 or self.__cmp__(b) == 0

    def __gt__(self, b):
        return self.__cmp__(b) > 0
