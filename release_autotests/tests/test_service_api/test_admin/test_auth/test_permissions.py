import allure

from support.markers import SANDBOX


@allure.id("28690")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Авторизация")
@allure.title(
    "Авторизация в админке",
)
@SANDBOX
def test_login(admin_account):
    with allure.step("Проверяем существование сессии"):
        admin_account.api_permissions()
