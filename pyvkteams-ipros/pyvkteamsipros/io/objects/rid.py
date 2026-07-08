import random


class Rid:
    RID_ID_BITS = 56

    def __init__(self, t, i):
        self.type = t
        self.id = i

    def __int__(self):
        return self.id | (self.type << self.RID_ID_BITS)

    def __eq__(self, b):
        return self.id == b.id and self.type == b.type

    def __ne__(self, b):
        return not (self == b)

    def __hash__(self):
        return int(self)

    def __str__(self):
        return str(self.type) + ":" + str(self.id)

    def __repr__(self):
        return str(self)

    @classmethod
    def fromU64(cls, u64):
        i = u64 & ((1 << cls.RID_ID_BITS) - 1)
        t = u64 >> cls.RID_ID_BITS
        return cls(t, i)

    @classmethod
    def getRandomId(cls):
        return int(random.getrandbits(cls.RID_ID_BITS))

    @classmethod
    def nextId(cls, _id):
        return (_id + 1) % (1 << cls.RID_ID_BITS)
