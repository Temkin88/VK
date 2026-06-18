from datetime import datetime

import allure
import lorem
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.test_scheduled_msgs import (
    get_chat_and_clear_queue,
    clear_queue_after_test,
)


@pytest.fixture(autouse=True)
def run_before_scheduled_as_instant_tests(myteam_config):
    is_scheduled_enabled = "scheduled-messages" in myteam_config and myteam_config["scheduled-messages"]["enabled"]
    if not is_scheduled_enabled:
        pytest.skip("Scheduled message sending is disabled")


@allure.id("515299")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки текстового запланированного сообщения как мгновенного")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_scheduled_send_by_message_send_as_instant(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Проверка отправки текстового запланированного сообщения как мгновенного
    """

    main_acc, opponent, group, channel = prepare_test_chats_msg
    chat = get_chat_and_clear_queue(main_acc, chat_type, opponent.uin, group, channel)

    # Enabling of scheduled messages is managed by compot variable front.message_send.scheduled.enabled
    with allure.step("Отправка текстового запланированного сообщения как мгновенного"):
        assert main_acc.send_basic_message_by_message_send(
            target=chat, plain=lorem.sentence(), schedule={"scheduledTime": int((datetime.now()).timestamp() + 5)}
        ), f"Failed to send scheduled text msg as instant to chat ID {chat}"

    clear_queue_after_test(main_acc, chat)


@allure.id("515300")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки текстового запланированного сообщения с запланированным времени отправки в прошлом")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_scheduled_send_by_message_send_with_scheduled_time_in_the_past(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Проверка отправки текстового запланированного сообщения с запланированным времени отправки в прошлом
    """

    main_acc, opponent, group, channel = prepare_test_chats_msg
    chat = get_chat_and_clear_queue(main_acc, chat_type, opponent.uin, group, channel)

    # Enabling of scheduled messages is managed by compot variable front.message_send.scheduled.enabled
    with allure.step("Отправка текстового запланированного сообщения с запланированным времени отправки в прошлом"):
        assert main_acc.send_basic_message_by_message_send(
            target=chat, plain=lorem.sentence(), schedule={"scheduledTime": int((datetime.now()).timestamp() - 5)}
        ), f"Failed to send scheduled text msg with scheduledTime in the past to chat ID {chat}"

    clear_queue_after_test(main_acc, chat)
