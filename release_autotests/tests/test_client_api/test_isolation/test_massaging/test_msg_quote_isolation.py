import allure
import lorem
import pytest

from support.markers import SAAS, ISOLATION, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    check_mentions_in_fetch_events,
    correct_message,
    send_msg_to_quote_it_later,
)


def get_target_chat(chat_type, main_sn, opponent_sn, group, channel):
    if chat_type == "private":
        chat = opponent_sn
    elif chat_type == "group":
        chat = group
    elif chat_type == "favorite":
        chat = main_sn
    else:
        chat = channel
    return chat


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала ответа на сообщения")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quote_with_quote_text_isolation(chat_type, prepare_test_chats_msg_isolation):
    """
    Проверка функционала ответа на сообщения
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg_isolation

    chat = get_target_chat(chat_type, main_acc.uin, opponent_acc.uin, group, channel)

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
        chat,
        opponent_acc,
        [opponent_acc.uin] if mention_occurs else [],
        mention_occurs,
    )


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала ответа на сообщения  без самого текста ответа")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quote_wo_quote_text_isolation(chat_type, prepare_test_chats_msg_isolation):
    """
    Проверка функционала ответа на сообщения без самого текста ответа
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg_isolation

    chat = get_target_chat(chat_type, main_acc.uin, opponent_acc.uin, group, channel)

    author_sn, plain_to_quote, text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat)

    with allure.step("Ответ на текстовое сообщение без самого текста ответа"):
        assert main_acc.quote_message_by_message_send(
            target=chat,
            author_sn=opponent_acc.uin,
            plain_to_quote=plain_to_quote,
            msg_id=text_msg_id,
        )


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала ответа на сообщения: ответ с созданием задачи")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quotes_task_creation_isolation(chat_type, prepare_test_chats_msg_isolation):
    """
    Проверка функционала ответа на сообщения: ответ с созданием задачи
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg_isolation

    chat = get_target_chat(chat_type, main_acc.uin, opponent_acc.uin, group, channel)

    author_sn, plain_to_quote, text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat)

    with allure.step("Ответ на текстовое сообщение с созданием задачи в качестве ответа"):
        assert main_acc.quote_message_by_message_send(
            target=chat,
            author_sn=opponent_acc.uin,
            plain_to_quote=plain_to_quote,
            main_part={"task": {"title": correct_message}},
            msg_id=text_msg_id,
        )


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала ответа на сообщения: ответ с созданием опроса")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quotes_poll_creation_isolation(chat_type, prepare_test_chats_msg_isolation):
    """
    Проверка функционала ответа на сообщения: ответ с созданием опроса
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg_isolation

    chat = get_target_chat(chat_type, main_acc.uin, opponent_acc.uin, group, channel)

    author_sn, plain_to_quote, text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat)

    with allure.step("Ответ на текстовое сообщение с созданием опроса в качестве ответа"):
        assert main_acc.quote_message_by_message_send(
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


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала ответа на сообщения")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quote_with_quote_text_isolation_not_in_tenant(
    chat_type, prepare_test_chats_msg_isolation, first_auth_account_not_in_tenant, check_message_in_history
):
    """
    Проверка функционала ответа на сообщения
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg_isolation

    chat = get_target_chat(chat_type, main_acc.uin, opponent_acc.uin, group, channel)

    author_sn, plain_to_quote, text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat)

    with allure.step("Ответ на текстовое сообщение пользователем не из тенанта"), pytest.raises(Exception):
        msg_id = first_auth_account_not_in_tenant.quote_message_by_message_send(
            target=chat,
            author_sn=opponent_acc.uin,
            plain_text=lorem.sentence(),
            plain_to_quote=plain_to_quote,
            msg_id=text_msg_id,
        )
        assert check_message_in_history(
            acc=main_acc,
            sn=chat,
            msg_id=msg_id,
        )
