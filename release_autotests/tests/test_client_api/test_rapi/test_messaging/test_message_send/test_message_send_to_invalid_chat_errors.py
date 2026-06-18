import allure
import lorem
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
)

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX


@allure.id("893736")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка отправки сообщения в чат со слишком длинным именем")
@VKTI
@PRE_VKTI
@TARM
@PRE_TARM
@SANDBOX
def test_text_sending_to_invalid_chat(auth_account):
    """
    Попытка отправки сообщения в чат со слишком длинным именем
    """

    with (
        allure.step("Попытка отправки сообщения в чат со слишком длинным именем"),
        pytest.raises(BadRequestException),
    ):
        auth_account.send_basic_message_by_message_send(
            target="24110345345345@chat.agent",
            plain=lorem.sentence(),
        )
