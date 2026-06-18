import string
import random

import allure
import pytest

from pyvkteamsclient.client import RequestException
from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, PRE_VKTI, VKTI, SAAS, PRE_SAAS


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = "".join(random.choice(letters) for i in range(length))
    return rand_string


@allure.id("83378")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Создать папку")
@allure.title("Создание папки")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_folders_create(prepare_test_chats, fetch_until_empty_answer_with_filter, event_filter):
    auth_account, _, group, channel = prepare_test_chats

    chats = [group, channel]

    with allure.step("Пытаемя создать папку с чатами"):
        response = auth_account.rapi_folders_create(
            title=f"Test {generate_random_string(10)}",
            chats=[group, channel],
        )

        assert isinstance(response["results"]["folderId"], int), "Folder id not int type"

    with allure.step("Проверяем что в папке добавлены чаты"):
        content = auth_account.rapi_folders_get_content(folder_id=response["results"]["folderId"])
        assert all(chat in content["results"]["chats"] for chat in chats), "Chat not found"

    with allure.step("Проверяем что папка появилась в событиях"):
        event_found_folder_id = False

        for event in fetch_until_empty_answer_with_filter(auth_account, "folders"):
            data = event["eventData"]["folders"]
            for folder_id in data:
                if response["results"]["folderId"] == folder_id["id"]:
                    event_found_folder_id = True

        assert event_found_folder_id, 'Event "Folders" not found'


@allure.id("83367")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Создать папку")
@allure.title("Создание папки с невалидными параметрами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("size_tite", ["Test more 15 symbol", "", 1234, [], {}, None])
def test_folders_create_invalid_param(auth_account, size_tite):
    with (
        allure.step("Пытаемя создать папку с чатами с невалидными параметрами"),
        pytest.raises((RequestException, BadRequestException)),
    ):
        auth_account.rapi_folders_create(
            title=size_tite,
            chats=size_tite,
        )
