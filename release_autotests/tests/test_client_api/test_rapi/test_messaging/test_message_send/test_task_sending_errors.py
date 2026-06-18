from datetime import datetime

import allure
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
    TaskCreationErrorException,
    SendImStateException,
)

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_messaging.test_message_send.test_task_sending import add_title_only_task


@allure.id("515311")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Отправка задачи cо времени окончания в прошлом")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_task_with_end_time_in_past(
    opponent_account,
    auth_account,
):
    """
    Отправка задачи cо времени окончания в прошлом
    """
    target = opponent_account.uin

    with (
        allure.step("Пытаемся создать задачу cо временем окончания в прошлом"),
        pytest.raises(TaskCreationErrorException),
    ):
        add_title_only_task(auth_account=auth_account, target=target, end_time=int(datetime.now().timestamp() - 10))

    with (
        allure.step(
            "Показываем консистентность message/send и sendIM"
            " при попытке создания задачи cо временем окончания в прошлом"
        ),
        pytest.raises(SendImStateException) as ex,
    ):
        auth_account.wim_im_sendIM(
            t=target,
            parts=[
                {
                    "mediaType": "text",
                    "text": "test",
                    "task": {
                        "title": "test",
                        "endTime": int(datetime.now().timestamp() - 10),
                    },
                },
            ],
        )
        st_code = ex.value.response_status_code
        assert st_code == 400, f"Unexpected statusCode from sendIM: {st_code}"
        st_text = ex.value.response_status_text
        assert "statusDetailCode 20" in st_text, f"Unexpected statusDetailCode from sendIM: {st_text}"
        assert 'state: "failed"' in st_text, f"Unexpected msg state from sendIM: {st_text}"


@allure.id("515313")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Отправка существующей задачи без подписи")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_existing_task_sending_wo_title(
    opponent_account,
    auth_account,
):
    """
    Отправка существующей задачи без подписи
    """
    target = opponent_account.uin

    with allure.step("Создаем задачу только с заголовком"):
        _, existing_task_id = add_title_only_task(auth_account, target=target)
        assert existing_task_id, f"Failed to create task with title only in chat ID {target}"

    with (
        allure.step("Отправка существующей задачи без подписи"),
        pytest.raises(BadRequestException),
    ):
        auth_account.send_existing_task_by_message_send(target=target, existing_task_id=existing_task_id)
