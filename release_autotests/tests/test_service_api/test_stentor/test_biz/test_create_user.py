import allure

from pyvkteamsclient.client import DesktopClient

from support.markers import SANDBOX


@allure.id("109192")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Biz")
@allure.title(
    "Проверка авторизации пользователем, созданным через метод biz/createUser",
)
@SANDBOX
def test_create_user_and_check_auth(
    ENV_PLATFORM,
    stentor_account,
    main_api,
    binary_api,
    api_version,
):
    with DesktopClient(
        uin=stentor_account["email"],
        api_url=main_api,
        binary_api=binary_api,
        api_ver=api_version,
        fix_otp="ONPREM",
        env=ENV_PLATFORM,
    ) as client:
        client.send_basic_message(
            sn=client.uin,
            text="test",
        )
