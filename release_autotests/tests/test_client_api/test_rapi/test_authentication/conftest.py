import allure
import pytest


@pytest.fixture(scope="session")
def session_id(
    auth_account,
):
    with allure.step("Получаем session_id"):
        return auth_account.rapi_auth_send_сode()["results"]["sessionId"]
