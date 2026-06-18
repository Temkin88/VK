import allure
import pytest

from pyvkteamsclient.client import RequestException
from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, PRE_VKTI, VKTI, SAAS, PRE_SAAS


@allure.id("83375")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Изменение порядка папок")
@allure.title("Расставляет папки в указанном порядке")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_folders_reorder(
    opponent_account,
    prepare_test_chats,
    fetch_until_empty_answer_with_filter,
    folder_id,
    event_filter,
):
    with allure.step("Ищем последние событие folders"):
        opponent_account.rapi_folders_create(
            title="Test folder",
            chats=prepare_test_chats[2:],
        )

        opponent_account.rapi_request_folders()

        folders_event = None

        for event in fetch_until_empty_answer_with_filter(opponent_account, "folders")[::-1]:
            folders_event = event
            break

        folders_order = [folder["id"] for folder in folders_event["eventData"]["folders"]]
        folders_new_order = folders_order[::-1]

    with allure.step("Пробуем изменить наименование папки"):
        event_filter.start_point()

        assert opponent_account.rapi_folders_reorder(
            new_folder_ids_order=folders_new_order,
        )

    with allure.step("Проверяем что в событиях появилось новой событие в правильном порядке папки"):
        folders_event_found = False

        for event in fetch_until_empty_answer_with_filter(opponent_account, "folders")[::-1]:
            folders_order = [folder["id"] for folder in event["eventData"]["folders"]]

            if folders_order == folders_new_order:
                folders_event_found = True
                break

        assert folders_event_found, 'Event "Folders" after reorder not found'


@allure.id("83369")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Папки")
@allure.feature("Изменение порядка папок")
@allure.title("Расставляет папки в указанном порядке с невалидными параметрами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "invalid_param",
    ["", 1234, [], {}, None],
)
def test_folders_reorder_invalid_param(
    auth_account,
    invalid_param,
):
    with (
        allure.step("Пытаемя удалить папку с чатами с невалидными параметрами"),
        pytest.raises((RequestException, BadRequestException)),
    ):
        auth_account.rapi_folders_reorder(
            new_folder_ids_order=invalid_param,
        )
