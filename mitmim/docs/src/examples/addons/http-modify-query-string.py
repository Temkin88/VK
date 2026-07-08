"""Modify HTTP query parameters."""
from mock_server.mitmim.mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    flow.request.query["mitmproxy"] = "rocks"
