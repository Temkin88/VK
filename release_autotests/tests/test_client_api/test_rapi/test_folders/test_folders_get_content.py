import allure
import pytest

from pyvkteamsclient.client import RequestException
from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, PRE_VKTI, VKTI, SAAS, PRE_SAAS


@allure.id("83377")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Получить содержимое папки")
@allure.title("Получаем содержимое папки")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_folders_get_content(
    prepare_test_chats,
    fetch_until_empty_answer,
    event_filter,
    second_folder_id,
):
    auth_account, _, group, channel = prepare_test_chats

    with allure.step("Пробуем получить содержимое папки"):
        chats = [group, channel]
        response = auth_account.rapi_folders_get_content(folder_id=second_folder_id)
        assert all(chat in chats for chat in response["results"]["chats"]), "Chat not found"


@allure.id("83371")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Получить содержимое папки")
@allure.title("Получаем содержимое папки с невалидными параметрами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_param", ["", [], {}, None])
def test_folders_get_content_invalid_param(auth_account, invalid_param):
    with (
        allure.step("Пытаемя получить содержимое папки с невалидными параметрами"),
        pytest.raises((RequestException, BadRequestException)),
    ):
        auth_account.rapi_folders_get_content(folder_id=invalid_param)
