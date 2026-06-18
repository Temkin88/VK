import datetime

import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("30154")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Задачи")
@allure.feature("Просмотр треда задачи")
@allure.title("Отметить задачу прочитанности")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_task_set_read(
    auth_account,
    opponent_account,
):
    task_title = f"test_task_set_read-{datetime.datetime.now().timestamp()}"

    with allure.step("Создаем задачу"):
        task_id = auth_account.task_add_by_add(
            title=task_title,
            assignee=opponent_account.uin,
        )

    with allure.step("Отмечаем задачу как прочитанную"):
        opponent_account.tasks_setRead(
            tasks=[
                task_id,
            ],
        )
