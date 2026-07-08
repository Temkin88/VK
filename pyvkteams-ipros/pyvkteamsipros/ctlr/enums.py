class MsgId:
    UNDEF = 0
    GETMAP = 1
    SBC = 2
    JOINOLD = 3
    MAP = 4
    PREP = 5
    MIGR = 6
    MOVEDOLD = 7
    FLIP = 8
    FLOP = 9
    JOIN = 10
    CHECK = 11
    PING = 12
    KILL = 13
    FLIPCHK = 14
    READY = 15
    MOVED = 16
    FORK = 17


class JoinTag:
    NONE = 0
    ASSIGNED = 1
    MASTER = 2
    SLAVE = 3
    MOVEDOLD = 4
    FLIP = 5
    FLOP = 6
    SRV = 7
    FLAG = 8
    HASH = 9
    READY = 10
    START = 11
    MOVED = 12
    SYNC = 13
    COMPOT = 14


class SrvFlag:
    CHECK = 0x00000001
    PING = 0x00000002
    KILL = 0x00000004
    DROP = 0x00000008
    FORK = 0x00000010
