import allure
import pytest

from api.client.adapter import ClientAdapterTeamsSSO
from api.client.client import UserClientTeamsSSO
from common.config import HOSTS_TEAMS, LOGIN_TEAMS_SSO, PASS_TEAMS_SSO
from conftest import get_config
from markers import TEAMS


@TEAMS
@pytest.mark.parametrize("subscriptions", ["message", 123, {}, [], None, ''])
def test_with_session_failed_params(get_config, SANDBOX, subscriptions: str) -> None:
    host = SANDBOX.replace("https://", "vkt-", 1)
    api_url = get_config(f"u.{host}")['api-urls']['main-api']
    api_ver = get_config(f"u.{host}")['api-version']
    user_ws = UserClientTeamsSSO(
        api_url=api_url,
        api_ver=api_ver,
        uin=LOGIN_TEAMS_SSO,
        email_password=PASS_TEAMS_SSO,
        login_adapter=ClientAdapterTeamsSSO(base_url=api_url),
    )

    with allure.step("Проверяем различные сообщения в поле subscriptions метода withSession"):
        if subscriptions == 123:
            user_with_session = user_ws.with_session(subscriptions=subscriptions)
            assert user_with_session["message"] == 'Bad Request'
        else:
            user_with_session = user_ws.with_session(subscriptions=subscriptions)
            assert user_with_session['start_session_response']['response']["statusCode"] == 200
