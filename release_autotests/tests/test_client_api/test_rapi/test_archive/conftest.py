import uuid

import allure
import pytest

from pyvkteamsclient.client.exceptions import BadRequestException


@pytest.fixture(scope="session", params=["group", "channel"])
def create_archive_chats(request, auth_account, opponent_account):
    default_role = "member" if request.param == "group" else "readonly"

    with allure.step(f"Создаем тестовые чаты ({request.param})"):
        chats_list = [
            auth_account.create_chat(
                f"Test channel - {uuid.uuid4().hex}",
                defaultRole=default_role,
                members=[opponent_account],
            )
            for _ in range(2)
        ]

    return auth_account, chats_list


@pytest.fixture(scope="session", autouse=True)
def clean_archive_after_tests(auth_account):
    try:
        auth_account.rapi_archive_getContent()
    except BadRequestException as error:
        pytest.skip(str(error))

    yield

    response = auth_account.rapi_archive_getContent()

    archive = response["results"]["chats"]

    auth_account.rapi_archive_chatsModify(del_chats=archive)
