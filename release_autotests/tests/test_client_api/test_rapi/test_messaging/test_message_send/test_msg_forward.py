import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    correct_message_with_mentions,
    check_mentions_in_fetch_events,
    correct_message,
    prepare_fwd_from_and_fwd_to_sns,
    send_msg_to_forward_it_later,
    check_forwarded_from_info_in_fetch_events,
)


@allure.id("515268")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка пересылки обычного текстового сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["personal", "group", "channel"])
def test_basic_forward(chat_type, prepare_public_and_private_test_chats_msg, third_account):
    """
    Проверка пересылки обычного текстового сообщения
    """
    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    is_personal_chat, fwd_from, fwd_to = prepare_fwd_from_and_fwd_to_sns(opponent_acc, third_account, chats, chat_type)

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(
        opponent_acc, chat_type, {"sn": fwd_from, "public": True}
    )

    with allure.step("Пересылка текстового сообщения"):
        msg_id_wo_mentions = main_acc.forward_message_by_message_send(
            target=fwd_to,
            author_sn=author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id,
            chat_sn_to_forward_from=None if is_personal_chat else fwd_from,
        )

    check_mentions_in_fetch_events(msg_id_wo_mentions, fwd_to, main_acc, [])


@allure.id("515269")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка пересылки текстового сообщения с 2 меншенами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["personal", "group", "channel"])
def test_forward_with_mentions(chat_type, prepare_public_and_private_test_chats_msg, third_account):
    """
    Проверка пересылки текстового сообщения с 2 меншенами
    """
    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    is_personal_chat, fwd_from, fwd_to = prepare_fwd_from_and_fwd_to_sns(opponent_acc, third_account, chats, chat_type)

    with allure.step("Отправка текстового сообщения с меншенами для последующей пересылки"):
        plain_to_forward_with_mentions = correct_message_with_mentions([opponent_acc.uin, third_account.uin])
        author_sn = opponent_acc.uin
        text_msg_id = opponent_acc.send_basic_message_by_message_send(
            target=fwd_from,
            plain=plain_to_forward_with_mentions,
        )
        assert text_msg_id, f"Failed to send basic msg to chat ID {fwd_from}"

    with allure.step("Пересылка текстового сообщения с меншенами"):
        mentions_msg_id = main_acc.forward_message_by_message_send(
            target=fwd_to,
            author_sn=author_sn,
            plain_to_forward=plain_to_forward_with_mentions,
            msg_id=text_msg_id,
            chat_sn_to_forward_from=None if is_personal_chat else fwd_from,
        )
        assert mentions_msg_id, f"Failed to forward basic msg with mentions to chat ID {fwd_to}"

    """
    В случае пересылки сообщения с меншеном бек не шлет ивент mentionMeMessage,
        но меншн рисуется за счет поля unreadMentionMeCount в histDlgState
    В случае личных сообщений пересылаем сообшение от main_acc в third_account
        и проверяем на third_account, что сообщение ему пришло с меншеном
    Во всех остальных случаях сообщение отправляется в группы, где состоит opponent_acc
    """
    receive_mention_from_chat = main_acc.uin if is_personal_chat else fwd_to
    msg_receiver_acc = third_account if is_personal_chat else opponent_acc
    check_mentions_in_fetch_events(
        mentions_msg_id,
        receive_mention_from_chat,
        msg_receiver_acc,
        [opponent_acc.uin, third_account.uin],
        check_mention_me_event=False,
        unread_mention_me_count=1,
    )


@allure.id("515272")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка пересылки текстового сообщения с дополнительным созданием задачи")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["personal", "group", "channel"])
def test_forward_with_task_creation(chat_type, prepare_public_and_private_test_chats_msg, third_account):
    """
    Проверка пересылки текстового сообщения с дополнительным созданием задачи
    """
    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    is_personal_chat, fwd_from, fwd_to = prepare_fwd_from_and_fwd_to_sns(opponent_acc, third_account, chats, chat_type)

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(
        opponent_acc, chat_type, {"sn": fwd_from, "public": True}
    )

    with allure.step("Пересылка текстового сообщения с дополнительным созданием задачи"):
        task_msg_id = main_acc.forward_message_by_message_send(
            target=fwd_to,
            author_sn=author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id,
            main_part={"task": {"title": correct_message}},
            chat_sn_to_forward_from=None if is_personal_chat else fwd_from,
        )
        assert task_msg_id, f"Failed to forward msg with additional task creation to chat ID {fwd_to}"

    with allure.step("Проверка пересылки текстового сообщения с дополнительным созданием задачи"):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=third_account if is_personal_chat else opponent_acc,
            check_chat=main_acc.uin if is_personal_chat else fwd_to,
            msg_id=task_msg_id,
            author_sn=author_sn,
            need_to_check_chat_info=False,
        )


@allure.id("515271")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка пересылки текстового сообщения с дополнительным созданием опроса")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["personal", "group", "channel"])
def test_forward_with_poll_creation(chat_type, prepare_public_and_private_test_chats_msg, third_account):
    """
    Проверка пересылки текстового сообщения с дополнительным созданием опроса
    """
    main_acc, opponent_acc, chats = prepare_public_and_private_test_chats_msg
    is_personal_chat, fwd_from, fwd_to = prepare_fwd_from_and_fwd_to_sns(opponent_acc, third_account, chats, chat_type)

    author_sn, plain_to_forward, text_msg_id = send_msg_to_forward_it_later(
        opponent_acc, chat_type, {"sn": fwd_from, "public": True}
    )

    with allure.step("Пересылка текстового сообщения с дополнительным созданием опроса"):
        poll_msg_id = main_acc.forward_message_by_message_send(
            target=fwd_to,
            author_sn=author_sn,
            plain_to_forward=plain_to_forward,
            msg_id=text_msg_id,
            main_part={"text": {"plain": "Yes or no?"}, "poll": {"type": "anon", "responses": ["Yes", "No"]}},
            chat_sn_to_forward_from=None if is_personal_chat else fwd_from,
        )
        assert poll_msg_id, f"Failed to forward msg with additional poll creation to chat ID {fwd_to}"

    with allure.step("Проверка пересылки текстового сообщения с дополнительным созданием опроса"):
        check_forwarded_from_info_in_fetch_events(
            account_to_fetch=third_account if is_personal_chat else opponent_acc,
            check_chat=main_acc.uin if is_personal_chat else fwd_to,
            msg_id=poll_msg_id,
            author_sn=author_sn,
            need_to_check_chat_info=False,
        )
