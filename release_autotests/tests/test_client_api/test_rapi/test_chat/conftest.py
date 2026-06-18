import uuid

import allure
import pytest


@pytest.fixture(scope="session", params=["group", "readonly"])
def create_chat_id(
    request,
    auth_account,
):
    with allure.step("Пробуем создать тестовый чат"):
        name = f"Test {request.param} - {uuid.uuid4().hex}"
        default_role = "member" if request.param == "group" else "readonly"

        chat_id = auth_account.create_chat(
            name=name,
            defaultRole=default_role,
        )

        yield chat_id
