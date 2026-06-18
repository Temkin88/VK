import time
from datetime import datetime

import allure

from support.markers import SANDBOX


@allure.id("250329")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Biz")
@allure.title("Методы /api/v1/biz/getUserLastSeen")
@SANDBOX
def test_get_user_lastseen_online(
    auth_account,
    opponent_account,
    stentor,
    fetch_until_empty_answer_with_filter,
):
    with allure.step(f"Подписываемся на userState пользователя {stentor}"):
        auth_account.rapi_eventSubscribe(
            subscriptions=[
                {
                    "type": "userState",
                    "data": {
                        "contacts": [opponent_account.uin, auth_account.uin],
                    },
                }
            ],
        )

    with allure.step("Отправляем сообщение сами себе"):
        (
            opponent_account.wim_im_sendIM(
                t=auth_account.uin,
                message="text",
            ),
            f"Failed to send basic msg to chat ID {auth_account.uin}",
        )
    with allure.step("Проверяем что в событии userState приходит правильный lastseen"):
        opponent_event_lastseen_zero = False
        for event in fetch_until_empty_answer_with_filter(auth_account, "userState"):
            data = event["eventData"]

            if data["userState"]["lastseen"] == 0 and opponent_account.uin == data["sn"]:
                before_opponent_event = data["userState"]["lastseen"]
                opponent_event_lastseen_zero = True
                break

        assert opponent_event_lastseen_zero, "Lastseen not equal 0"

    with allure.step("Пытаемся получить lastseen пользователя"):
        response = stentor.biz_getUserLastSeen(
            email=opponent_account.uin,
        )

        last_seen_time_stamp = response["results"]["lastSeenTimeStamp"]

    with allure.step("Проверяем, что lastSeen  == 0"):
        assert last_seen_time_stamp == before_opponent_event
        assert last_seen_time_stamp == 0, f"{auth_account.env}:Wrong user lastSeenTimeStamp"

    time.sleep(120)

    with allure.step("Проверяем что в событии userState приходит правильный lastseen"):
        opponent_event_lastseen_not_zero = False
        for event in fetch_until_empty_answer_with_filter(auth_account, "userState")[::-1]:
            data = event["eventData"]

            if data["userState"]["lastseen"] > 0 and opponent_account.uin == data["sn"]:
                after_opponent_event = data["userState"]["lastseen"]
                opponent_event_lastseen_not_zero = True
                break

        assert opponent_event_lastseen_not_zero, "Lastseen equal 0"

    with allure.step("Пытаемся получить lastseen пользователя"):
        response = stentor.biz_getUserLastSeen(
            email=opponent_account.uin,
        )

        last_seen_time_stamp = response["results"]["lastSeenTimeStamp"]

    with allure.step("Проверяем, что lastSeen  > 0"):
        assert last_seen_time_stamp == after_opponent_event != before_opponent_event
        assert last_seen_time_stamp > 0, f"{auth_account.env}:Wrong user lastSeenTimeStamp"


@allure.id("250330")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Biz")
@allure.title("Методы /api/v1/biz/getUserLastSeen")
@SANDBOX
def test_get_user_lastseen_fetch_online(auth_account, stentor, fetch_until_empty_answer):
    with allure.step("Отправляем сообщение сами себе"):
        fetch_until_empty_answer(auth_account)

    with allure.step("Пытаемся получить lastseen пользователя"):
        response = stentor.biz_getUserLastSeen(
            email=auth_account.uin,
        )

        last_seen_time_stamp = response["results"]["lastSeenTimeStamp"]

    with allure.step("Проверяем, что lastSeen  == 0"):
        assert last_seen_time_stamp == 0, f"{auth_account.env}:Wrong user lastSeenTimeStamp"

        time.sleep(120)

    with allure.step("Пытаемся получить lastseen пользователя"):
        response = stentor.biz_getUserLastSeen(
            email=auth_account.uin,
        )

        last_seen_time_stamp = response["results"]["lastSeenTimeStamp"]

    with allure.step("Проверяем, что lastSeen  == 0"):
        assert last_seen_time_stamp > 0, f"{auth_account.env}:Wrong user lastSeenTimeStamp"


@allure.id("28535")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Biz")
@allure.title("Методы /api/v1/biz/getUserLastSeen")
@SANDBOX
def test_get_user_lastseen(auth_account, stentor):
    before_request = int(datetime.now().timestamp())

    with allure.step("Пытаемся получить lastseen пользователя"):
        auth_account.fetch(timeout=200)

        response = stentor.biz_getUserLastSeen(
            email=auth_account.uin,
        )

        last_seen_time_stamp = response["results"]["lastSeenTimeStamp"]

        assert last_seen_time_stamp == 0 or before_request <= last_seen_time_stamp, (
            f"{auth_account.env}:Wrong user lastSeenTimeStamp"
        )
