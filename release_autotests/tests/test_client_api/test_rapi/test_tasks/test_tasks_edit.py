import datetime

import allure
import pytest

from support.cases.tasks import TASK_TITLE_CASES, TASK_TAGS_CASES, TASK_STATUS_CASES
from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26930")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Задачи")
@allure.feature("Создание задачи")
@allure.title("Редактирование задачи в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
@pytest.mark.parametrize("task_status", TASK_STATUS_CASES)
@pytest.mark.parametrize("task_title", TASK_TITLE_CASES)
@pytest.mark.parametrize("task_tags", TASK_TAGS_CASES)
def test_edit_task_status(
    chat_type,
    task_status,
    task_title,
    task_tags,
    prepare_test_chats,
):
    """
    Проверяем создание и редактирование задачи
    """
    main_acc, opponent, group, channel = prepare_test_chats

    if chat_type == "private":
        chat = main_acc.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем тестовую задачу и подписываемся на нее"):
        task_id = main_acc.task_add_by_add(
            title=chat,
            assignee=main_acc.uin,
        )

    with allure.step("Пытаемся отредактировать задачу"):
        main_acc.tasks_edit(
            taskId=task_id,
            title=task_title,
            assignee=opponent.uin,
            status=task_status,
            endTime=int(datetime.datetime.now().timestamp()) + 3600,
            priority="critical",
            label="red",
            tags=task_tags,
        )
