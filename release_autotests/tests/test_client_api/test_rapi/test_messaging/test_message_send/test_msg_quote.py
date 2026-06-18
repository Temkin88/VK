import allure
import lorem
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    check_mentions_in_fetch_events,
    correct_message,
    send_msg_to_quote_it_later,
)


def get_target_chat(chat_type, opponent_sn, group, channel):
    if chat_type == "private":
        chat = opponent_sn
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    return chat


@allure.id("515286")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала ответа на сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quote_with_quote_text(chat_type, prepare_test_chats_msg):
    """
    Проверка функционала ответа на сообщения
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    chat = get_target_chat(chat_type, opponent_acc.uin, group, channel)

    author_sn, plain_to_quote, text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat)

    with allure.step("Ответ на текстовое сообщение"):
        mentions_msg_id = main_acc.quote_message_by_message_send(
            target=chat,
            author_sn=opponent_acc.uin,
            plain_text=lorem.sentence(),
            plain_to_quote=plain_to_quote,
            msg_id=text_msg_id,
        )

    """
    Меншн возникает только для чатов / каналов при ответе на сообщение
    """
    mention_occurs = chat_type != "private"
    check_mentions_in_fetch_events(
        mentions_msg_id,
        receive_mention_from_chat=chat,
        auth_account=opponent_acc,
        mentioned_users=[opponent_acc.uin] if mention_occurs else [],
        check_mention_me_event=mention_occurs,
        unread_mention_me_count=None if mention_occurs else 1,
    )


@allure.id("515289")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала ответа на сообщения без самого текста ответа")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quote_wo_quote_text(
    chat_type,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка функционала ответа на сообщения без самого текста ответа
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    chat = get_target_chat(chat_type, opponent_acc.uin, group, channel)

    author_sn, plain_to_quote, text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat)

    with allure.step("Ответ на текстовое сообщение без самого текста ответа"):
        send_msg_id = main_acc.quote_message_by_message_send(
            target=chat,
            author_sn=opponent_acc.uin,
            plain_to_quote=plain_to_quote,
            msg_id=text_msg_id,
        )
    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        for account in [main_acc, opponent_acc]:
            assert check_events_list_contains_event_with_msgId(account, send_msg_id), (
                f"Sended message not found in events of {account}"
            )


@allure.id("515278")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала ответа на сообщения: ответ с созданием задачи")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quotes_task_creation(
    chat_type,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка функционала ответа на сообщения: ответ с созданием задачи
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    chat = get_target_chat(chat_type, opponent_acc.uin, group, channel)

    author_sn, plain_to_quote, text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat)

    with allure.step("Ответ на текстовое сообщение с созданием задачи в качестве ответа"):
        send_msg_id = main_acc.quote_message_by_message_send(
            target=chat,
            author_sn=opponent_acc.uin,
            plain_to_quote=plain_to_quote,
            main_part={"task": {"title": correct_message}},
            msg_id=text_msg_id,
        )
    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        for account in [main_acc, opponent_acc]:
            assert check_events_list_contains_event_with_msgId(account, send_msg_id), (
                f"Sended message not found in events of {account}"
            )


@allure.id("515283")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала ответа на сообщения: ответ с созданием опроса")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quotes_poll_creation(
    chat_type,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка функционала ответа на сообщения: ответ с созданием опроса
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    chat = get_target_chat(chat_type, opponent_acc.uin, group, channel)

    author_sn, plain_to_quote, text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat)

    with allure.step("Ответ на текстовое сообщение с созданием опроса в качестве ответа"):
        send_msg_id = main_acc.quote_message_by_message_send(
            target=chat,
            author_sn=author_sn,
            plain_to_quote=plain_to_quote,
            main_part={
                "text": {"plain": "Yes or no?"},
                "poll": {
                    "type": "anon",
                    "responses": ["yes", "no"],
                },
            },
            msg_id=text_msg_id,
        )
    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        assert check_events_list_contains_event_with_msgId(opponent_acc, send_msg_id), (
            "Sended message not found in events"
        )
