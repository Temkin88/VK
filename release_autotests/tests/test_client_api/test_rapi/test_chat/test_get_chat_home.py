import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26902")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.suite("Чаты")
@allure.feature("Витрина чатов")
@allure.title("Получение списка чатов витрине")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_get_chat_home(auth_account):
    with allure.step("Делаем запрос"):
        response = auth_account.rapi_getChatHome(
            geo_lat=45,
            geo_lon=45,
            country="RU",
        )

    with allure.step("Проверяем ответ"):
        assert response["status"]["code"] == 20000, "Response code error"

        assert response["results"].get("items") is not None, "Empty chat home"
