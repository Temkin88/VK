from typing import Union

import allure
from jsondiff import diff

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


def default_notification(seconds: int, enabled: bool = True) -> dict[str, Union[int, bool]]:
    return {"duration": seconds, "enabled": enabled}


@allure.id("30157")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Задачи")
@allure.feature("Уведомления о задаче")
@allure.title("Обновление настроек базовых уведомлений о задаче")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_default_update(
    auth_account,
):
    default_list = [
        default_notification(3600),
        default_notification(86400),
        default_notification(604800),
    ]

    with allure.step("Создаем задачу"):
        task_id = auth_account.task_add_by_add(
            title="task_title",
            assignee=auth_account.uin,
        )

    with allure.step("Обновляем базовые уведомления о задаче"):
        auth_account.tasks_notifications_default_update(
            task_id=task_id,
            defaultNotifications=default_list,
        )

    with allure.step("Получаем список настроенных уведомлений"):
        results = auth_account.tasks_notifications_list(
            task_id=task_id,
        )["results"]

    with allure.step("Проверяем кастомные уведомления"):
        assert not results["customNotifications"], "Found customNotifications just after task creation"

    with allure.step("Проверяем базовые уведомления"):
        assert results["defaultNotifications"], "Not found customNotifications just after task creation"

        notifications = results["defaultNotifications"]
        result = diff(default_list, notifications)

        assert not result, f"Not found default notifications with duration: {result}"
