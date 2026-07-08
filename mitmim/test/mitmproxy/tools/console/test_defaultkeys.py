import pytest

import mock_server.mitmim.mitmproxy.types
from mock_server.mitmim.mitmproxy import command
from mock_server.mitmim.mitmproxy import ctx
from mock_server.mitmim.mitmproxy.test.tflow import tflow
from mock_server.mitmim.mitmproxy.tools.console import defaultkeys
from mock_server.mitmim.mitmproxy.tools.console import keymap
from mock_server.mitmim.mitmproxy.tools.console import master


@pytest.mark.asyncio
async def test_commands_exist():
    command_manager = command.CommandManager(ctx)

    km = keymap.Keymap(None)
    defaultkeys.map(km)
    assert km.bindings
    m = master.ConsoleMaster(None)
    await m.load_flow(tflow())

    for binding in km.bindings:
        parsed, _ = command_manager.parse_partial(binding.command.strip())

        cmd = parsed[0].value
        args = [
            a.value for a in parsed[1:]
            if a.type != mitmproxy.types.Space
        ]

        assert cmd in m.commands.commands

        cmd_obj = m.commands.commands[cmd]
        try:
            cmd_obj.prepare_args(args)
        except Exception as e:
            raise ValueError("Invalid command: {}".format(binding.command)) from e
