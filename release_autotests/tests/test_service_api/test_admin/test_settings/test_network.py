import allure

from support.markers import SANDBOX


@allure.id("79666")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Настройки")
@allure.title(
    "Настройки сети",
)
@SANDBOX
def test_get_settings_network(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.get_api_settings_network()
