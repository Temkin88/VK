import time

import allure
import pytest

from pyvkteamsclient.client.exceptions import RequestException

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("30136")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Опросы")
@allure.feature("Действия с опросами")
@allure.title("Подписка на опрос")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_poll_subscribe(
    chat_type,
    prepare_test_chats,
    fetch_until_empty_answer_with_filter,
    event_filter,
):
    """
    Проверяем отправку опроса
    """
    main_acc, opponent, group, channel = prepare_test_chats

    for i in range(1, 3):
        try:
            response = main_acc.send_poll(
                chat_id=group if chat_type == "group" else channel,
                poll_title="test poll",
                poll_type="anon",
                responses=[f"variant_{i}" for i in range(1, 11)],
            )
            poll_id = response["response"]["data"]["pollId"]
            break
        except KeyError:
            time.sleep(i)
    else:
        raise RequestException("Failed to create poll")

    with allure.step("Подписываемся на опрос"):
        opponent.rapi_poll_subscribe(poll_id)

    with allure.step("Голосуем"):
        event_filter.start_point()

        main_acc.rapi_poll_vote(
            _id=poll_id,
            answerId="1",
        )

    with allure.step("Ищем события опроса"):
        event_found = False

        for _ in range(3):
            for event in fetch_until_empty_answer_with_filter(opponent, "pollUpdate"):
                data = event["eventData"]
                if data["id"] == poll_id and not data["closed"] and not data["canStop"]:
                    event_found = True
                    break
            if event_found:
                break
            else:
                time.sleep(1)

        assert event_found, "pollUpdate event found"
