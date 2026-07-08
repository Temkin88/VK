from pyvkteamsipros.alias import Alias


class Record:
    def __init__(self, bkr_start: int, host: str, port: int, alias: Alias):
        self.bkr_start = bkr_start
        self.host = host
        self.port = port
        self.hostport = "{}:{}".format(self.host, self.port)
        self.alias = alias

    def __repr__(self):
        return "{:08x}    {}".format(self.bkr_start, self.alias)
