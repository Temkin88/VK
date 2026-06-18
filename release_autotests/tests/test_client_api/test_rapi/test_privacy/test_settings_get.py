import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26904")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Настройки приватности")
@allure.feature("Получение настроек приватности")
@allure.title("Простое получение настроек приватности")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_get_privacy_settings(auth_account):
    """
    Проверяем получение настроек приватности
    """

    with allure.step("Делаем запрос"):
        response = auth_account.rapi_getPrivacySetting()

        assert response["status"]["code"] == 20000, "Failed request"

    with allure.step("Проверяем ответ"):
        assert response["results"].get("calls") is not None, "Calls settings not listed"
        assert response["results"].get("groups") is not None, "Groups settings not listed"
