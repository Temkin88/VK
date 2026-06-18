import allure

from support.markers import SAAS, SANDBOX, PRE_SAAS


@allure.id("507929")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("idm")
@allure.feature("Получить список доступных типов аутентификации для домена")
@allure.title("Получение списка доступных типов аутентификации")
@SAAS
@PRE_SAAS
@SANDBOX
def test_idm_admin_provider_list(auth_account, create_admin_provider, get_admin_token):
    with allure.step("Проверяем, что в списке есть все типы доменов"):
        type_list = ["ESIA", "SWA", "OTP", "SSO"]

        response = auth_account.idm_admin_provider_list(domain="dev6.on-premise.ru", access_token=get_admin_token)
        result = response["results"]["providers"]

        assert result
        assert all(_type["type"] in type_list for _type in result)
        assert all(_type["available"] for _type in result if _type["type"] == "OTP")
