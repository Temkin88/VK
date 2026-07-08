from mock_server.mitmim.mitmproxy.addons import anticache
from mock_server.mitmim.mitmproxy.addons import anticomp
from mock_server.mitmim.mitmproxy.addons import block
from mock_server.mitmim.mitmproxy.addons import browser
from mock_server.mitmim.mitmproxy.addons import check_ca
from mock_server.mitmim.mitmproxy.addons import clientplayback
from mock_server.mitmim.mitmproxy.addons import command_history
from mock_server.mitmim.mitmproxy.addons import core
from mock_server.mitmim.mitmproxy.addons import cut
from mock_server.mitmim.mitmproxy.addons import disable_h2c
from mock_server.mitmim.mitmproxy.addons import export
from mock_server.mitmim.mitmproxy.addons import onboarding
from mock_server.mitmim.mitmproxy.addons import proxyauth
from mock_server.mitmim.mitmproxy.addons import script
from mock_server.mitmim.mitmproxy.addons import serverplayback
from mock_server.mitmim.mitmproxy.addons import mapremote
from mock_server.mitmim.mitmproxy.addons import maplocal
from mock_server.mitmim.mitmproxy.addons import modifybody
from mock_server.mitmim.mitmproxy.addons import modifyheaders
from mock_server.mitmim.mitmproxy.addons import stickyauth
from mock_server.mitmim.mitmproxy.addons import stickycookie
from mock_server.mitmim.mitmproxy.addons import streambodies
from mock_server.mitmim.mitmproxy.addons import save
from mock_server.mitmim.mitmproxy.addons import upstream_auth


def default_addons():
    return [
        core.Core(),
        browser.Browser(),
        block.Block(),
        anticache.AntiCache(),
        anticomp.AntiComp(),
        check_ca.CheckCA(),
        clientplayback.ClientPlayback(),
        command_history.CommandHistory(),
        cut.Cut(),
        disable_h2c.DisableH2C(),
        export.Export(),
        onboarding.Onboarding(),
        proxyauth.ProxyAuth(),
        script.ScriptLoader(),
        serverplayback.ServerPlayback(),
        mapremote.MapRemote(),
        maplocal.MapLocal(),
        modifybody.ModifyBody(),
        modifyheaders.ModifyHeaders(),
        stickyauth.StickyAuth(),
        stickycookie.StickyCookie(),
        streambodies.StreamBodies(),
        save.Save(),
        upstream_auth.UpstreamAuth(),
    ]
