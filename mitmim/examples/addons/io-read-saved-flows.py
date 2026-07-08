#!/usr/bin/env python
"""
Read a mitmproxy dump file.
"""
from mock_server.mitmim.mitmproxy import io
from mock_server.mitmim.mitmproxy.exceptions import FlowReadException
import pprint
import sys

with open(sys.argv[1], "rb") as logfile:
    freader = io.FlowReader(logfile)
    pp = pprint.PrettyPrinter(indent=4)
    try:
        for f in freader.stream():
            print(f)
            print(f.request.host)
            pp.pprint(f.get_state())
            print("")
    except FlowReadException as e:
        print("Flow file corrupted: {}".format(e))
