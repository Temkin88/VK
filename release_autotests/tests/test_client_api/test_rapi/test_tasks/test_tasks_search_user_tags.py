from datetime import datetime

import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("30153")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Задачи")
@allure.feature("Теги задач")
@allure.title("Поиск по тегам задач")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_search_user_tags(
    auth_account,
):
    timestamp = str(datetime.now().timestamp())

    tags = [
        f"tag_1-{timestamp}",
        f"tag_2-{timestamp}",
    ]

    with allure.step("Создаем задачу"):
        auth_account.task_add_by_add(
            title="task_title",
            assignee=auth_account.uin,
            tags=tags,
        )

    with allure.step("Ищем теги задач"):
        auth_account.tasks_searchUserTags(
            keyword="tag_",
        )
