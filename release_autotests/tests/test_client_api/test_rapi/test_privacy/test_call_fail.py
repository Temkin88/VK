import json

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@pytest.fixture(scope="module", autouse=True)
def wipe_privacy_settings(auth_account):
    yield

    auth_account.rapi_updatePrivacySettings("calls", "everybody")


@allure.id("30620")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Настройки приватности")
@allure.feature("Изменение настроек приватности")
@allure.title(
    "Ошибка при попытке звонить пользователю с запретом входящих звонков",
)
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_call_fail(
    auth_account,
    opponent_account,
    event_filter,
    fetch_until_empty_answer_with_filter,
):
    """
    Проверяем изменение настроек приватности
    """
    with allure.step("Изменяем настройки приватности"):
        auth_account.rapi_updatePrivacySettings("calls", "nobody")

    with allure.step("Пытаемся позвонить пользователю"):
        event_filter.start_point()

        alloc_data = opponent_account.wim_webrtc_alloc(
            target=auth_account.uin,
        )["response"]["data"]

        opponent_account.wim_voip_webrtcMsg(
            target=auth_account.uin,
            guidSession=alloc_data["guid"],
            stun=alloc_data["stun_addresses"],
            turn=alloc_data.get("relay_tcp_addresses") or alloc_data["relay_udp_addresses"],
        )

    with allure.step("Ищем событие webrtcMsg"):
        for event in filter(
            lambda x: x["eventData"]["guidSession"] == alloc_data["guid"],
            fetch_until_empty_answer_with_filter(opponent_account, "webrtcMsg"),
        ):
            data = event["eventData"]

            if data["subtype"] == "DECLINE":
                signalling_json = json.loads(data["signalling_json"])

                assert signalling_json["reason"] == "blocked_by_callee_privacy"

                return

        pytest.fail("DECLINE webrtcMsg event not found")
