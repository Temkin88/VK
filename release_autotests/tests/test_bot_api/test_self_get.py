import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("37487")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Запрос self/get")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_bot_self_get(
    bot_class,
):
    with allure.step("Пробуем сделать запрос self/get"):
        response = bot_class.self_get()

    with allure.step("Проверяем ответ"):
        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")

        assert response_info.get("userId") == bot_class.uin, "UIN not supplied in server response"
