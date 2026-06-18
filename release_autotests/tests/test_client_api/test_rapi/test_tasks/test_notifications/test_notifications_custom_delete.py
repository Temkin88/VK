from datetime import datetime, timedelta

import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("30155")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Задачи")
@allure.feature("Уведомления о задаче")
@allure.title("Удаление кастомных уведомлений о задаче")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_custom_delete(
    auth_account,
):
    custom_notfication_timestamp = int((datetime.now() + timedelta(days=1)).timestamp())

    with allure.step("Создаем задачу"):
        task_id = auth_account.task_add_by_add(
            title="task_title",
            assignee=auth_account.uin,
        )

    with allure.step("Добавляем кастомное уведомление о задаче"):
        auth_account.tasks_notifications_custom_add(
            task_id=task_id,
            timestamp=custom_notfication_timestamp,
        )

    with allure.step("Удаляем кастомное уведомление о задаче"):
        auth_account.tasks_notifications_custom_delete(
            task_id=task_id,
            timestamp=custom_notfication_timestamp,
        )

    with allure.step("Получаем список настроенных уведомлений"):
        results = auth_account.tasks_notifications_list(
            task_id=task_id,
        )["results"]

    with allure.step("Проверяем кастомные уведомления"):
        assert not results["customNotifications"], "Found customNotifications just after task creation"

    with allure.step("Проверяем базовые уведомления"):
        assert results["defaultNotifications"], "Not found customNotifications just after task creation"
