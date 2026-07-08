from mock_server.mitmim.mitmproxy import ctx


def running():
    ctx.master.shutdown()