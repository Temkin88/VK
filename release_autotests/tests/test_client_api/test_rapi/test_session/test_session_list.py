import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("37494")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Авторизация")
@allure.feature("Сессии")
@allure.title("Получение списка сессий текущего пользователя")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_rapi_session_list(
    auth_account,
):
    with allure.step("Пробуем сделать запрос"):
        response = auth_account.rapi_session_list()

    with allure.step("Проверяем ответ"):
        assert list(filter(lambda x: x.get("current", False), response["results"]["sessions"])), (
            "No current session in sessions list"
        )
