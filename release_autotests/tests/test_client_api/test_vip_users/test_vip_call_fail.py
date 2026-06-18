import json

import allure
import pytest

from support.markers import TARM, PRE_TARM, SANDBOX


@allure.id("33219")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("VIP")
@allure.feature("Действия со стороны обычного пользователя")
@allure.title(
    "Ошибка при попытке звонить пользователю VIP1",
)
@TARM
@PRE_TARM
def test_call_fail_vip1(
    vip_one,
    opponent_account,
    event_filter,
    fetch_until_empty_answer,
):
    with allure.step("Пытаемся позвонить пользователю"):
        event_filter.start_point()

        alloc_data = opponent_account.wim_webrtc_alloc(
            target=vip_one.uin,
        )["response"]["data"]

        opponent_account.wim_voip_webrtcMsg(
            target=vip_one.uin,
            guidSession=alloc_data["guid"],
            stun=alloc_data["stun_addresses"],
            turn=alloc_data.get("relay_tcp_addresses") or alloc_data["relay_udp_addresses"],
        )

    with allure.step("Ищем событие webrtcMsg"):
        fetch_until_empty_answer(opponent_account)

        for event in filter(
            lambda x: x["eventData"]["guidSession"] == alloc_data["guid"],
            event_filter(opponent_account.events, "webrtcMsg"),
        ):
            data = event["eventData"]

            if data["subtype"] == "DECLINE":
                signalling_json = json.loads(data["signalling_json"])

                assert signalling_json["reason"] == "calee_is_vip_and_caller_can_not_disturb_him"

                return

        pytest.fail("DECLINE webrtcMsg event not found")


@allure.id("33221")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("VIP")
@allure.feature("Действия со стороны обычного пользователя")
@allure.title(
    "Возможность звонить пользователю VIP2",
)
@TARM
@PRE_TARM
@SANDBOX
def test_call_fail_vip2(
    vip_two,
    opponent_account,
    event_filter,
    fetch_until_empty_answer,
):
    with allure.step("Пытаемся позвонить пользователю"):
        event_filter.start_point()

        alloc_data = opponent_account.wim_webrtc_alloc(
            target=vip_two.uin,
        )["response"]["data"]

        opponent_account.wim_voip_webrtcMsg(
            target=vip_two.uin,
            guidSession=alloc_data["guid"],
            stun=alloc_data["stun_addresses"],
            turn=alloc_data.get("relay_tcp_addresses") or alloc_data["relay_udp_addresses"],
        )

    with allure.step("Ищем событие webrtcMsg"):
        fetch_until_empty_answer(opponent_account)

        for event in filter(
            lambda x: x["eventData"]["guidSession"] == alloc_data["guid"],
            event_filter(opponent_account.events, "webrtcMsg"),
        ):
            data = event["eventData"]

            if data["subtype"] == "DECLINE":
                raise ValueError
