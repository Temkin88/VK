import allure

from support.markers import SANDBOX


@allure.id("79672")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление статусами пользователя")
@allure.title(
    "Получение текущей локали статусов",
)
@SANDBOX
def test_get_statuses(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.get_api_settings_statuses_local()


@allure.id("79668")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Управление статусами пользователя")
@allure.title(
    "Обновление текущей локали статусов",
)
@SANDBOX
def test_post_statuses(admin_account):
    with allure.step("Пробуем сделать запрос"):
        admin_account.post_api_settings_statuses_local("en")
