import mock_server.mitmim
from mock_server.mitmim.mitmproxy import ctx


class CheckCA:
    def __init__(self):
        self.failed = False

    def configure(self, updated):
        has_ca = (
           mock_server.mitmim.mitmproxy.master.server and
           mock_server.mitmim.mitmproxy.master.server.config and
           mock_server.mitmim.mitmproxy.master.server.config.certstore and
           mock_server.mitmim.mitmproxy.master.server.config.certstore.default_ca
        )
        if has_ca:
            self.failed =mock_server.mitmim.mitmproxy.master.server.config.certstore.default_ca.has_expired()
            if self.failed:
                ctx.log.warn(
                    "The mitmproxy certificate authority has expired!\n"
                    "Please delete all CA-related files in your ~/.mitmproxy folder.\n"
                    "The CA will be regenerated automatically after restarting mitmproxy.\n"
                    "Then make sure all your clients have the new CA installed.",
                )
