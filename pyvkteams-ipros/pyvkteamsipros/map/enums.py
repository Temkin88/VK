class Tag:
    MAP_TYPE = 1
    MAP_NODE = 2
    MAP_SRV = 3
    MAP_BKRS = 4
    NODE_NAME = 1
    SRV_BIND = 1
    SRV_ROLE = 2
    SRV_NODE = 3


class Role:
    NONE = 0
    MAIN = 1
    SLAVE = 2
    MIRROR = 3
    FALLBACK = 4
    AB = 5
    DUP = 6
    BOND = 7
    FORK = 8
    REPL = 9

    @classmethod
    def by_id(cls, _id):
        for n in cls.__dict__:
            if getattr(cls, n) == _id:
                return n.lower()
        raise Exception("unknown srv role: {}".format(_id))
