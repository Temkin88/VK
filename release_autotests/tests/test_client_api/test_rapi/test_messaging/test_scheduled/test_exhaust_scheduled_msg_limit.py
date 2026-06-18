import allure
import pytest

from datetime import datetime, timedelta

from pyvkteamsclient.client import RequestException
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("148534")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Запланированные сообщения")
@allure.title("Ограничение количества запланированных сообщений в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_exhaust_scheduled_msg_limit(
    auth_account,
    prepare_test_chats,
    schedule_message_sending,
):
    """
    Проверяем что количество запланированных сообщений в рамках одного чата ограниченно (100 шт.)
    """

    chat_type, msg_type, chat, schedule_message = schedule_message_sending

    scheduled_msg_ids = []

    with pytest.raises(RequestException):
        for _ in range(102):
            response = schedule_message(
                int((datetime.now() + timedelta(days=1)).timestamp()),
            )

            scheduled_msg_ids.append(response["scheduledMsgId"])

    auth_account.rapi_message_scheduled_cancel(
        sn=chat,
    )
