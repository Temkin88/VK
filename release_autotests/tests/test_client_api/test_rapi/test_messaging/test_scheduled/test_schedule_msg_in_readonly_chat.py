import time

import allure

from datetime import datetime, timedelta

from support.markers import SANDBOX, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM


@allure.id("148773")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Запланированные сообщения")
@allure.title("Попытка запланировать сообщение в группе где пользователь имеет права readonly")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_schedule_msg_in_readonly_group(
    one_time_user,
    readonly_group,
    fetch_until_empty_answer,
    event_filter,
):
    """
    Проверяем невозможность запланировать отправку сообщений в группу с правами readonly
    """

    with allure.step("Пытаемся запланировать сообщение"):
        schedule_date = datetime.now() + timedelta(seconds=25)

        response = one_time_user.wim_im_sendIM(
            t=readonly_group,
            message=f"Test message for scheduled sending - {one_time_user.getReqId()}",
            schedule={
                "scheduledTime": int(schedule_date.timestamp()),
            },
        )

        response = response["response"]["data"]["scheduled"]

        event_filter.start_point()

        time.sleep((schedule_date - datetime.now()).seconds + 5)

        fetch_until_empty_answer(one_time_user)

    with allure.step("Ждем события scheduledUpdate"):
        for event in event_filter(one_time_user.events, "scheduledUpdate"):
            event_data = event["eventData"]

            if (
                event_data["sn"] == readonly_group
                and int(response["historyVersion"]) < int(event_data["historyVersion"])
                and event_data["queuedMessagesCount"] == 0
            ):
                break
        else:
            raise ValueError("scheduledUpdate event not found")

    with allure.step("Ждем события histDlgState с сообщением о невозможности запланировать сообщение в указанном чате"):
        for event in event_filter(one_time_user.events, "histDlgState"):
            event_data = event["eventData"]

            if event_data["sn"] == readonly_group:
                return

        else:
            raise ValueError("histDlgState event not found")


@allure.id("148772")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Запланированные сообщения")
@allure.title("Попытка запланировать сообщение в канале где пользователь имеет права readonly")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_schedule_msg_in_readonly_channel(
    one_time_user,
    readonly_channel,
    fetch_until_empty_answer,
    event_filter,
):
    """
    Проверяем невозможность запланировать отправку сообщений в канал с правами readonly
    """

    with allure.step("Пытаемся запланировать сообщение"):
        schedule_date = datetime.now() + timedelta(seconds=25)

        response = one_time_user.wim_im_sendIM(
            t=readonly_channel,
            message=f"Test message for scheduled sending - {one_time_user.getReqId()}",
            schedule={
                "scheduledTime": int(schedule_date.timestamp()),
            },
        )

        response = response["response"]["data"]["scheduled"]

        event_filter.start_point()

        time.sleep((schedule_date - datetime.now()).seconds + 5)

        fetch_until_empty_answer(one_time_user)

    with allure.step("Ждем события scheduledUpdate"):
        for event in event_filter(one_time_user.events, "scheduledUpdate"):
            event_data = event["eventData"]

            if (
                event_data["sn"] == readonly_channel
                and int(response["historyVersion"]) < int(event_data["historyVersion"])
                and event_data["queuedMessagesCount"] == 0
            ):
                break
        else:
            raise ValueError("scheduledUpdate event not found")

    with allure.step("Ждем события histDlgState с сообщением о невозможности запланировать сообщение в указанном чате"):
        for event in event_filter(one_time_user.events, "histDlgState"):
            event_data = event["eventData"]

            if event_data["sn"] == readonly_channel:
                return

        else:
            raise ValueError("histDlgState event not found")
