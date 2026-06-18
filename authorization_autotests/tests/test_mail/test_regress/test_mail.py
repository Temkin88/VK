from api.client.adapter import ClientAdapterWs
from api.client.client import UserClientWS, UserClientWSSSO
from common.config import LOGIN_WS, PASS_WS
from conftest import get_config
from markers import WS_INTEGRATION, WS_ONPREMDEV


def test_mail(get_config, SANDBOX):
    user_ws = UserClientWS(
        base_url=SANDBOX,
        username=LOGIN_WS,
        password=PASS_WS,
        login_adapter=ClientAdapterWs(base_url=SANDBOX),
    )
    user_ws.login()
    user_check = user_ws.auth_check()
    assert LOGIN_WS == user_check["data"]["email"]
    assert LOGIN_WS in user_check["data"]["list"]

    # "autotest{001-10}@sso.auth-test.vkteams.vkwm.ru" - кейклок
    # "autotest{001-10}@swa.auth-test.vkteams.vkwm.ru" - по паролю почты
    # "autotest{001-10}@otp.auth-test.vkteams.vkwm.ru" - одноразовый пароль


def test_mail_2(get_config, SANDBOX):
    LOGIN_WS = "test777@ad2013.on-premise.ru"
    PASS_WS = "12345"
    user_ws = UserClientWSSSO(
        base_url=SANDBOX,
        username=LOGIN_WS,
        password=PASS_WS,
        login_adapter=ClientAdapterWs(base_url=SANDBOX),
    )
    user_ws.login()
    user_check = user_ws.auth_check()
    assert LOGIN_WS == user_check["data"]["email"]
    assert LOGIN_WS in user_check["data"]["list"]