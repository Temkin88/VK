import datetime

import allure
import pytest

from support.cases.tasks import TASK_STATUS_CASES
from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("27377")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Задачи")
@allure.feature("Фильтры задач")
@allure.label("layer", "api_layer")
@allure.title("Удаление фильтра задач")
@pytest.mark.parametrize(
    "task_assignees",
    [
        None,
        # "self",
        # "opponent",
        "both",
    ],
)
@pytest.mark.parametrize(
    ("is_subscribed", "withChanges"),
    [
        (False, False),
        (True, True),
    ],
)
@pytest.mark.parametrize(
    "deadline",
    [
        "expired",
        # "today",
        # "tomorrow",
        # "thisWeek",
        # "nextWeek",
        "month",
        datetime.datetime.now() + datetime.timedelta(hours=5),
    ],
)
@pytest.mark.parametrize("task_status", TASK_STATUS_CASES)
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_add_n_delete_tasks_filter(
    auth_account,
    opponent_account,
    task_assignees,
    task_status,
    is_subscribed,
    withChanges,
    deadline,
):
    if task_assignees is None:
        task_assignees = ()
    elif task_assignees == "self":
        task_assignees = (auth_account.uin,)
    elif task_assignees == "opponent":
        task_assignees = (opponent_account.uin,)
    elif task_assignees == "both":
        task_assignees = (opponent_account.uin, auth_account.uin)
    else:
        raise ValueError

    with allure.step("Создаем фильтр задач"):
        filter_name = f"Test {datetime.datetime.now().date()}"

        filter_id = auth_account.add_task_filter(
            name=filter_name,
            assignees=task_assignees,
            statuses=(task_status,),
            subscribed=is_subscribed,
            withChanges=withChanges,
            deadline=deadline,
        )

    with allure.step("Пробуем удалить фильтр"):
        auth_account.tasks_filters_delete(
            filter_id=filter_id,
        )
