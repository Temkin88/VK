import allure
import pytest


@pytest.fixture(scope="session", autouse=True)
def login_admin(admin_account, alter_sandbox, auth_account, ENV_PLATFORM):
    if alter_sandbox or ENV_PLATFORM == "PRE_TARM":
        with allure.step("Отправляем OTP код"):
            admin_account.auth_otp_generate(
                email=admin_account.uin,
            )

        with allure.step("Отправляем OTP код"):
            otp_token = admin_account.get_otp_token(
                login=admin_account.uin,
            )

        with allure.step("Проверяем присланный OTP код"):
            admin_account.auth_otp_check(
                email=admin_account.uin,
                password=otp_token,
            )
    else:
        with allure.step("Отправляем OTP код"):
            admin_account.auth_otp_generate(
                email=admin_account.uin,
            )

        with allure.step("Проверяем присланный OTP код"):
            admin_account.auth_otp_check(
                email=admin_account.uin,
                password="ONPREM",
            )

    yield

    with allure.step("Проверяем существование сессии"):
        admin_account.auth_logout()


@pytest.fixture(
    params=[pytest.param(None, marks=pytest.mark.Godmod)],
    autouse=True,
)
def godmod_mark(): ...
