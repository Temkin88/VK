class ConnFlags:
    KEY = 0x0001
    STATUS = 0x0002
    REPLY2 = 0x0004
    RECONNECT = 0x0080
    CTLRCNG = 0x0800


class ConnState:
    NONE = 1
    ESTABLISHED = 2
    FINISH = 3
