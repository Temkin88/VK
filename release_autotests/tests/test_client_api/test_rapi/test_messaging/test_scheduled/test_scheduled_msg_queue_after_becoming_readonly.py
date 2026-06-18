import time
import allure
from datetime import datetime, timedelta
from support.markers import SANDBOX, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM


@allure.id("148885")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Запланированные сообщения")
@allure.title("Проверка запланированных сообщений после смены роли в группе на readonly")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_schedule_msg_after_becoming_readonly_in_group(
    auth_account,
    one_time_user,
    for_readonly_group,
    fetch_until_empty_answer,
    event_filter,
):
    """
    Проверяем что очередь запланированных сообщений очищается после смены прав пользователя в группе на readonly
    """

    with allure.step("Пытаемся запланировать сообщение"):
        schedule_date = datetime.now() + timedelta(seconds=25)

        response = one_time_user.wim_im_sendIM(
            t=for_readonly_group,
            message=f"Test message for scheduled sending - {one_time_user.getReqId()}",
            schedule={
                "scheduledTime": int(schedule_date.timestamp()),
            },
        )

        scheduled_response = response["response"]["data"]["scheduled"]

    with allure.step("Отнимаем у пользователя право писать в чате"):
        auth_account.rapi_modChatMember(
            sn=for_readonly_group,
            memberSn=one_time_user.uin,
            role="readonly",
        )

        event_filter.start_point()

        time.sleep((schedule_date - datetime.now()).seconds + 5)

        fetch_until_empty_answer(one_time_user)

    with allure.step("Ждем события scheduledUpdate"):
        for event in event_filter(one_time_user.events, "scheduledUpdate"):
            event_data = event["eventData"]

            if (
                event_data["sn"] == for_readonly_group
                and int(scheduled_response["historyVersion"]) < int(event_data["historyVersion"])
                and event_data["queuedMessagesCount"] == 0
            ):
                break
        else:
            raise ValueError("scheduledUpdate event not found")

    with allure.step("Ждем события histDlgState с сообщением о невозможности запланировать сообщение в указанном чате"):
        for event in event_filter(one_time_user.events, "histDlgState"):
            event_data = event["eventData"]

            if event_data["sn"] == for_readonly_group:
                return

        else:
            raise ValueError("histDlgState event not found")


@allure.id("148884")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Запланированные сообщения")
@allure.title("Проверка запланированных сообщений после смены роли в канале на readonly")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_schedule_msg_after_becoming_readonly_in_channel(
    auth_account,
    one_time_user,
    for_readonly_channel,
    fetch_until_empty_answer,
    event_filter,
):
    """
    Проверяем что очередь запланированных сообщений очищается после смены прав пользователя в канале на readonly
    """

    with allure.step("Пытаемся запланировать сообщение"):
        schedule_date = datetime.now() + timedelta(seconds=25)

        response = one_time_user.wim_im_sendIM(
            t=for_readonly_channel,
            message=f"Test message for scheduled sending - {one_time_user.getReqId()}",
            schedule={
                "scheduledTime": int(schedule_date.timestamp()),
            },
        )

        scheduled_response = response["response"]["data"]["scheduled"]

    with allure.step("Отнимаем у пользователя право писать в чате"):
        auth_account.rapi_modChatMember(
            sn=for_readonly_channel,
            memberSn=one_time_user.uin,
            role="readonly",
        )

        event_filter.start_point()

        time.sleep((schedule_date - datetime.now()).seconds + 5)

        fetch_until_empty_answer(one_time_user)

    with allure.step("Ждем события scheduledUpdate"):
        for event in event_filter(one_time_user.events, "scheduledUpdate"):
            event_data = event["eventData"]

            if (
                event_data["sn"] == for_readonly_channel
                and int(scheduled_response["historyVersion"]) < int(event_data["historyVersion"])
                and event_data["queuedMessagesCount"] == 0
            ):
                break
        else:
            raise ValueError("scheduledUpdate event not found")

    with allure.step("Ждем события histDlgState с сообщением о невозможности запланировать сообщение в указанном чате"):
        for event in event_filter(one_time_user.events, "histDlgState"):
            event_data = event["eventData"]

            if event_data["sn"] == for_readonly_channel:
                return

        else:
            raise ValueError("histDlgState event not found")
