import allure

from datetime import datetime, timedelta

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("148533")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Запланированные сообщения")
@allure.title("Принудительная отправка запланированных сообщений сейчас")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_rapi_message_scheduled_flush(
    auth_account,
    prepare_test_chats,
    schedule_message_sending,
):
    """
    Проверяем метод rapi/message/scheduled/flush
    """

    chat_type, msg_type, chat, schedule_message = schedule_message_sending

    response = schedule_message(
        int((datetime.now() + timedelta(days=1)).timestamp()),
    )

    with allure.step("Пробуем отменить запланированную отправку сообщения"):
        auth_account.rapi_message_scheduled_flush(
            sn=chat,
            scheduled_msg_ids=[response["scheduledMsgId"]],
        )
