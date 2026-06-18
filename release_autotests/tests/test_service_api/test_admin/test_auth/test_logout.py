import allure
import pytest

from support.markers import SANDBOX


@pytest.fixture
def relogin(admin_account):
    yield

    with allure.step("Отправляем OTP код"):
        admin_account.auth_otp_generate(
            email="autotest001@autotest.clients",
        )

    with allure.step("Проверяем присланный OTP код"):
        admin_account.auth_otp_check(
            email="autotest001@autotest.clients",
            password="ONPREM",
        )


@allure.id("28692")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Авторизация")
@allure.title(
    "Сброс сессии авторизации",
)
@SANDBOX
@pytest.mark.last
def test_logout(admin_account, relogin):
    with allure.step("Отправляем OTP код"):
        response = admin_account.auth_otp_generate(
            email="autotest001@autotest.clients",
        )

        assert response["status"]["code"] == 200, "Response code error"
        assert response["status"]["reason"] == "One-time password sent to your email", "Password not sent to your email"

    with allure.step("Проверяем присланный OTP код"):
        response = admin_account.auth_otp_check(
            email="autotest001@autotest.clients",
            password="ONPREM",
        )

        assert response["status"]["code"] == 202, "Response code error"
        assert response["status"]["reason"] == "authorized", "Not authorizad"
        assert response["result"]["email"] == "autotest001@autotest.clients", "Uin dont match"

    with allure.step("Проверяем существование сессии"):
        response = admin_account.auth_logout()

        assert response["status"]["code"] == 200, "Response code error"
        assert response["status"]["reason"] == "Signed out", "Not Log out"
