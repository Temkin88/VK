from datetime import datetime, timedelta
import time

import allure
import lorem
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
    ScheduledTimeIsTooFarInFutureException,
    ScheduledMessagesLimitReachedException,
)

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    failed_message,
)
from tests.test_client_api.test_rapi.test_messaging.test_message_send.test_scheduled_msgs import (
    get_chat_and_clear_queue,
    clear_queue_after_test,
)


@pytest.fixture(autouse=True)
def run_before_scheduled_errors_tests(myteam_config):
    is_scheduled_enabled = "scheduled-messages" in myteam_config and myteam_config["scheduled-messages"]["enabled"]
    if not is_scheduled_enabled:
        pytest.skip("Scheduled message sending is disabled")


@allure.id("515297")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title(
    "Проверка отправки текстового запланированного сообщения "
    "с запланированным времени отправки слишком далеко в будущем"
)
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_scheduled_by_message_send_time_too_far_in_the_future(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Проверка отправки текстового запланированного сообщения
    с запланированным времени отправки слишком далеко в будущем
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg
    chat = get_chat_and_clear_queue(main_acc, chat_type, opponent.uin, group, channel)

    with (
        allure.step(
            "Попытка отправки текстового запланированного сообщения "
            "с запланированным времени отправки слишком далеко в будущем"
        ),
        pytest.raises(ScheduledTimeIsTooFarInFutureException),
    ):
        main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=lorem.sentence(),
            schedule={"scheduledTime": int((datetime.now() + timedelta(days=368)).timestamp())},
        )

    clear_queue_after_test(main_acc, chat)


@allure.id("515312")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки запланированного сообщения выше лимита (100) очереди запланированных сообщений")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private"])
def test_scheduled_by_message_send_scheduled_queue_limit(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Проверка отправки запланированного сообщения выше лимита (100) очереди запланированных сообщений
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg
    chat = get_chat_and_clear_queue(main_acc, chat_type, opponent.uin, group, channel)

    with allure.step("Полностью заполняем очередь запланированных до лимита (100) числа сообщений в очереди"):
        scheduled_msgs_queue_size = 0

        schedule = {"scheduledTime": int((datetime.now() + timedelta(days=1)).timestamp())}
        while scheduled_msgs_queue_size < 100:
            plain = f"{lorem.sentence()} {int(datetime.now().timestamp())}"

            response = main_acc.rapi_message_send(
                target=chat,
                parts={"mainPart": {"text": {"plain": plain}}},
                schedule=schedule,
            )
            status_code = response["status"]["code"]
            is_msg_scheduled = status_code == 20020
            if not is_msg_scheduled:
                continue

            if scheduled_msgs_queue_size == 0:
                assert response["results"]["scheduled"]["queuedMessagesCount"] == 1, "Scheduled queue was NOT empty"
            if scheduled_msgs_queue_size != 99:
                time.sleep(0.1)
            scheduled_msgs_queue_size += 1

    with (
        allure.step("Попытка отправки запланированного сообщения выше лимита (100) очереди запланированных сообщений"),
        pytest.raises(ScheduledMessagesLimitReachedException),
    ):
        status_code = 0
        while status_code != 20020:
            response = main_acc.rapi_message_send(
                target=chat,
                parts={"mainPart": {"text": {"plain": f"{failed_message} {int(datetime.now().timestamp())}"}}},
                schedule=schedule,
            )
            status_code = response["status"]["code"]

    clear_queue_after_test(main_acc, chat)


@allure.id("515294")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки запланированного с созданием задачи")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_scheduled_by_message_send_scheduled_with_task_creation(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Проверка отправки запланированного с созданием задачи
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg
    chat = get_chat_and_clear_queue(main_acc, chat_type, opponent.uin, group, channel)

    with (
        allure.step("Попытка создания задачи в запланированном сообщении"),
        pytest.raises(BadRequestException),
    ):
        main_acc.task_add_by_message_send(
            target=chat, schedule={"scheduledTime": int((datetime.now() + timedelta(days=5)).timestamp())}
        )

    clear_queue_after_test(main_acc, chat)
