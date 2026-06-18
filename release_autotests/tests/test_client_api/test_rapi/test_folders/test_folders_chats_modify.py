import uuid

import allure
import pytest

from pyvkteamsclient.client import RequestException
from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, PRE_VKTI, VKTI, SAAS, PRE_SAAS


@allure.id("83376")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Изменение содержимого папки")
@allure.title("Добавляет/удаляет чаты в папке")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_folders_chats_modify(
    auth_account,
    opponent_account,
    prepare_test_chats,
    fetch_until_empty_answer,
    event_filter,
    folder_id,
):
    _, _, group, channel = prepare_test_chats

    chats = []
    for _ in range(3):
        chat_id = auth_account.create_chat(
            f"Test channel - {uuid.uuid4().hex}",
            defaultRole="readonly",
            members=[opponent_account],
        )
        chats.append(chat_id)

    with allure.step("Пробуем изменить содержимое папки"):
        event_filter.start_point()
        auth_account.rapi_folders_chats_modify(
            folder_id=folder_id,
            add_chats=chats,
        )

    with allure.step("Проверяем что содержимое папок изменилось"):
        content = auth_account.rapi_folders_get_content(folder_id=folder_id)
        assert all(chat in content["results"]["chats"] for chat in chats), "Chat not found"

    with allure.step("Проверяем что событияе создалось"):
        for event in event_filter(auth_account.events[::-1], "folders"):
            folders_list = [folder["id"] for folder in event["eventData"]["folders"]]
            assert folder_id in folders_list, 'Event "Folders" not found'


@allure.id("83374")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Изменение содержимого папки")
@allure.title("Добавляет/удаляет чаты в папке с невалидными параметрами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_param", ["", 1234, [], {}, None])
def test_folders_chats_modify_invalid_param(auth_account, invalid_param):
    with (
        allure.step("Пытаемя удалить папку с чатами с невалидными параметрами"),
        pytest.raises((RequestException, BadRequestException)),
    ):
        auth_account.rapi_folders_chats_modify(
            folder_id=invalid_param,
            add_chats=invalid_param,
        )
