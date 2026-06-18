import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("28162")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Поддержка")
@allure.feature("Отправка report/abuse")
@allure.title("Отправка report/abuse на сообщение")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "chat_type",
    [
        "group",
        "channel",
    ],
)
@pytest.mark.parametrize(
    "reason",
    [
        "porno",
        "violation",
        "spam",
        "other",
    ],
)
def test_send_report_abuse_on_message(
    prepare_test_chats,
    reason,
    chat_type,
):
    auth_account, opponent_account, group, channel = prepare_test_chats

    with allure.step("Отправляем сообщение спама"):
        msg_id = opponent_account.send_basic_message(
            sn=group if chat_type == "group" else channel,
            text=reason,
        )

    with allure.step("Отправляем тестовый отчет"):
        auth_account.rapi_reportAbuse(
            reason=reason,
            context_json={
                "context": "message",
                "sn": opponent_account.uin,
                "msgId": msg_id,
                "chatSn": group if chat_type == "group" else channel,
            },
        )
