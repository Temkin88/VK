import random

import allure
import pytest

from support.markers import SANDBOX
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.MAIL)]


@allure.id("79719")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Mail")
@allure.title("Метод /api/v1/mail/newMessages - init")
@SANDBOX
def test_new_message_init(
    auth_account,
    stentor_api_url,
    fetch_until_empty_answer,
    event_filter,
):
    with allure.step("Подписываемся на события почты"):
        auth_account.rapi_eventSubscribe(
            subscriptions=[{"type": "unreadEmailsCount"}],
        )

    with allure.step("Очищаем очередь событий аккаунта"):
        fetch_until_empty_answer(auth_account)
        event_filter.start_point()

    for counter in range(1, 6):
        with allure.step("Обновляем счетчик непрочитанных email"):
            event_filter.start_point()

            auth_account.request(
                method="POST",
                url=f"{stentor_api_url}/api/v1/mail/newMessages",
                json=[
                    {
                        "email": auth_account.uin,
                        "uid": random.randint(0, 100),
                        "counter": counter,
                        "chk": 4,
                        "seq": counter,
                    }
                ],
            )

        with allure.step("Ищем событие unreadEmailsCount"):
            event_found = False
            valid_email_counter = False
            for _ in range(4):
                fetch_until_empty_answer(auth_account)

                for event in event_filter(auth_account.events, "unreadEmailsCount"):
                    event_found = True
                    valid_email_counter = event["eventData"]["counter"] == counter
                    if event_found:
                        break

                if event_found:
                    break

            assert event_found, f"{auth_account.env}:Event unreadEmailsCount not found"
            assert valid_email_counter, f"{auth_account.env}:Received wrong email counter"


@allure.id("28536")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Mail")
@allure.title("Метод /api/v1/mail/newMessages для двух аккаунтов")
@SANDBOX
@pytest.mark.parametrize(
    ("first_range", "second_range"),
    [
        (2, 3),
        (5, 0),
    ],
)
def test_new_message_two_accounts(
    auth_account,
    opponent_account,
    logger,
    stentor_api_url,
    fetch_until_empty_answer,
    event_filter,
    first_range,
    second_range,
):
    with allure.step("Подписываемся на события почты"):
        auth_account.rapi_eventSubscribe(
            subscriptions=[{"type": "unreadEmailsCount"}],
        )

        opponent_account.rapi_eventSubscribe(
            subscriptions=[{"type": "unreadEmailsCount"}],
        )

    with allure.step("Очищаем очередь событий аккаунта"):
        fetch_until_empty_answer(auth_account)
        fetch_until_empty_answer(opponent_account)
        event_filter.start_point()

    for first_counter, second_counter in zip(range(1, first_range), range(4, second_range, -1), strict=False):
        with allure.step("Обновляем счетчик непрочитанных email"):
            event_filter.start_point()

            auth_account.request(
                method="POST",
                url=f"{stentor_api_url}/api/v1/mail/newMessages",
                json=[
                    {
                        "email": auth_account.uin,
                        "uid": random.randint(0, 100),
                        "counter": first_counter,
                        "chk": 4,
                        "seq": first_counter,
                    },
                    {
                        "email": opponent_account.uin,
                        "uid": random.randint(0, 100),
                        "counter": second_counter,
                        "chk": 4,
                        "seq": first_counter,
                    },
                ],
            )

        with allure.step("Ищем событие unreadEmailsCount"):
            for account, counter in (
                (auth_account, first_counter),
                (opponent_account, second_counter),
            ):
                fetch_until_empty_answer(account)

                event_found = False

                for event in event_filter(account.events, "unreadEmailsCount"):
                    event_found = event["eventData"]["counter"] == counter
                    if event_found:
                        break

                assert event_found, f"{auth_account.env}:Received wrong email counter"


@allure.id("28537")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Mail")
@allure.title("Метод /api/v1/mail/newMessages - desc seq")
@SANDBOX
def test_new_message_desc_seq(
    auth_account,
    stentor_api_url,
    fetch_until_empty_answer,
    event_filter,
):
    with allure.step("Подписываемся на события почты"):
        auth_account.rapi_eventSubscribe(
            subscriptions=[{"type": "unreadEmailsCount"}],
        )

    with allure.step("Очищаем очередь событий аккаунта"):
        fetch_until_empty_answer(auth_account)
        event_filter.start_point()

    for counter in range(202, 200, -1):
        with allure.step("Обновляем счетчик непрочитанных email"):
            auth_account.request(
                method="POST",
                url=f"{stentor_api_url}/api/v1/mail/newMessages",
                json=[
                    {
                        "email": auth_account.uin,
                        "uid": random.randint(0, 100),
                        "counter": counter,
                        "chk": 4,
                        "seq": counter,
                    }
                ],
            )

    with allure.step("Ищем событие unreadEmailsCount"):
        fetch_until_empty_answer(auth_account)

        event_found = False
        event_not_found = False

        for event in event_filter(auth_account.events, "unreadEmailsCount"):
            if event["eventData"]["counter"] == 202:
                event_found = True
            if event["eventData"]["counter"] == 201:
                event_not_found = True

        assert event_found and not event_not_found, f"{auth_account.env}:Received wrong email counter"  # noqa: PT018
