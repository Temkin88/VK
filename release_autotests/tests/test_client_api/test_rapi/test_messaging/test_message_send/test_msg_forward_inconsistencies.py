import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    formally_ok_but_invalid_user_sn,
    prepare_fwd_from_and_fwd_to_sns,
    send_msg_to_forward_it_later,
)


@allure.id("515270")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Пересылка сообщений с указанием авторства невалидных юзеров")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["personal", "group", "channel"])
def test_forwards_from_invalid(chat_type, prepare_public_and_private_test_chats_msg):
    """
    Пересылка сообщений с указанием авторства невалижных юзеров
    """
    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    is_personal_chat, fwd_from, fwd_to = prepare_fwd_from_and_fwd_to_sns(main_acc, opponent_acc, chats, chat_type)

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(
        opponent_acc, chat_type, {"sn": fwd_from, "public": True}
    )

    with allure.step(
        "message/send: Пересылка текстового сообщения формально корректного, но на самом деле невалидного юзера"
    ):
        assert main_acc.forward_message_by_message_send(
            target=fwd_to,
            author_sn=formally_ok_but_invalid_user_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id,
            chat_sn_to_forward_from=None if is_personal_chat else fwd_from,
        )

    with allure.step(
        "sendIM: Пересылка текстового сообщения формально корректного, но на самом деле невалидного юзера"
    ):
        assert main_acc.forward_message(
            sn=fwd_to,
            author_sn=formally_ok_but_invalid_user_sn,
            quote=plain_to_forward,
            msg_id=text_msg_id,
            old_sn=None if is_personal_chat else fwd_from,
        )
