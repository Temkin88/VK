import time

import allure
import pytest


def get_users(
    admin,
    auth,
):
    with allure.step("Получаем пользователей"):
        RETRIES = 3
        for _ in range(RETRIES):
            response = admin.api_users(
                filter_name=auth.uin,
                filter_blocked=False,
                filter_last_activity=0,
                filter_never_went=False,
                domains=["autotest.clients"],
            )
            if response["result"]["page_data"]["count"] > 0:
                break
            else:
                time.sleep(3)
                continue

        yield response


@pytest.fixture(scope="session")
def user_id(admin_account, auth_account):
    with allure.step("Получаем user_id пользователей"):
        response = list(get_users(admin=admin_account, auth=auth_account))

        yield response[0]["result"]["users"][0]["id"]
