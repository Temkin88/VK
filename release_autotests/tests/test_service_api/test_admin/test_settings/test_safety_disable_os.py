import allure

from support.markers import SANDBOX


@allure.id("79661")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Настройки")
@allure.title(
    "Выключение автообновлений",
)
@SANDBOX
def test_safety_disable_os(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.api_settings_safety_disable_os(
            os_disable=[
                "android",
                "win_32",
                "ios",
            ],
        )
