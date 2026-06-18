import allure

from support.markers import SAAS, SANDBOX, PRE_SAAS


@allure.id("507928")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("idm")
@allure.feature("Удалить тип аутентификации из домена")
@allure.title("Удаление типа аутентификации из домена")
@SAAS
@PRE_SAAS
@SANDBOX
def test_idm_admin_provider_delete(auth_account, get_admin_token):
    with allure.step("Пробуем добавить новый вид аутентификации"):
        response = auth_account.idm_admin_provider_create(
            _type="OTP", domain="dev6.on-premise.ru", access_token=get_admin_token
        )

        assert response["status"]["code"] == 20000, "Response code error"

    with allure.step("Пробуем удалить тип аутентификации"):
        response = auth_account.idm_admin_provider_delete(
            _type="OTP", domain="dev6.on-premise.ru", access_token=get_admin_token
        )

        assert response["status"]["code"] == 20000, "Response code error"
