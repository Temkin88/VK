import time

import allure

from datetime import datetime, timedelta

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("148536")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Запланированные сообщения")
@allure.title("Получение события scheduledUpdate после изменения списка запланированных сообщений")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_schedule_update_event(
    auth_account,
    prepare_test_chats,
    schedule_message_sending,
    fetch_until_empty_answer,
    event_filter,
):
    """
    Проверяем что приходит событие scheduledUpdate
    после сохранения запланированного сообщения и после его отправки
    """

    chat_type, msg_type, chat, schedule_message = schedule_message_sending

    response = schedule_message(
        scheduled_time=int((datetime.now() + timedelta(seconds=18)).timestamp()),
        sleep=True,
    )
    assert "queuedMessagesCount" in response, 'Field "queuedMessagesCount" not in response'

    with allure.step("Ждем события об отправке запланированного сообщения"):
        for _ in range(3):
            fetch_until_empty_answer(auth_account)

            for event in event_filter(auth_account.events[::-1], "scheduledUpdate"):
                event_data = event["eventData"]

                if (
                    event_data["sn"] == chat
                    and int(response["historyVersion"]) < int(event_data["historyVersion"])
                    and response["queuedMessagesCount"] > event_data["queuedMessagesCount"]
                ):
                    return
                else:
                    time.sleep(1)
                    break
            else:
                raise ValueError("scheduledUpdate not found")
