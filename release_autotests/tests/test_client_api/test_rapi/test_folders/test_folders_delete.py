import allure
import pytest

from pyvkteamsclient.client import RequestException
from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, PRE_VKTI, VKTI, SAAS, PRE_SAAS


@allure.id("83379")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Удалить папку")
@allure.title("Удаление папки")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_folders_delete(prepare_test_chats, fetch_until_empty_answer_with_filter, event_filter):
    auth_account, _, group, channel = prepare_test_chats

    with allure.step("Создаем папку с чатами"):
        folders_id = auth_account.rapi_folders_create(
            title="Test folders",
            chats=[group, channel],
        )["results"]["folderId"]

    with allure.step("Проверяем что папка появилась в событиях"):
        event_found_folder_id = False

        for event in fetch_until_empty_answer_with_filter(auth_account, "folders"):
            data = event["eventData"]["folders"]
            for folder_id in data[1:]:
                if folders_id == folder_id["id"]:
                    event_found_folder_id = True

        assert event_found_folder_id, "Folder id not found"

    with allure.step("Пробуем удалить папку"):
        assert auth_account.rapi_folders_delete(folder_id=folders_id)["status"]["code"] == 20000

    with allure.step("Проверяем что папка появилась в событиях"):
        event_found_folder_id = False

        for event in fetch_until_empty_answer_with_filter(auth_account, "folders"):
            data = event["eventData"]["folders"]
            for folder_id in data:
                if folders_id != folder_id["id"]:
                    event_found_folder_id = True

        assert event_found_folder_id, 'Event "Folders" not found'


@allure.id("83368")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Удалить папку")
@allure.title("Удаление папки с невалидными параметрами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_param", ["", 1234, [], {}, None])
def test_folders_delete_invalid_param(prepare_test_chats, invalid_param):
    auth_account, _, group, channel = prepare_test_chats

    with (
        allure.step("Пытаемя удалить папку с чатами с невалидными параметрами"),
        pytest.raises((RequestException, BadRequestException)),
    ):
        auth_account.rapi_folders_delete(folder_id=invalid_param)
