from urllib.parse import urlparse

import allure
import pytest

from support.markers import SANDBOX, PRE_TARM, TARM, PRE_VKTI, VKTI, SAAS, PRE_SAAS


@allure.id("83032")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Авторизация")
@allure.feature("Продолжить OpenID Connect авторизацию")
@allure.title("Продолжаем OpenID Connect авторизацию")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.skip("Не реализован метод с 2fa для получения данных")
def test_rapi_auth_oidc_submite_code(
    auth_account,
):
    """
    Проверяем продолжение OpenID Connect авторизации

    Используемые параметры:
    :param auth_account: аккаунт ICQ
    """
    with allure.step("Пробуем отправить запрос"):
        response = auth_account.rapi_auth_oidc_authorize()
        assert response.status_code == 302
    with allure.step("Пробуем получить state и code"):
        parsed_url = urlparse(response.headers["Location"])
        query = {key: value for key, value in [item.split("=") for item in parsed_url.query.split("&")]}  # noqa: C416

    with allure.step("Пробуем продолжить авторизацию"):
        auth_account.rapi_auth_oidc_submitCode(
            state=query.get("state", "NoState"),
            code=query.get("code", 20000),
        )
