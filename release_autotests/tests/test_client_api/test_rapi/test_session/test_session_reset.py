import allure
import pytest

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("85337")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Авторизация")
@allure.feature("Сессии")
@allure.title("Завершает сессию которой соответствует hash")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_rapi_session_reset(
    auth_account,
):
    with allure.step("Пробуем получить все сессии"):
        response = auth_account.rapi_session_list()

    with allure.step("Пробуем сбросить любую сессию кроме текущей"):
        for session in filter(
            lambda x: not x.get("current", False),
            response["results"]["sessions"],
        ):
            auth_account.rapi_session_reset(
                session_hash=session["hash"],
            )
            break


@allure.id("85336")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Авторизация")
@allure.feature("Сессии")
@allure.title("Завершает сессию которой соответствует hash с невалидными типами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_type", ["", [], {}, 1234, None])
def test_rapi_session_reset_invalid_type(
    auth_account,
    invalid_type,
):
    with allure.step("Пробуем сбросить выбранную сессию"), pytest.raises(BadRequestException):
        auth_account.rapi_session_reset(
            session_hash=invalid_type,
        )
