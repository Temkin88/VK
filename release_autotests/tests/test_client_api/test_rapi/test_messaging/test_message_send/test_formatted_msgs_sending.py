import allure
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
)
from tenacity import sleep

from support.cases.invalid_formatted_msgs_parts import invalid_formatted_msgs_parts
from support.cases.correct_formatted_msgs_parts import correct_formatted_msgs_parts

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS


@allure.id("513347")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверяем функицонала отправку сообщений с корректным форматированием")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
@pytest.mark.parametrize(
    "correct_formatted_msg_parts",
    correct_formatted_msgs_parts,
)
def test_formatted_msg_sending(
    chat_type,
    correct_formatted_msg_parts,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверяем функицонала отправку сообщений с корректным форматированием
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправка сообщения с корректным форматированием"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts=correct_formatted_msg_parts,
        )
        assert response["status"]["code"] == 20000, f"Failed to send correctly formatted msg to chat ID {chat}"
    send_msg_id = response["results"]["msgId"]

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Ждем"):
        sleep(10)

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        assert check_events_list_contains_event_with_msgId(opponent, send_msg_id), "Sended message not found in events"


@allure.id("513356")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала отправки сообщений с некорректно форматированием")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
@pytest.mark.parametrize(
    "invalid_formatted_msg_parts",
    invalid_formatted_msgs_parts,
)
def test_invalid_formatted_msg_sending(
    chat_type,
    invalid_formatted_msg_parts,
    prepare_test_chats_msg,
):
    """
    Проверка функционала отправки сообщений с некорректно форматированием
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with (
        allure.step("Отправка сообщения с некорректным форматированием"),
        pytest.raises(BadRequestException),
    ):
        main_acc.rapi_message_send(
            target=chat,
            parts=invalid_formatted_msg_parts,
        )
