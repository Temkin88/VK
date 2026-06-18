import allure

from support.markers import SAAS, SANDBOX, PRE_SAAS


@allure.id("508346")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("idm")
@allure.feature("Внутренний метод проверки валидности токена")
@allure.title("Внутренний метод проверки валидности токена")
@SAAS
@PRE_SAAS
@SANDBOX
def test_idm_auth_validate(auth_account):
    response = auth_account.idm_auth_validate(access_token=auth_account.token)
    results = response["results"]

    assert results["user_sn"] == auth_account.uin, f"User={results['user_sn']} dont matched"
