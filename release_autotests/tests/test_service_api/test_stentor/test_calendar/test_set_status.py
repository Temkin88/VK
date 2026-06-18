from datetime import datetime, timedelta

import allure
import pytest

from support.markers import SANDBOX
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CALENDAR)]


@allure.id("79716")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Calendar")
@allure.title("Метод /api/v1/calendar/setAutoStatus")
@SANDBOX
@pytest.mark.parametrize(
    "user",
    [
        "self",
        "not_self",
    ],
)
def test_set_autostatus_success(
    auth_account,
    opponent_account,
    stentor,
    event_filter,
    fetch_until_empty_answer,
    user,
):
    event_filter.start_point()

    account = auth_account if user == "self" else opponent_account

    startTs = int(datetime.now().timestamp())
    endTs = int((datetime.now() + timedelta(seconds=10)).timestamp())

    fetch_until_empty_answer(account)

    with allure.step("Подписываемся на обновления статуса"):
        account.rapi_eventSubscribe(
            subscriptions=[
                {
                    "type": "status",
                    "data": {
                        "contacts": [auth_account.uin],
                    },
                }
            ],
        )

    with allure.step("Отправяем запрос на автостатус"):
        stentor.calendar_setAutoStatus(
            email=auth_account.uin,
            startTS=startTs,
            endTS=endTs,
        )

    with allure.step("Ищем событие автостатуса"):
        event_found = False

        for _ in range(4):
            fetch_until_empty_answer(account)

            for event in event_filter(account.events, "status"):
                data = event["eventData"]
                event_found = (
                    data.get("startTime") == startTs and data.get("endTime") == endTs and data["sn"] == auth_account.uin
                )
                if event_found:
                    break

            if event_found:
                break
        assert event_found, "Auto_Status_event_not_found"


@allure.id("28534")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Calendar")
@allure.title("Метод /api/v1/calendar/setAutoStatus - ошибки")
@SANDBOX
@pytest.mark.parametrize("user", [True, False])
def test_set_autostatus_errors(
    auth_account,
    stentor,
    user,
):
    with allure.step("Отправяем запрос на автостатус"), pytest.raises(Exception):
        stentor.calendar_setAutoStatus(
            email=auth_account.uin if user else None,
            startTS=int((datetime.now() - timedelta(days=5)).timestamp()),
            endTS=int((datetime.now() - timedelta(days=4)).timestamp()),
        )
