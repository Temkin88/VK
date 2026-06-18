from datetime import datetime, timedelta

import allure
import lorem
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
    ScheduledTimeIsTooFarInFutureException,
)

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS

from tests.test_client_api.test_rapi.test_messaging.test_message_send.test_scheduled_msgs import (
    get_chat_and_clear_queue,
    clear_queue_after_test,
    send_plain_scheduled_msg,
)


@pytest.fixture(autouse=True)
def run_before_scheduled_updates_errors_tests(myteam_config):
    is_scheduled_enabled = "scheduled-messages" in myteam_config and myteam_config["scheduled-messages"]["enabled"]
    if not is_scheduled_enabled:
        pytest.skip("Scheduled message sending is disabled")


@allure.id("515296")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка отредактировать существующее сообщениее с помощью редактирвоания запланированного сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_scheduled_by_message_send_edit_instant_message_with_scheduled(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Попытка отредактировать существующее сообщениее с помощью редактирвоания запланированного сообщения
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg
    chat = get_chat_and_clear_queue(main_acc, chat_type, opponent.uin, group, channel)

    # Enabling of scheduled messages is managed by compot variable front.message_send.scheduled.enabled
    existing_scheduled_msg_id = send_plain_scheduled_msg(main_acc, chat)

    with (
        allure.step(
            "Попытка отредактировать существующее сообщениее с помощью редактирвоания запланированного сообщения"
        ),
        pytest.raises(BadRequestException),
    ):
        main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=lorem.sentence(),
            schedule={
                "scheduledTime": int((datetime.now() + timedelta(days=5)).timestamp()),
                "updateScheduledMsgId": existing_scheduled_msg_id,
            },
            update_msg_id=12345,
        )

    clear_queue_after_test(main_acc, chat)


@allure.id("515306")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка редактирвоания запланированного сообщения с updateScheduledMsgId==0")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_scheduled_by_message_send_edit_with_update_scheduled_msgid_eq_zero(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Попытка редактирвоания запланированного сообщения с updateScheduledMsgId==0
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg
    chat = get_chat_and_clear_queue(main_acc, chat_type, opponent.uin, group, channel)

    with (
        allure.step("Попытка редактирвоания запланированного сообщения с updateScheduledMsgId==0"),
        pytest.raises(BadRequestException),
    ):
        main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=lorem.sentence(),
            schedule={
                "scheduledTime": int((datetime.now() + timedelta(days=5)).timestamp()),
                "updateScheduledMsgId": 0,
            },
        )

    clear_queue_after_test(main_acc, chat)


@allure.id("515304")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка редактирвоания запланированного сообщения с запланированным временем слишком далеко в будущем")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_scheduled_by_message_send_edit_with_time_too_far_in_the_future(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Попытка редактирвоания запланированного сообщения с запланированным временем слишком далеко в будущем
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg
    chat = get_chat_and_clear_queue(main_acc, chat_type, opponent.uin, group, channel)

    existing_scheduled_msg_id = send_plain_scheduled_msg(main_acc, chat)

    with (
        allure.step(
            "Попытка редактирвоания запланированного сообщения с запланированным временем слишком далеко в будущем"
        ),
        pytest.raises(ScheduledTimeIsTooFarInFutureException),
    ):
        main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=lorem.sentence(),
            schedule={
                "scheduledTime": int((datetime.now() + timedelta(days=368)).timestamp()),
                "updateScheduledMsgId": existing_scheduled_msg_id,
            },
        )

    clear_queue_after_test(main_acc, chat)
