import allure
import pytest
from requests import Session

from pyvkteamsclient.client import DesktopClient
from pyvkteamsclient.client.exceptions import MissingParameterException


@allure.id("86723")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Авторизация")
@allure.feature("Авторизация пользователя по телефонному номеру")
@allure.title("Авторизоваться пользоватем по телефонному номеру")
def test_smsreg_login_with_phone_number(
    accounts_data,
):
    """
    Проверяем авторизацию по телефонному номеру

    Используемые параметры:
    :param accounts_data: данные аккаунта
    """
    with allure.step("Создаем аккаунт"):
        account = accounts_data[0]
        session = Session()
        auth_account = DesktopClient(
            uin=account["uin"],
            session=session,
            phone=account["phone"],
            code=account["code"],
            api_url="https://u.icq.net",
            binary_api_url="https://ub.icq.net",
            api_ver=110,
            env="ICQ",
            forced_ip=None,
        )

    with allure.step("Пробуем запросить код для телефонного номера"):
        trans_id = auth_account.smsreg_requestPhoneValidation()["response"]["data"]["trans_id"]

    with allure.step("Пробуем авторизоваться пользоватем по номером телефона"):
        result = auth_account.smsreg_loginWithPhoneNumber(trans_id=trans_id)

        assert result["response"]["statusCode"] == 200, "Failed request"

        assert isinstance(result["response"]["requestId"], str), "Failed to type"

        assert result["response"]["data"]["phone_verified"], "Failed to phone verified"

        assert isinstance(result["response"]["data"]["token"]["a"], str), "Failed to type"


@allure.id("86721")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Авторизация")
@allure.feature("Авторизация пользователя по телефонному номеру")
@allure.title("Авторизоваться пользоватем по телефонному номеру с невалидными типами")
@pytest.mark.parametrize("invalid_type", [123, [], {}, None])
def test_smsreg_login_with_phone_number_invalid_param(
    accounts_data,
    invalid_type,
):
    with allure.step("Создаем аккаунт"):
        account = accounts_data[0]
        session = Session()
        auth_account = DesktopClient(
            uin=account["uin"],
            session=session,
            phone=account["phone"],
            code=account["code"],
            api_url="https://u.icq.net",
            binary_api_url="https://ub.icq.net",
            api_ver=110,
            env="ICQ",
            forced_ip=None,
        )
    with pytest.raises(MissingParameterException):
        auth_account.smsreg_loginWithPhoneNumber(trans_id=invalid_type)
