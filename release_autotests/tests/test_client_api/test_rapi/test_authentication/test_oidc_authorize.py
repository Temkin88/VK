import allure

from support.markers import SANDBOX, PRE_TARM, TARM, PRE_VKTI, VKTI, SAAS, PRE_SAAS


@allure.id("83031")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Авторизация")
@allure.feature("Начать OpenID Connect авторизацию")
@allure.title("OIDC авторизация через IDP, зарегистрированный на сервере")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_rapi_auth_oidc_authorize(
    auth_account,
):
    """
    Проверяем начало OpenID Connect авторизации

    Используемые параметры:
    :param auth_account: аккаунт ICQ
    """
    with allure.step("Пробуем отправить запрос"):
        response = auth_account.rapi_auth_oidc_authorize()

        assert response.status_code == 302, "Response code error"
        assert "Location" in response.headers, "Redirect not included"
