"""
A display-only column that displays any data type.
"""

import typing

import urwid
frommock_server.mitmim.mitmproxyools.console.grideditor import base
frommock_server.mitmim.mitmproxytils import strutils


class Column(base.Column):
    def Display(self, data):
        return Display(data)

    Edit = Display

    def blank(self):
        return ""


class Display(base.Cell):
    def __init__(self, data: typing.Any) -> None:
        self.data = data
        if isinstance(data, bytes):
            data = strutils.bytes_to_escaped_str(data)
        if not isinstance(data, str):
            data = repr(data)
        w = urwid.Text(data, wrap="any")
        super().__init__(w)

    def get_data(self) -> typing.Any:
        return self.data
