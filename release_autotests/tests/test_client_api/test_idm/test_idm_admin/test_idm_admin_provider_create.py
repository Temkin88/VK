import allure

from support.markers import SAAS, SANDBOX, PRE_SAAS


@allure.id("507926")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("idm")
@allure.feature("Добавить тип аутентификации домену")
@allure.title("Добавление типа аутентификации домену")
@SAAS
@PRE_SAAS
@SANDBOX
def test_idm_admin_provider_create(auth_account, get_admin_token):
    with allure.step("Пробуем добавить новый вид аутентификации"):
        response = auth_account.idm_admin_provider_create(
            _type="OTP", domain="dev6.on-premise.ru", access_token=get_admin_token
        )

        assert response["status"]["code"] == 20000, "Response code error"

    with allure.step("Проверяем что все типы OTP изменился"):
        response = auth_account.idm_admin_provider_list(domain="dev6.on-premise.ru", access_token=get_admin_token)
        result = response["results"]["providers"]

        assert all(_type["available"] for _type in result if _type["type"] == "OTP")
