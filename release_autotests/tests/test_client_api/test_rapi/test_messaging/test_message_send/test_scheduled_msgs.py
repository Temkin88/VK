from datetime import datetime, timedelta


import allure
import lorem
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    set_draft_and_check_its_really_set,
    correct_message,
    check_draft_is_reset,
)


@pytest.fixture(autouse=True)
def run_before_scheduled_tests(myteam_config):
    is_scheduled_enabled = "scheduled-messages" in myteam_config and myteam_config["scheduled-messages"]["enabled"]
    if not is_scheduled_enabled:
        pytest.skip("Scheduled message sending is disabled")


def get_chat_and_clear_queue(main_acc, chat_type, opponent_sn, group, channel):
    if chat_type == "private":
        chat = opponent_sn
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отчищаем заполненную очередь запланированных перед дальнейшими тестами"):
        response = main_acc.rapi_message_scheduled_cancel(
            sn=chat,
        )
        assert response["status"]["code"] == 20000, "Failed to clear scheduled queue"

    return chat


def clear_queue_after_test(main_acc, chat):
    with allure.step("Отчищаем заполненную очередь запланированных после теста"):
        response = main_acc.rapi_message_scheduled_cancel(
            sn=chat,
        )
        assert response["status"]["code"] == 20000, "Failed to clear scheduled queue"


def send_plain_scheduled_msg(author_acc, chat):
    with allure.step("Отправка текстового запланированного сообщения"):
        existing_scheduled_msg_id = author_acc.send_basic_message_by_message_send(
            target=chat,
            plain=lorem.sentence(),
            schedule={"scheduledTime": int((datetime.now() + timedelta(days=5)).timestamp())},
        )
        assert existing_scheduled_msg_id, f"Failed to send scheduled text msg to chat ID {chat}"

    return existing_scheduled_msg_id


@allure.id("515288")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки текстового запланированного сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_scheduled_send_by_message_send(
    chat_type,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки текстового запланированного сообщения
    """

    """
    #TODO: check what if scheduled messages are disabled in front
    """

    main_acc, opponent, group, channel = prepare_test_chats_msg
    chat = get_chat_and_clear_queue(main_acc, chat_type, opponent.uin, group, channel)

    # Enabling of scheduled messages is managed by compot variable front.message_send.scheduled.enabled
    send_plain_scheduled_msg(main_acc, chat)

    clear_queue_after_test(main_acc, chat)


@allure.id("515305")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Провеяряем, что черновик сброшен после добавления сообщения в очередь запланированных")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_scheduled_send_by_message_send_draft_reset(chat_type, prepare_test_chats_msg, is_draft_enabled):
    """
    Провеяряем, что черновик сброшен после добавления сообщения в очередь запланированных
    """

    if not is_draft_enabled:
        pytest.skip("Drafts are disabled in myteam-config")

    main_acc, opponent, group, channel = prepare_test_chats_msg
    chat = get_chat_and_clear_queue(main_acc, chat_type, opponent.uin, group, channel)

    set_draft_and_check_its_really_set(main_acc, chat)

    # Enabling of scheduled messages is managed by compot variable front.message_send.scheduled.enabled
    with allure.step(
        "Отправка текстового запланированного сообщения, которое до этого было черновиком. "
        "Провеяряем, что черновик после добавления задачи в очередь запланированных сброшен"
    ):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={"mainPart": {"text": {"plain": correct_message}}},
            draftDeleteTime=int(datetime.now().timestamp()),
            schedule={"scheduledTime": int((datetime.now() + timedelta(days=5)).timestamp())},
        )
        assert response["status"]["code"] == 20020, (
            f"Failed to send scheduled text msg with draftDeleteTime to chat ID {chat}"
        )

    check_draft_is_reset(main_acc, chat)

    clear_queue_after_test(main_acc, chat)


@allure.id("515298")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Провеяряем редактирование запланированного сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_scheduled_edit_by_message_send(
    chat_type,
    prepare_test_chats_msg,
):
    """
    Провеяряем редактирование запланированного сообщения
    """

    """
    #TODO: somehow test when planner is down
    """

    main_acc, opponent, group, channel = prepare_test_chats_msg
    chat = get_chat_and_clear_queue(main_acc, chat_type, opponent.uin, group, channel)

    existing_scheduled_msg_id = send_plain_scheduled_msg(main_acc, chat)

    # Enabling of scheduled messages is managed by compot variable front.message_send.scheduled.enabled
    with allure.step("Проверка редактирования запланированного сообщения"):
        new_scheduled_msg_id = main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=lorem.sentence(),
            schedule={
                "scheduledTime": int((datetime.now() + timedelta(days=5)).timestamp()),
                "updateScheduledMsgId": existing_scheduled_msg_id,
            },
        )
        assert new_scheduled_msg_id == existing_scheduled_msg_id, f"Failed to edit scheduled text msg in chat ID {chat}"

    clear_queue_after_test(main_acc, chat)


@allure.id("515293")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки запланированного с опросом")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_scheduled_by_message_send_scheduled_with_poll_creation(
    chat_type,
    prepare_test_chats_msg,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки запланированного с опросом
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg
    chat = get_chat_and_clear_queue(main_acc, chat_type, opponent.uin, group, channel)
    current_time = datetime.now()
    scheduled_time = current_time + timedelta(seconds=60)
    with allure.step("Отправка опроса в запланированном сообщении"):
        main_acc.send_poll_by_message_send(
            poll_title="Да или нет?",
            responses=["Да", "Нет"],
            target=chat,
            schedule={"scheduledTime": int(scheduled_time.timestamp())},
        )

    clear_queue_after_test(main_acc, chat)
