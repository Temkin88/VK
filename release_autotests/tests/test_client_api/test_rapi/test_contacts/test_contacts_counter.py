import time

import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("86222")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Контакты")
@allure.feature("Управление каунтером чата")
@allure.title("Управление каунтером чата")
@pytest.mark.parametrize("counter", [False, True])
def test_contacts_counter(
    auth_account,
    opponent_account,
    fetch_until_empty_answer,
    event_filter,
    counter,
):
    event_filter.start_point()

    with allure.step("Добавляем в контакты"):
        auth_account.send_basic_message(opponent_account.uin, "pong")

    with allure.step("Проверяем что сообщение отправлено"):
        for _ in range(3):
            fetch_until_empty_answer(opponent_account)
            message_event_text = False

            for event in event_filter(opponent_account.events, "histDlgState"):
                messages = event["eventData"]["tail"]["messages"]
                for message in messages:
                    message_text = message.get("text", "")
                    if message_text == "pong":
                        message_event_text = True
                        break
                if message_event_text:
                    break
            if message_event_text:
                break
            else:
                time.sleep(1)

        assert message_event_text, 'Message text "pong" not found'

    with allure.step("Пробуем отключить mute"):
        opponent_account.rapi_contacts_mute(
            sn=auth_account.uin,
            duration=0,
        )
        opponent_account.fetch()

    with allure.step("Пробуем включить mute"):
        opponent_account.rapi_contacts_mute(
            sn=auth_account.uin,
            duration=1280,
        )

    with allure.step("Пробуем включить counter"):
        opponent_account.rapi_contacts_counter(
            sn=auth_account.uin,
            enable=counter,
        )
        opponent_account.fetch()

    with allure.step("Проверяем появление/не появление поля counterEnabled"):
        event_counterEnabled_disable = False
        fetch_until_empty_answer(opponent_account)

        for _ in range(3):
            for event in event_filter(opponent_account.events[::-1], "diff"):
                data = event["eventData"]
                for events_data in data:
                    for event_temporarily in events_data["data"]:
                        if event_temporarily["name"] == "Temporarily":
                            for user in event_temporarily["buddies"]:
                                if user["aimId"] == auth_account.uin:
                                    assert "mute" in user, "Field mute not found"
                                    if counter:
                                        assert "counterEnabled" not in user, "Field counterEnabled not found"
                                    else:
                                        assert "counterEnabled" in user, "Field counterEnabled not found"

                                    event_counterEnabled_disable = True
                                    break

                    if event_counterEnabled_disable:
                        break
                if event_counterEnabled_disable:
                    break
            if event_counterEnabled_disable:
                break
            else:
                time.sleep(1)

        assert event_counterEnabled_disable, "CounterEnabled event not found"
