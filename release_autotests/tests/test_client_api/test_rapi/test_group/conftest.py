import uuid

import allure
import pytest


@pytest.fixture(scope="session")
def create_chat_with_public_join_moderation(auth_account):
    with allure.step("Создаем чат"):
        name = f"Test group {uuid.uuid4().hex}"
        chat_id = auth_account.create_chat(
            name=name,
            public=True,
            joinModeration=False,
        )
        stamp = auth_account.get_chat_stamp(chat_id)

        yield chat_id, stamp
