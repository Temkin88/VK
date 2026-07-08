import time
import sys
from mock_server.mitmim.mitmproxy.script import concurrent


@concurrent
def request(flow):
    time.sleep(0.1)
