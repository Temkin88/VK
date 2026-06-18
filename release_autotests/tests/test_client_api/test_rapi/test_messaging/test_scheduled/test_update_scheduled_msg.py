import allure

from datetime import datetime, timedelta

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("255606")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Запланированные сообщения")
@allure.title("Редактирование запланированного сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_update_scheduled_msg(
    auth_account,
    prepare_test_chats,
    schedule_message_sending,
):
    """
    Проверяем редактирование запланированного сообщения
    """

    chat_type, msg_type, chat, schedule_message = schedule_message_sending

    schedule_response = schedule_message(
        int((datetime.now() + timedelta(days=1)).timestamp()),
    )

    with allure.step("Пробуем изменить запланированную отправку сообщения"):
        update_response = schedule_message(
            int((datetime.now() + timedelta(days=2)).timestamp()),
            update_scheduled_msg_id=schedule_response["scheduledMsgId"],
        )

    assert schedule_response["scheduledMsgId"] == update_response["scheduledMsgId"], (
        "Planned new msg instead of updating old msg"
    )
