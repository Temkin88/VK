import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("66410")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Авторизация")
@allure.feature("Сессии")
@allure.title("Старт сессии для миниаппа")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_rapi_webapp_session_start(
    miniapp_id: str,
    auth_account,
):
    with allure.step("Пробуем стартовать сессию"):
        response = auth_account.rapi_webapp_session_start(miniapp_id)
        assert response["status"]["code"] == 20000, "Response code error"

    with allure.step("Проверяем старт сессии с одинаковыми miniapp_id"):
        same_miniapp_id = auth_account.rapi_webapp_session_start(miniapp_id)
        assert same_miniapp_id["status"]["code"] == 20000, "Response code error"
        assert response["results"]["aimsid"] == same_miniapp_id["results"]["aimsid"], "AimsId not equal"

    with allure.step("Проверяем старт сессии с разными miniapp_id"):
        different_miniapp_id = auth_account.rapi_webapp_session_start("test_miniapp_id")
        assert different_miniapp_id["status"]["code"] == 20000, "Response code error"
        assert response["results"]["aimsid"] != different_miniapp_id["results"]["aimsid"], "AimsId equal"
