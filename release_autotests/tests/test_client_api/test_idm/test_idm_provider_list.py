import allure

from support.markers import SAAS, SANDBOX, TARM, PRE_TARM, SLA, PRE_SAAS


@allure.id("508377")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("idm")
@allure.feature("Email пользователя по которому определяется доступный список видов аутентификации")
@allure.title("Email пользователя по которому определяется доступный список видов аутентификации")
@SAAS
@PRE_SAAS
@SANDBOX
@TARM
@PRE_TARM
@SLA
def test_idm_provider_list(auth_account):
    with allure.step("Пробуем добавить новый вид аутентификации"):
        response = auth_account.idm_provider_list(email=auth_account.uin)

        assert response["status"]["code"] == 20000, "Response code error"
