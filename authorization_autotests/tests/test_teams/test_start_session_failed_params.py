import pytest

from api.client.adapter import ClientAdapterTeamsOTP
from api.client.client import UserClientTeamsOTP
from common.config import HOSTS_TEAMS, PASS_TEAMS_OTP, LOGIN_TEAMS_OTP
from conftest import get_config
from markers import TEAMS


@TEAMS
@pytest.mark.parametrize("subscriptions", ["message", 123, {}, [], None, ''])
def test_start_session_failed_params(get_config, SANDBOX, subscriptions):
    host = SANDBOX.replace("https://", "vkt-", 1)
    api_url = get_config(f"u.{host}")['api-urls']['main-api']
    api_ver = get_config(f"u.{host}")['api-version']
    user_ws = UserClientTeamsOTP(
        api_url=api_url,
        api_ver=api_ver,
        uin=LOGIN_TEAMS_OTP,
        password=PASS_TEAMS_OTP,
        login_adapter=ClientAdapterTeamsOTP(base_url=api_url),
    )

    user = user_ws.login(subscriptions=[{"type": subscriptions}])
    assert user[3] == 200
    assert "autotest001@autotest.clients" in user[0]
    assert "https://u.vkt-auth-test.vkteams.vkwm.ru" in user[1]
