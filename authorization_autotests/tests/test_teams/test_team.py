import pytest

from api.client.adapter import ClientAdapterTeamsOTP, ClientAdapterTeamsSSO, ClientAdapterTeamsSWA
from api.client.client import UserClientTeamsOTP, UserClientTeamsSSO, UserClientTeamsSWA
from common.config import HOSTS_TEAMS, PASS_TEAMS_OTP, LOGIN_TEAMS_OTP, LOGIN_TEAMS_SSO, PASS_TEAMS_SSO, LOGIN_TEAMS_SWA, \
    PASS_TEAMS_SWA
from conftest import get_config
from markers import TEAMS


# "autotest{001-10}@sso.auth-test.vkteams.vkwm.ru" - кейклок
# "autotest{001-10}@swa.auth-test.vkteams.vkwm.ru" - по паролю почты
# "autotest{001-10}@otp.auth-test.vkteams.vkwm.ru" - одноразовый пароль

@TEAMS
def test_teams_otp(get_config):
    api_url = get_config(f"u.{HOSTS_TEAMS}")['api-urls']['main-api']
    api_ver = get_config(f"u.{HOSTS_TEAMS}")['api-version']
    user_ws = UserClientTeamsOTP(
        api_url=api_url,
        api_ver=api_ver,
        uin=LOGIN_TEAMS_OTP,
        password=PASS_TEAMS_OTP,
        login_adapter=ClientAdapterTeamsOTP(base_url=api_url),
    )
    user = user_ws.login()
    assert "autotest001@autotest.clients" in user[0]
    assert "https://u.vkt-auth-test.vkteams.vkwm.ru" in user[1]

@TEAMS
def test_teams_sso(get_config):
    api_url = get_config(f"u.{HOSTS_TEAMS}")['api-urls']['main-api']
    api_ver = get_config(f"u.{HOSTS_TEAMS}")['api-version']
    user_ws = UserClientTeamsSSO(
        api_url=api_url,
        api_ver=api_ver,
        uin=LOGIN_TEAMS_SSO,
        email_password=PASS_TEAMS_SSO,
        login_adapter=ClientAdapterTeamsSSO(base_url=api_url),
    )
    user = user_ws.login()
    assert LOGIN_TEAMS_SSO in user[0]
    assert "https://u.vkt-auth-test.vkteams.vkwm.ru" in user[1]

@TEAMS
def test_teams_swa(get_config):
    api_url = get_config(f"u.{HOSTS_TEAMS}")['api-urls']['main-api']
    api_ver = get_config(f"u.{HOSTS_TEAMS}")['api-version']

    user_ws = UserClientTeamsSWA(
        api_url=api_url,
        api_ver=api_ver,
        uin=LOGIN_TEAMS_SWA,
        email_password=PASS_TEAMS_SWA,
        redirect=api_url,
        login_adapter=ClientAdapterTeamsSWA(base_url=api_url),
    )

    user = user_ws.login()
    assert LOGIN_TEAMS_SWA in user[0]
    assert "https://u.vkt-auth-test.vkteams.vkwm.ru" in user[1]