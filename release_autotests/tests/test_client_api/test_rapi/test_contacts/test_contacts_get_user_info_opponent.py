import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("31916")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Контакты")
@allure.feature("Запрос информации id")
@allure.title("Запрос информации id пользователя")
def test_contacts_get_user_info_opponent(
    auth_account,
    opponent_account,
):
    with allure.step("Пробуем получить информацию"):
        response = auth_account.rapi_getUserInfo(sn=opponent_account.uin)
        results = response["results"]

    with allure.step("Проверяем ответ сервера"):
        assert "friendly" in results, "Failed to get friendly"
        assert "firstName" in results, "Failed to get firstName"
        assert "lastName" in results, "Failed to get lastName"
