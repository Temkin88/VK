"""Add a custom command to mitmproxy's command prompt."""
from mock_server.mitmim.mitmproxy import command
from mock_server.mitmim.mitmproxy import ctx


class MyAddon:
    def __init__(self):
        self.num = 0

    @command.command("myaddon.inc")
    def inc(self) -> None:
        self.num += 1
        ctx.log.info(f"num = {self.num}")


addons = [
    MyAddon()
]
