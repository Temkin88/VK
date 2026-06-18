import time

import allure

from datetime import datetime, timedelta

from support.markers import SANDBOX, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM


@allure.id("148544")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Запланированные сообщения")
@allure.title("Отмена отправки запланированных сообщений после блокировки пользователя")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_autocancel_scheduled_messages_after_user_blocked(
    auth_account,
    one_time_user,
    stentor,
    fetch_until_empty_answer,
    event_filter,
):
    """
    Проверяем что очередь запланированных сообщений
    очищается после блокировки пользователя и сообщения не отправляются
    """

    scheduled_message_text = f"Test scheduled message for user block [{auth_account.getReqId()}]"

    with allure.step("Пытаемся запланировать сообщение"):
        one_time_user.wim_im_sendIM(
            t=auth_account.uin,
            message=scheduled_message_text,
            schedule={
                "scheduledTime": int((datetime.now() + timedelta(seconds=25)).timestamp()),
            },
        )

    with allure.step("Блокируем пользователя, запланировавшего сообщение"):
        stentor.biz_deleteUser(
            email=one_time_user.uin,
        )

    with allure.step("Ждем наступления запланированного времени отправки"):
        time.sleep(25)

    with allure.step("Проверяем что пользователю не пришли запланированные сообщения заблокированного пользователя"):
        fetch_until_empty_answer(auth_account)

        for event in event_filter(auth_account.events, "histDlgState"):
            event_data = event["eventData"]

            if event_data["sn"] == one_time_user.uin:
                last_messages = event_data.get("tail", {}).get("messages", [])

                assert scheduled_message_text not in [x["text"] for x in last_messages], (
                    "Scheduled message from blocked user was received AFTER user was blocked"
                )

        else:
            return
