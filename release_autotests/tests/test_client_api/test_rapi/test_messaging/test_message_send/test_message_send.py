import hashlib
import os
import string
from datetime import datetime

import allure
import lorem
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    correct_message_with_mentions,
    check_mentions_in_fetch_events,
    set_draft_and_check_its_really_set,
    correct_message,
    check_draft_is_reset,
)


@allure.id("515249")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки текстового сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_text_sending_basic_message(
    chat_type,
    bot_class,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки текстового сообщения
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "bot":
        chat = bot_class.uin
    elif chat_type == "channel":
        chat = channel

    with allure.step("Отправка текстового сообщения"):
        send_msg_id = main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=lorem.sentence(),
        )

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    account = opponent
    if chat_type == "bot":
        account = main_acc
    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        assert check_events_list_contains_event_with_msgId(account, send_msg_id), "Sended message not found in events"


@allure.id("515253")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка редактирования текстового сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_text_sending_edit_message(chat_type, bot_class, prepare_test_chats_msg):
    """
    Проверка редактирования текстового сообщения
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "bot":
        chat = bot_class.uin
    else:
        chat = channel

    with allure.step("Отправка сообщения, чтобы потом отредактировать его"):
        msg_id = main_acc.send_basic_message_by_message_send(
            target=chat,
            plain="Test msg for edit",
        )
        assert msg_id, f"Failed to send msg to edit it to chat ID {chat}"

    with allure.step(f"Редактируем сообщение ID {msg_id}"):
        response = main_acc.rapi_message_send(
            target=chat,
            updateMsgId=msg_id,
            parts={"mainPart": {"text": {"plain": "Test"}}},
        )
        assert msg_id == response["results"]["msgId"], f"Got unexpected msg_id[{msg_id}]"
        assert "updatePatchVersion" in response["results"], f"No updatePatchVersion in msg id[{msg_id}]"


@allure.id("515260")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки текстового сообщения с 2 меншенами")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_text_sending_with_two_mentions(chat_type, bot_class, prepare_test_chats_msg, third_account):
    """
    Проверка отправки текстового сообщения с 2 меншенами
    """
    main_acc, opponent_acc, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent_acc.uin
        receive_mention_from_chat = main_acc.uin
        msg_receiver_acc = opponent_acc
    elif chat_type == "group":
        chat = group
        receive_mention_from_chat = chat
        msg_receiver_acc = opponent_acc
    elif chat_type == "bot":
        chat = bot_class.uin
        receive_mention_from_chat = bot_class.uin
        msg_receiver_acc = main_acc
        """
        Посылаем сообщение в бот с меншенами, самого бота не меншеним =>
            ивента с меншеном в чате с ним быть не должно, но histDlgState нужно проверить
        """
    else:
        chat = channel
        receive_mention_from_chat = chat
        msg_receiver_acc = opponent_acc

    with allure.step("Отправка сообщения с двумя меншенами"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={
                "mainPart": {"text": {"plain": correct_message_with_mentions([opponent_acc.uin, third_account.uin])}}
            },
        )
        mentions_msg_id = response["results"]["msgId"]
        assert mentions_msg_id

    check_mentions_in_fetch_events(
        mentions_msg_id,
        receive_mention_from_chat,
        msg_receiver_acc,
        [opponent_acc.uin, third_account.uin],
        check_mention_me_event=chat_type != "bot",
    )


@allure.id("515261")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки текстового сообщения, которое должно сбросить черновик")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_text_sending_and_draft_reset(chat_type, bot_class, prepare_test_chats_msg, is_draft_enabled):
    """
    Проверка отправки текстового сообщения, которое должно сбросить черновик
    """

    if not is_draft_enabled:
        pytest.skip("Drafts are disabled in myteam-config")

    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "bot":
        chat = bot_class.uin
    else:
        chat = channel

    set_draft_and_check_its_really_set(main_acc, chat)

    # Enabling of draft reset after success message send is managed
    #   by compot variable front.message_send.draft_delete_time_enabled
    with allure.step("Отправка текстового сообщения, которое должно сбросить черновик"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={"mainPart": {"text": {"plain": correct_message}}},
            draftDeleteTime=int(datetime.now().timestamp()),
        )
        assert response["status"]["code"] == 20000, f"Failed to reset draft in chat ID {chat}"

    check_draft_is_reset(main_acc, chat)


@allure.step("Проверяем reqId во входящих событиях о сообщении")
def check_reqId_in_fetch_events(msg_id, chat, auth_account, req_id: string):
    auth_account.events = []
    for i in range(1, 6):
        auth_account.fetch(timeout=i * 100)

    # the race is possible during this check:
    # it's possible that there won't be any event for the message,
    # so we check reqId only in case of event existence for chosen msgId
    for event in filter(
        lambda x: x["type"] == "histDlgState" and x["eventData"].get("sn") == chat,
        auth_account.events[::-1],
    ):
        for cur_part in ("eventData", "tail", "intro"):
            event_data_to_check = event["eventData"]
            if cur_part != "eventData" and cur_part in event_data_to_check:
                event_data_to_check = event_data_to_check[cur_part]
            for message in event_data_to_check.get("messages", []):
                if message["msgId"] == msg_id:
                    if "reqId" not in message or message["reqId"] != req_id:
                        pytest.fail("failed to find reqId in histDlgState for msg_id ", msg_id)
                    # if nothing was raised before this line then the check is passed
                    return


@allure.id("520850")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка замены reqId на localMsgId для предовращения дублирования на клиентах")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_reqId_replacing_with_localMsgId(chat_type, bot_class, prepare_test_chats_msg, third_account):
    """
    Проверка замены reqId на localMsgId для предовращения дублирования на клиентах

    При получении поля localMsgId сервером оно будет использовано вместо reqId для текущего запроса.
    Необходимо для предотвращения дублирования сообщений на некоторых клиентах.
    LocalMsgId- это сгенерированный на клиенте временный идентификатор сообщения,
        используемый локально на клиенте до момента получения msgId от сервера.
    Серверный msgId может быть получен из тела ответа message/send,
        а также из некоторых ивентов, приходящих в теле ответа fetchEvents.
    При получении ивентов histDlgState/imState поле reqId/sendReqId соответственно будет совпадать с localMsgId,
        что позволит избежать дублирования сообщений.
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "bot":
        chat = bot_class.uin
    else:
        chat = channel

    localMsgId = str(hashlib.sha1(os.urandom(256)).hexdigest())[:15]

    with allure.step("Отправка сообщения с localMsgId для замены reqId, чтобы предовратить дублирование на клиентах"):
        response = main_acc.rapi_message_send(
            target=chat,
            localMsgId=localMsgId,
            parts={"mainPart": {"text": {"plain": correct_message}}},
        )
        msg_id = response["results"]["msgId"]
        assert msg_id

    check_reqId_in_fetch_events(msg_id, chat, main_acc, localMsgId)
