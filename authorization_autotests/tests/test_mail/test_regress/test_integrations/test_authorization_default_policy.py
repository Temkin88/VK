import allure

from api.client.adapter import ClientAdapterWs, ClientAdapterTeamsOTP
from api.client.client import UserClientWS, UserClientTeamsOTP
from markers import WS_INTEGRATION


@allure.id("2489850")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.story("Админка")
@allure.feature("Интеграционное тестирование VKT+WorkSpace")
@allure.title("Авторизация пользователя с политикой по умолчанию")
@WS_INTEGRATION
def test_authorization_default_policy(get_config, SANDBOX, account_otp):
    # login_ws = "1@otp.auth-test.vkteams.vkwm.ru"
    login_ws = account_otp["uin"]
    pass_ws = "Q-12345"
    user_ws = UserClientWS(
        base_url=SANDBOX,
        username=login_ws,
        password=pass_ws,
        login_adapter=ClientAdapterWs(base_url=SANDBOX),
    )
    user_ws.login()
    user_check = user_ws.auth_check()
    assert login_ws == user_check["data"]["email"]
    assert login_ws in user_check["data"]["list"]

    api_url = get_config(f"u.{SANDBOX.replace("https://", "vkt-", 1)}")['api-urls']['main-api']
    api_ver = get_config(f"u.{SANDBOX.replace("https://", "vkt-", 1)}")['api-version']
    imap_url = SANDBOX.replace("https://", "imap.", 1)
    url = SANDBOX.replace("https://", "https://u.vkt-", 1)

    user_teams = UserClientTeamsOTP(
        api_url=api_url,
        api_ver=api_ver,
        uin=login_ws,
        password=pass_ws,
        imap_url=imap_url,
        login_adapter=ClientAdapterTeamsOTP(base_url=api_url),
    )
    user = user_teams.login(fix_otp=False)

    assert login_ws in user[0]
    assert url in user[1]
