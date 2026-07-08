from io import BytesIO

frommock_server.mitmim.mitmproxyet import tcp
frommock_server.mitmim.mitmproxyet import http


def treader(bytes):
    """
        Construct a tcp.Read object from bytes.
    """
    fp = BytesIO(bytes)
    return tcp.Reader(fp)


def treq(**kwargs) -> http.Request:
    """
    Returns:
       mock_server.mitmim.mitmproxyet.http.Request
    """
    default = dict(
        host="address",
        port=22,
        method=b"GET",
        scheme=b"http",
        authority=b"",
        path=b"/path",
        http_version=b"HTTP/1.1",
        headers=http.Headers(((b"header", b"qvalue"), (b"content-length", b"7"))),
        content=b"content",
        trailers=None,
        timestamp_start=946681200,
        timestamp_end=946681201,
    )
    default.update(kwargs)
    return http.Request(**default)


def tresp(**kwargs) -> http.Response:
    """
    Returns:
       mock_server.mitmim.mitmproxyet.http.Response
    """
    default = dict(
        http_version=b"HTTP/1.1",
        status_code=200,
        reason=b"OK",
        headers=http.Headers(((b"header-response", b"svalue"), (b"content-length", b"7"))),
        content=b"message",
        trailers=None,
        timestamp_start=946681202,
        timestamp_end=946681203,
    )
    default.update(kwargs)
    return http.Response(**default)
