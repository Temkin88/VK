from datetime import datetime, timedelta
from typing import Optional

import allure
import pytest
from pyvkteamsclient.client.exceptions import (
    BadRequestException,
)

from support.cases.tasks import (
    TASK_TITLE_CASES,
    TASK_ASSIGNEE_CASES,
    TASK_TAGS_CASES,
    TASK_PRIORITY_CASES,
    TASK_LABEL_CASES,
)
from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS


def add_title_only_task(
    auth_account,
    target: str,
    end_time: Optional[int] = None,
    label: Optional[str] = None,
):
    return auth_account.task_add_by_message_send(
        target=target,
        title="Only task title",
        end_time=end_time,
        label=label,
    )


def get_task_assignee(task_assignee_type, auth_account, opponent_account):
    if task_assignee_type == "me":
        task_assignee = auth_account.uin
    elif task_assignee_type == "opponent":
        task_assignee = opponent_account.uin
    else:
        task_assignee = ""
    return task_assignee


@allure.id("515307")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка функционала создания задач")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("task_title", TASK_TITLE_CASES)
@pytest.mark.parametrize("task_assignee_type", TASK_ASSIGNEE_CASES)
@pytest.mark.parametrize("task_tags", TASK_TAGS_CASES)
@pytest.mark.parametrize("task_priority", TASK_PRIORITY_CASES)
@pytest.mark.parametrize("task_label", TASK_LABEL_CASES)
def test_task_creation(
    task_title,
    task_assignee_type,
    task_tags,
    task_label,
    task_priority,
    opponent_account,
    auth_account,
):
    """
    Проверка функционала создания задач
    """

    task_assignee = get_task_assignee(task_assignee_type, auth_account, opponent_account)

    target = opponent_account.uin

    def add_task():
        return auth_account.task_add_by_message_send(
            title=task_title,
            target=target,
            assignee=task_assignee,
            end_time=int((datetime.now() + timedelta(days=5)).timestamp()),
            priority=task_priority,
            label=task_label,
            tags=task_tags,
        )

    if not task_tags:
        with allure.step("Отправляем задачу с пустым массивом tags"), pytest.raises(BadRequestException):
            add_task()
    else:
        with allure.step("Отправляем задачу"):
            assert add_task(), f"Failed to create task in chat ID {target}"


@allure.id("515309")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Отправка задачи только с заголовком")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_task_creation_only_with_title(
    opponent_account,
    auth_account,
):
    """
    Отправка задачи только с заголовком
    """
    target = opponent_account.uin

    with allure.step("Создаем задачу только с заголовком"):
        _, existing_task_id = add_title_only_task(auth_account, target=target)
        assert existing_task_id, f"Failed to create task with title only in chat ID {target}"


@allure.id("515308")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Отправка задачи с серым флагом")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_task_creation_with_grey_label(
    opponent_account,
    auth_account,
):
    """
    Отправка задачи с серым флагом
    """
    target = opponent_account.uin

    with allure.step("Создаем задачу с cерым флагом"):
        assert add_title_only_task(auth_account=auth_account, target=target, label="grey"), (
            f"Failed to create task with with grey label in chat ID {target}"
        )


@allure.id("515310")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Отправка существующей задачи")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_existing_task_sending(
    opponent_account,
    auth_account,
):
    """
    Отправка существующей задачи
    """
    target = opponent_account.uin
    with allure.step("Создаем задачу только с заголовком"):
        _, existing_task_id = add_title_only_task(auth_account, target=target)
        assert existing_task_id, f"Failed to create task with title only in chat ID {target}"

    with allure.step("Отправка существующей задачи с подписью"):
        assert auth_account.send_existing_task_by_message_send(
            target=target, existing_task_id=existing_task_id, text="Существующая задача"
        ), f"Failed to send existing poll to chat ID {target}"
