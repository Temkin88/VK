import allure

from support.markers import SANDBOX


@allure.id("79660")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Настройки")
@allure.title(
    "Проверка ключа антивируса",
)
@SANDBOX
def test_safety_key(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.api_settings_safety_key(
            "test",
            "test",
        )
