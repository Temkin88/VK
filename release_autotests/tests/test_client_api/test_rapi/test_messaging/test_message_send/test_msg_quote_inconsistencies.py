import allure
import lorem
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    formally_ok_but_invalid_user_sn,
    send_msg_to_quote_it_later,
)
from tests.test_client_api.test_rapi.test_messaging.test_message_send.test_msg_quote import get_target_chat


@allure.id("515287")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала ответа на сообщения: невалидный msgId пересылаемого сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quotes_with_invalid_quote_msg_id(chat_type, prepare_test_chats_msg):
    """
    Проверка функционала ответа на сообщения: невалидный msgId пересылаемого сообщения
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    chat = get_target_chat(chat_type, opponent_acc.uin, group, channel)

    author_sn, plain_to_quote, text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat)

    obviously_invalid_msg_id = 12345
    with allure.step("Ответ на текстовое сообщение с неправильным msg_id"):
        assert main_acc.quote_message_by_message_send(
            target=chat,
            author_sn=opponent_acc.uin,
            plain_to_quote=plain_to_quote,
            msg_id=obviously_invalid_msg_id,
        )


@allure.id("515291")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала ответа на сообщения: невалидный sn автора пересылаемого сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_quotes_with_invalid_quote_author_sn(chat_type, prepare_test_chats_msg):
    """
    Проверка функционала ответа на сообщения: невалидный sn автора пересылаемого сообщения
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    chat = get_target_chat(chat_type, opponent_acc.uin, group, channel)

    author_sn, plain_to_quote, text_msg_id = send_msg_to_quote_it_later(opponent_acc, chat)

    with allure.step("message/send: Отправка сообщения формально корректному, но на самом деле невалидному юзеру"):
        assert main_acc.quote_message_by_message_send(
            target=chat,
            author_sn=formally_ok_but_invalid_user_sn,
            plain_text=lorem.sentence(),
            plain_to_quote=plain_to_quote,
            msg_id=text_msg_id,
        )

    with allure.step("sendIM: Отправка сообщения формально корректному, но на самом деле невалидному юзеру"):
        assert main_acc.reply_message(
            sn=chat,
            author_sn=formally_ok_but_invalid_user_sn,
            text=lorem.sentence(),
            quote=plain_to_quote,
            msg_id=text_msg_id,
        )
