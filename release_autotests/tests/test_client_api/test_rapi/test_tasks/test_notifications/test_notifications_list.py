from typing import Union

import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


def default_notification(seconds: int, enabled: bool = True) -> dict[str, Union[int, bool]]:
    return {"duration": seconds, "enabled": enabled}


@allure.id("30158")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Задачи")
@allure.feature("Уведомления о задаче")
@allure.title("Список настроенных уведомлений о задаче")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_notifications_list(
    auth_account,
):
    with allure.step("Создаем задачу"):
        task_id = auth_account.task_add_by_add(
            title="task_title",
            assignee=auth_account.uin,
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

        for duration in (3600, 86400):
            assert default_notification(duration) in notifications, (
                f"Not found default notifications with duration: {duration}"
            )

        assert default_notification(604800, False) in notifications, (
            f"Not found default notifications with duration: {duration}"
        )
