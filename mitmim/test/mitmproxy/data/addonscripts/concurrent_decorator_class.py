import time
from mock_server.mitmim.mitmproxy.script import concurrent


class ConcurrentClass:

    @concurrent
    def request(self, flow):
        time.sleep(0.1)


addons = [ConcurrentClass()]
