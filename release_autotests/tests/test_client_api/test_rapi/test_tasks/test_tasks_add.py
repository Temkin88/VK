import datetime

import allure
import pytest

from support.cases.tasks import (
    TASK_LABEL_CASES,
    TASK_TITLE_CASES,
    TASK_DURATION_CASES,
    TASK_ASSIGNEE_CASES,
    TASK_TAGS_CASES,
    TASK_PRIORITY_CASES,
)
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26927")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Задачи")
@allure.feature("Создание задачи")
@allure.title("Создание задачи через /tasks/add")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("task_title", TASK_TITLE_CASES)
@pytest.mark.parametrize("task_duration", TASK_DURATION_CASES)
@pytest.mark.parametrize("task_assignee", TASK_ASSIGNEE_CASES)
@pytest.mark.parametrize("task_tags", TASK_TAGS_CASES)
@pytest.mark.parametrize("task_priority", TASK_PRIORITY_CASES)
@pytest.mark.parametrize("task_label", TASK_LABEL_CASES)
def test_task_add(
    task_title,
    task_assignee,
    task_duration,
    task_tags,
    task_label,
    task_priority,
    opponent_account,
    auth_account,
):
    """
    Создание задачи
    """

    if task_assignee == "me":
        task_assignee = auth_account.uin
    elif task_assignee == "opponent":
        task_assignee = opponent_account.uin
    else:
        task_assignee = None

    with allure.step("Отправляем запрос"):
        auth_account.task_add_by_add(
            title=task_title,
            assignee=task_assignee,
            endTime=int(datetime.datetime.now().timestamp()) + task_duration,
            tags=task_tags,
            label=task_label,
            priority=task_priority,
        )
