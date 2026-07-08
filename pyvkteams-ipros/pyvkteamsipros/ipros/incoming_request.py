from pyvkteamsipros.alias import Alias
from pyvkteamsipros.packet import Packet


class IncomingRequest:
    def __init__(self, req: Packet, sender: Alias, writer):
        self.req = req
        self.sender = sender
        self.writer = writer

    def __repr__(self):
        return "=> {} {}".format(self.sender, self.req)

    def reply(self, status, reason, data=None):
        self.writer.write(
            self.req.compose_reply(status, reason, data).dump()
        )
