import allure


@allure.id("79693")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Авторизация")
@allure.title(
    "Проверка существования сессии",
)
def test_auth_check(admin_account):
    admin_account.auth_check()
