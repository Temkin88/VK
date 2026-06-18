import allure
import pytest

from pyvkteamsclient.client import RequestException
from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, PRE_VKTI, VKTI, SAAS, PRE_SAAS


@allure.id("83372")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Переименование папки")
@allure.title("Переименовывает папку по id")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_folders_rename(
    auth_account,
    fetch_until_empty_answer_with_filter,
    event_filter,
    folder_id,
):
    with allure.step("Пробуем изменить наименование папки"):
        assert auth_account.rapi_folders_rename(
            folder_id=folder_id,
            title="New test folder",
        )

    with allure.step("Проверяем что в событиях появилось новой событие с новым именем"):
        event_found_folder_id = False

        for event in fetch_until_empty_answer_with_filter(auth_account, "folders"):
            data = event["eventData"]["folders"]
            for folders_id in data[1:]:
                if folders_id["title"] == "New test folder":
                    event_found_folder_id = True

        assert event_found_folder_id, 'Event "Folders" with "New test folder" title not found'


@allure.id("83373")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Переименование папки")
@allure.title("Переименовывает папку по id с невалидными параметрами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_param", ["Test more 15 symbol", "", 1234, [], {}, None])
def test_folders_rename_invalid_param(auth_account, invalid_param):
    with (
        allure.step("Пытаемя удалить папку с чатами с невалидными параметрами"),
        pytest.raises((RequestException, BadRequestException)),
    ):
        auth_account.rapi_folders_rename(
            folder_id=invalid_param,
            title=invalid_param,
        )
