from datetime import datetime

import allure
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
    MessageIsTooBigException,
    InvalidAimsidException,
)

from support.cases.invalid_formatted_msgs_parts import invalid_formatted_msgs_parts

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    failed_message,
    set_draft_and_check_its_really_set,
    check_draft_is_kept,
    msg_too_long_len,
)


@allure.id("515257")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка отправки слишком длинного текстового сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_text_sending_with_too_long_message(chat_type, bot_class, prepare_test_chats_msg):
    """
    Попытка отправки слишком длинного текстового сообщения
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

    # Size limit of message is managed by compot variable front.message_send.max_message_length
    with (
        allure.step("Попытка отправки слишком длинного текстового сообщения"),
        pytest.raises(MessageIsTooBigException),
    ):
        main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=failed_message + msg_too_long_len * "a",
        )


@allure.id("515258")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка редактирования сообщения невалидным сообщением")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_text_sending_edit_message_with_invalid_msg(chat_type, bot_class, prepare_test_chats_msg):
    """
    Попытка редактирования сообщения невалидным сообщением
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

    with (
        allure.step(f"Попытка отредактировать сообщение ID {msg_id} некорректным сообщением"),
        pytest.raises(BadRequestException),
    ):
        main_acc.rapi_message_send(
            target=chat,
            update_msg_id=msg_id,
            parts=invalid_formatted_msgs_parts[0],
        )


@allure.id("515259")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка отправки сообщения с невалидным aimsid")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_text_sending_with_invalid_aimsid(chat_type, bot_class, prepare_test_chats_msg):
    """
    Попытка отправки сообщения с невалидным aimsid
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

    with (
        allure.step("Попытка отправки сообщения с невалидным aimsid"),
        pytest.raises(InvalidAimsidException),
    ):
        target = chat
        invalid_aimsid = f"1 {main_acc.aimsid}"

        main_acc.send_basic_message_by_message_send(target=target, plain=failed_message, aimsid=invalid_aimsid)


@allure.id("515267")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка отправки текстового сообщения, которое НЕ должно сбросить черновик")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "bot"])
def test_draft_keeping_after_sending_message_with_invalid_msg(
    chat_type, bot_class, prepare_test_chats_msg, is_draft_enabled
):
    """
    Попытка отправки текстового сообщения, которое НЕ должно сбросить черновик
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

    with (
        allure.step("Попытка отправки текстового сообщения, которое НЕ должно сбросить черновик"),
        pytest.raises(BadRequestException),
    ):
        main_acc.rapi_message_send(
            target=chat,
            parts=invalid_formatted_msgs_parts[0],
            draft_delete_time=int(datetime.now().timestamp()),
        )

    check_draft_is_kept(main_acc, chat)
