from time import sleep

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    correct_message_with_mentions,
    check_mentions_in_fetch_events,
    correct_message,
)


@allure.id("513345")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки файла с подписью")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_captioned_content_sending(
    chat_type,
    prepare_test_chats_msg,
    photo,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки файла с подписью
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем ссылку на фото с подписью"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "captionedContent": {"url": photo, "caption": {"plain": correct_message}},
                },
            },
        )
        assert response["status"]["code"] == 20000, f"Failed to send captionedContent to chat ID {chat}"

    send_msg_id = response["results"]["msgId"]

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Ждем"):
        sleep(20)

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        assert check_events_list_contains_event_with_msgId(opponent, send_msg_id), "Sended message not found in events"


@allure.id("515244")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки файла с подписью и 2 меншенами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_captioned_content_sending_with_two_mentions(
    chat_type,
    prepare_test_chats_msg,
    photo,
    third_account,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки файла с подписью и 2 меншенами
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent_acc.uin
        receive_mention_from_chat = main_acc.uin
    elif chat_type == "group":
        chat = group
        receive_mention_from_chat = chat
    else:
        chat = channel
        receive_mention_from_chat = chat

    with allure.step("Отправляем ссылку на фото с подписью, в которой есть два меншена"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {
                    "captionedContent": {
                        "url": photo,
                        "caption": {"plain": correct_message_with_mentions([opponent_acc.uin, third_account.uin])},
                    },
                },
            },
        )
        status_code = response["status"]["code"]
        assert status_code == 20000, f"Failed to send captionedContent with two mentions to chat ID {chat}"
        msg_id = response["results"]["msgId"]

    check_mentions_in_fetch_events(
        msg_id,
        receive_mention_from_chat,
        opponent_acc,
        [opponent_acc.uin, third_account.uin],
        check_mention_me_event=True,
    )
    send_msg_id = msg_id

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        assert check_events_list_contains_event_with_msgId(opponent_acc, send_msg_id), (
            "Sended message not found in events"
        )
