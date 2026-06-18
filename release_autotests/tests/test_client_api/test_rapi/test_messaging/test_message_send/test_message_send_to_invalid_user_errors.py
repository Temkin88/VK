import allure
import lorem
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
    BadTargetException,
)

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    obviously_invalid_user_sn,
    formally_ok_but_invalid_user_sn,
)


@allure.id("515263")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка отправки текстового сообщения очевидно невалижному юзеру")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_text_sending_to_obviously_invalid_user(bot_class, prepare_test_chats_msg):
    """
    Попытка отправки текстового сообщения очевидно невалижному юзеру
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    with (
        allure.step("Попытка отправки текстового сообщения очевидно невалидному юзеру"),
        pytest.raises(BadTargetException),
    ):
        main_acc.send_basic_message_by_message_send(
            target=obviously_invalid_user_sn,
            plain=lorem.sentence(),
        )


@allure.id("515262")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попытка отправки сообщения формально корректному, но на самом деле невалидному юзеру")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_text_sending_to_invalid_user(bot_class, prepare_test_chats_msg):
    """
    Попытка отправки сообщения формально корректному, но на самом деле невалидному юзеру
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    with (
        allure.step("Попытка отправки сообщения формально корректному, но на самом деле невалидному юзеру"),
        pytest.raises(BadRequestException),
    ):
        main_acc.send_basic_message_by_message_send(
            target=formally_ok_but_invalid_user_sn,
            plain=lorem.sentence(),
        )
