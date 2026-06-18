import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("31915")
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
def test_contacts_get_id_info_user(
    auth_account,
):
    with allure.step("Пробуем получить информацию"):
        response = auth_account.rapi_getIdInfo(_id=auth_account.uin)
        user = response["results"]["user"]

    with allure.step("Проверяем ответ сервера"):
        assert "sn" in user, "Failed to get sn"
        assert "firstName" in user, "Failed to get firstName"
        assert "lastName" in user, "Failed to get lastName"
