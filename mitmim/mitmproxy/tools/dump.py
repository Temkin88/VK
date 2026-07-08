from mock_server.mitmim.mitmproxy import addons
from mock_server.mitmim.mitmproxy import options
from mock_server.mitmim.mitmproxy import master
from mock_server.mitmim.mitmproxy.addons import dumper, termlog, termstatus, keepserving, readfile
import asyncio

class ErrorCheck:
    def __init__(self):
        self.has_errored = False

    def log(self, e):
        if e.level == "error":
            self.has_errored = True


class DumpMaster(master.Master):

    def __init__(
        self,
        options: options.Options,
        loop,
        with_termlog=True,
        with_dumper=True,
    ) -> None:
        super().__init__(options, loop)
        self.errorcheck = ErrorCheck()
        if with_termlog:
            self.addons.add(termlog.TermLog(), termstatus.TermStatus())
        self.addons.add(*addons.default_addons())
        if with_dumper:
            self.addons.add(dumper.Dumper())
        self.addons.add(
            keepserving.KeepServing(),
            readfile.ReadFileStdin(),
            self.errorcheck
        )
