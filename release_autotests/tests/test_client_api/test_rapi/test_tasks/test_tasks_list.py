import allure
import pytest

from support.markers import SANDBOX, SAAS, VKTI, PRE_VKTI, TARM, PRE_TARM, SLA, PRE_SAAS


def func_chunks_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


@allure.id("27380")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Задачи")
@allure.feature("Список задач")
@allure.label("layer", "api_layer")
@allure.title("Проход по курсору списка задач")
@pytest.mark.parametrize(
    "task_filter_name",
    [
        "Все",
        "На меня",
        "От меня",
        "Задачи себе",
        "Закрытые",
        "Сегодня",
        "Текущая неделя",
        "Текущий месяц",
    ],
    ids=[
        "all",
        "on_me",
        "from_me",
        "task_for_myself",
        "closed",
        "for_today",
        "current_week",
        "current_month",
    ],
)
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
def test_tasks_list_cursor_and_read(
    auth_account,
    task_filter_name,
):
    tasks_list_to_read = []
    tasks_list_to_close = []

    with allure.step("Итерируем список задач по курсору"):
        for task in auth_account.iter_task_list(
            filter_name=task_filter_name,
            page_size=50,
        ):
            if not task["isRead"]:
                tasks_list_to_read.append(task["taskId"])
            if task["status"] != "closed" and "closed" in task["allowedStatuses"]:
                tasks_list_to_close.append(task["taskId"])

            break

        for task_pool in func_chunks_generators(tasks_list_to_read, 5):
            auth_account.tasks_setRead(
                tasks=task_pool,
            )
        for task in tasks_list_to_close:
            auth_account.tasks_edit(
                taskId=task,
                status="closed",
            )
