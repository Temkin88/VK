"""Handle file paths as command arguments."""
import typing

from mock_server.mitmim.mitmproxy import command
from mock_server.mitmim.mitmproxy import ctx
from mock_server.mitmim.mitmproxy import flow
from mock_server.mitmim.mitmproxy import types


class MyAddon:
    @command.command("myaddon.histogram")
    def histogram(
        self,
        flows: typing.Sequence[flow.Flow],
        path: types.Path,
    ) -> None:
        totals = {}
        for f in flows:
            totals[f.request.host] = totals.setdefault(f.request.host, 0) + 1

        with open(path, "w+") as fp:
            for cnt, dom in sorted([(v, k) for (k, v) in totals.items()]):
                fp.write("%s: %s\n" % (cnt, dom))

        ctx.log.alert("done")


addons = [
    MyAddon()
]
