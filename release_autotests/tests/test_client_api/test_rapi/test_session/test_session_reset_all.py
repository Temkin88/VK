import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("37495")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Авторизация")
@allure.feature("Сессии")
@allure.title("Сброс всех других сессий текущего пользователя")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_rapi_session_reset_all(
    auth_account,
):
    with allure.step("Пробуем сбросить все сессии кроме текущей"):
        auth_account.rapi_session_resetAll()
