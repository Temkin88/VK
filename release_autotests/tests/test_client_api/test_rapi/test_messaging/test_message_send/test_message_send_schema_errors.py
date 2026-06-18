import allure
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
)

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.common import (
    failed_message,
)


@allure.id("515264")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попвтка отправки текстового сообщения с полем pla[1]n вместо plain")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_schema_restrictions_plain(prepare_test_chats_msg):
    """
    Попвтка отправки текстового сообщения с полем pla[1]n вместо plain
    """
    main_acc, opponent, _, _ = prepare_test_chats_msg

    with (
        allure.step("Отправка текстового сообщения с полем pla[1]n вместо plain"),
        pytest.raises(BadRequestException),
    ):
        main_acc.rapi_message_send(
            target=opponent.uin,
            parts={"mainPart": {"text": {"pla1n": failed_message}}},
        )


@allure.id("515266")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попвтка отправки сообщения для одновременного создания задачи и опроса")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_schema_restrictions_task_and_poll(prepare_test_chats_msg):
    """
    Попвтка отправки сообщения для одновременного создания задачи и опроса
    """
    main_acc, opponent, _, _ = prepare_test_chats_msg

    with (
        allure.step("Попытка создания задачи и опроса одновременно"),
        pytest.raises(BadRequestException),
    ):
        main_acc.rapi_message_send(
            target=opponent.uin,
            parts={
                "mainPart": {
                    "text": {"plain": failed_message},
                    "task": {"title": failed_message},
                    "poll": {"type": "anon", "responses": ["1", "2"]},
                }
            },
        )


@allure.id("515265")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Попвтка отправки сообщения с существующей задачей и существующим опросом одновременно")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_schema_restrictions_existing_task_and_existing_poll(prepare_test_chats_msg):
    """
    Попвтка отправки сообщения с существующей задачей и существующим опросом одновременно
    """
    main_acc, opponent, _, _ = prepare_test_chats_msg

    with (
        allure.step("Попытка отправки существующей задачи и существующего опроса одновременно"),
        pytest.raises(BadRequestException),
    ):
        main_acc.rapi_message_send(
            target=opponent.uin,
            parts={
                "mainPart": {
                    "text": {"plain": failed_message},
                    "task": {"taskId": "randomId1"},
                    "poll": {"id": "randomId2"},
                }
            },
        )
