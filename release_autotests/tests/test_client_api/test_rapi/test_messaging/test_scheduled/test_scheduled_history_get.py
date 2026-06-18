import allure

from datetime import datetime, timedelta

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("148535")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Запланированные сообщения")
@allure.title("Получение истории запланированных сообщений")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_rapi_message_scheduled_history_get(
    auth_account,
    prepare_test_chats,
    schedule_message_sending,
):
    """
    Проверяем метод rapi/message/scheduled/history/get
    """

    chat_type, msg_type, chat, schedule_message = schedule_message_sending

    response = schedule_message(
        int((datetime.now() + timedelta(days=1)).timestamp()),
    )

    with allure.step("Пробуем отменить запланированную отправку сообщения"):
        history_response = auth_account.rapi_message_scheduled_history_get(
            sn=chat,
        )

        new_sch_msgs = history_response["results"]["messages"]["new"]

        assert response["scheduledMsgId"] in [x["scheduledMsgId"] for x in new_sch_msgs], (
            "Scheduled msg not found in history"
        )

    with allure.step("Пробуем отменить запланированную отправку сообщения"):
        history_response = auth_account.rapi_message_scheduled_history_get(
            sn=chat,
            history_version=response["historyVersion"],
        )

        assert history_response["status"]["code"] == 20002
        assert history_response["status"]["reason"] == "Already up to date"
