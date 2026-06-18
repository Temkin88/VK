import allure

from support.markers import SANDBOX


@allure.id("79663")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Настройки")
@allure.title(
    "Получение настроек для VIP",
)
@SANDBOX
def test_get_settings_network(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.get_api_settings_vip()


@allure.id("79664")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Настройки")
@allure.title(
    "Изменение настроек для VIP",
)
@SANDBOX
def test_post_settings_network(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.post_api_settings_vip(
            "test",
            "test",
            True,
            True,
        )
