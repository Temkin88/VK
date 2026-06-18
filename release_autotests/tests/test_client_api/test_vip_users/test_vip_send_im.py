import time

import allure

from support.markers import TARM, PRE_TARM, SANDBOX


@allure.id("33217")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("VIP")
@allure.feature("Действия со стороны обычного пользователя")
@allure.title("Отправка сообщения пользователю VIP1")
@TARM
@PRE_TARM
def test_send_msg_to_vip1(
    auth_account,
    vip_one,
    event_filter,
    fetch_until_empty_answer,
):
    with allure.step("Отправляем сообщение пользователю VIP1"):
        auth_account.send_basic_message(
            sn=vip_one.uin,
            text="Test message to VIP1",
        )

    with allure.step(
        "Проверяем наличие на исходящей стороне события communicationRestricted",
    ):
        event_found = False

        for _ in range(3):
            fetch_until_empty_answer(auth_account)

            for event in event_filter(auth_account.events, "histDlgState"):
                tail = event["eventData"]["tail"]["messages"]

                for msg in tail:
                    if "class" in msg and msg["class"] == "event" and msg["event"]["type"] == "communicationRestricted":
                        event_found = True
                        break

                if event_found:
                    break
            if event_found:
                break
            else:
                time.sleep(1)

        assert event_found, "communicationRestricted msg not found"


@allure.id("33218")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("VIP")
@allure.feature("Действия со стороны обычного пользователя")
@allure.title("Отправка сообщения пользователю VIP2")
@TARM
@PRE_TARM
@SANDBOX
def test_send_msg_to_vip2(
    auth_account,
    vip_two,
    event_filter,
    fetch_until_empty_answer,
):
    with allure.step("Отправляем сообщение пользователю VIP1"):
        auth_account.send_basic_message(
            sn=vip_two.uin,
            text="Test message to VIP1",
        )

    with allure.step(
        "Проверяем наличие на исходящей стороне события communicationRestricted",
    ):
        event_found = False

        for _ in range(3):
            fetch_until_empty_answer(auth_account)

            for event in event_filter(auth_account.events, "histDlgState"):
                tail = event["eventData"]["tail"]["messages"]

                for msg in tail:
                    if "class" in msg and msg["class"] == "event" and msg["event"]["type"] == "communicationRestricted":
                        event_found = True
                        break

                if event_found:
                    break
            if event_found:
                break
            else:
                time.sleep(1)

        assert not event_found, "communicationRestricted msg found"


@allure.id("33216")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("VIP")
@allure.feature("Действия со стороны обычного пользователя")
@allure.title("Отправка сообщения пользователю VIP1 от VIP2")
@TARM
@PRE_TARM
@SANDBOX
def test_send_msg_from_vip2_to_vip1(
    vip_one,
    vip_two,
    event_filter,
    fetch_until_empty_answer,
):
    with allure.step("Отправляем сообщение пользователю VIP1"):
        vip_two.send_basic_message(
            sn=vip_one.uin,
            text="Test message to VIP1",
        )

    with allure.step(
        "Проверяем наличие на исходящей стороне события communicationRestricted",
    ):
        event_found = False

        for i in range(3):
            time.sleep(i)

            fetch_until_empty_answer(vip_two)

            for event in event_filter(vip_two.events, "histDlgState"):
                tail = event["eventData"]["tail"]["messages"]

                for msg in tail:
                    if "class" in msg and msg["class"] == "event" and msg["event"]["type"] == "communicationRestricted":
                        event_found = True
                        break

                if event_found:
                    break
            if event_found:
                break
            else:
                time.sleep(1)

        assert not event_found, "communicationRestricted msg found"


@allure.id("33214")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("VIP")
@allure.feature("Действия со стороны обычного пользователя")
@allure.title("Отправка сообщения пользователю VIP2 от VIP1")
@TARM
@PRE_TARM
@SANDBOX
def test_send_msg_from_vip1_to_vip2(
    vip_one,
    vip_two,
    event_filter,
    fetch_until_empty_answer,
):
    with allure.step("Отправляем сообщение пользователю VIP1"):
        vip_one.send_basic_message(
            sn=vip_two.uin,
            text="Test message to VIP1",
        )

    with allure.step(
        "Проверяем наличие на исходящей стороне события communicationRestricted",
    ):
        event_found = False

        for i in range(3):
            time.sleep(i)

            fetch_until_empty_answer(vip_one)

            for event in event_filter(vip_one.events, "histDlgState"):
                tail = event["eventData"]["tail"]["messages"]

                for msg in tail:
                    if "class" in msg and msg["class"] == "event" and msg["event"]["type"] == "communicationRestricted":
                        event_found = True
                        break

                if event_found:
                    break
            if event_found:
                break
            else:
                time.sleep(1)

        assert not event_found, "communicationRestricted msg found"
