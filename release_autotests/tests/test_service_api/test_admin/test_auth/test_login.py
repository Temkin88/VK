import allure
import pytest

from pyvkteamsclient.admin.exceptions import RequestException
from support.markers import SANDBOX, PRE_TARM


@allure.id("28695")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Авторизация")
@allure.title(
    "Авторизация в админке",
)
@SANDBOX
@PRE_TARM
def test_login(admin_account, alter_sandbox):
    if alter_sandbox:
        with allure.step("Отправляем OTP код"):
            otp_token = admin_account.get_otp_token(
                login=admin_account.uin,
            )

        with allure.step("Проверяем присланный OTP код"):
            response = admin_account.auth_otp_check(
                email=admin_account.uin,
                password=otp_token,
            )

            assert response["status"]["code"] == 202, "Response code error"
            assert response["status"]["reason"] == "authorized", "Not authorizad"
            assert admin_account.uin == response["result"]["email"], "Uin dont match"
    else:
        with allure.step("Отправляем OTP код"):
            response = admin_account.auth_otp_generate(
                email=admin_account.uin,
            )

            assert response["status"]["code"] == 200, "Response code error"
            assert response["status"]["reason"] == "One-time password sent to your email", (
                "Password not sent to your email"
            )

        with allure.step("Проверяем присланный OTP код"):
            response = admin_account.auth_otp_check(
                email=admin_account.uin,
                password="ONPREM",
            )

            assert response["status"]["code"] == 202, "Response code error"
            assert response["status"]["reason"] == "authorized", "Not authorizad"
            assert admin_account.uin == response["result"]["email"], "Uin dont match"

    with allure.step("Проверяем существование сессии"):
        response = admin_account.api_permissions()

        assert response["status"]["code"] == 200, "Response code error"

        result = response["result"]["Permissions"]["Resources"]

        assert all(result[resourse]["Default"] == "allow" for resourse in result)


@allure.id("79788")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Авторизация")
@allure.title(
    "Авторизация в админке с невалидными данными",
)
@SANDBOX
def test_login_is_invalid_params(admin_account, alter_sandbox):
    with allure.step("Отправляем OTP код"), pytest.raises(RequestException):
        admin_account.auth_otp_generate(
            email="test{}@autotest.clients",
        )

    with allure.step("Проверяем присланный OTP код"), pytest.raises(RequestException):
        admin_account.auth_otp_check(
            email="test{}@autotest.clients",
            password="",
        )
