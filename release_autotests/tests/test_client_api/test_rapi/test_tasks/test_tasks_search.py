import time
from datetime import timedelta, datetime

import allure
import lorem
import pytest

from support.cases.tasks import TASK_LABEL_CASES, TASK_TAGS_CASES, TASK_PRIORITY_CASES, TASK_TITLE_CASES
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("27379")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Задачи")
@allure.feature("Фильтры задач")
@allure.title("Поиск задачи через фильтр")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("task_tags", TASK_TAGS_CASES)
@pytest.mark.parametrize("task_priority", TASK_PRIORITY_CASES)
@pytest.mark.parametrize("task_label", TASK_LABEL_CASES)
def test_search_task_by_filter(
    auth_account,
    opponent_account,
    task_tags,
    task_label,
    task_priority,
):
    with allure.step("Создаем фильтр"):
        filter_id = auth_account.add_task_filter(
            name="Filter",
            assignees=(auth_account.uin,),
            deadline=(datetime.now() + timedelta(days=8)),
        )

    task_title = f"Fitting task {lorem.sentence()}"

    with allure.step("Создаем задачу, подходящую под фильтр"):
        fitting_task_id = auth_account.task_add_by_add(
            title=task_title,
            assignee=auth_account.uin,
            tags=task_tags,
            label=task_label,
            priority=task_priority,
        )

    with allure.step("Создаем задачу, не подходящую под фильтр"):
        not_fitting_task_id = auth_account.task_add_by_add(
            title="Fitting Not task [test_search_task_by_filter]",
            assignee=opponent_account.uin,
        )

    with allure.step("Проверяем фильтр задач"):
        for retry_count in range(1, 6):
            time.sleep(retry_count)

            try:
                result = auth_account.tasks_search(
                    keyword=task_title,
                    filter_id=filter_id,
                    quick_tags=task_tags,
                    quick_labels=[task_label],
                    quick_priorities=[task_priority],
                )

                found_tasks_list = [task["task"]["taskId"] for task in result["results"]["foundTasks"]]

                if not result["results"]["foundTasks"]:
                    time.sleep(retry_count)
                else:
                    with allure.step("Ищем в результатах подходящие задачи"):
                        assert fitting_task_id in found_tasks_list, (
                            f"/api/v{auth_account.api_ver}/rapi/tasks/search:fitting_task_not_found:{fitting_task_id}"
                        )

                    with allure.step("Проверяем что нет не подходящих под фильтр"):
                        assert not_fitting_task_id not in found_tasks_list, (
                            f"/api/v{auth_account.api_ver}/"
                            f"rapi/tasks/search:not_fitting_task_found:"
                            f"{not_fitting_task_id}"
                        )

                    break
            except AssertionError as error:
                auth_account.logger.warning(error)
                if retry_count > 1:
                    raise error

    with allure.step("Удаляем фильтр"):
        auth_account.tasks_filters_delete(
            filter_id=filter_id,
        )


@allure.id("79697")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Задачи")
@allure.feature("Поиск задач")
@allure.title("Поиск задачи")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("task_title", TASK_TITLE_CASES)
@pytest.mark.parametrize("task_priority", TASK_PRIORITY_CASES)
@pytest.mark.parametrize("task_label", TASK_LABEL_CASES)
def test_search_task(
    auth_account,
    opponent_account,
    task_title,
    task_label,
    task_priority,
):
    with allure.step("Создаем задачу"):
        auth_task_id = auth_account.task_add_by_add(
            title=task_title,
            assignee=auth_account.uin,
            label=task_label,
            priority=task_priority,
        )

    for retry_count in range(1, 6):
        time.sleep(retry_count)

        try:
            with allure.step("Пробуем найти задачу"):
                result = auth_account.tasks_search(
                    keyword=task_title,
                    quick_labels=[task_label],
                    quick_priorities=[task_priority],
                )

            auth_found_tasks_list = [task["task"]["taskId"] for task in result["results"]["foundTasks"]]

            if not result["results"]["foundTasks"]:
                time.sleep(retry_count)
            else:
                with allure.step("Ищем в результатах подходящие задачи"):
                    assert auth_task_id in auth_found_tasks_list, f"Task not found: {auth_task_id}"
                break
        except AssertionError as error:
            auth_account.logger.warning(error)
            if retry_count > 1:
                raise error

    with allure.step("Создаем задачу для opponents"):
        title_opponent = f"Opponent {task_title}"
        opponent_task_id = auth_account.task_add_by_add(
            title=title_opponent,
            assignee=opponent_account.uin,
        )
    for retry_count in range(1, 6):
        time.sleep(retry_count)
        try:
            with allure.step("Пробуем найти задачу для opponents"):
                result = opponent_account.tasks_search(
                    keyword=title_opponent,
                )

            opponent_found_tasks_list = [task["task"]["taskId"] for task in result["results"]["foundTasks"]]

            if not result["results"]["foundTasks"]:
                time.sleep(retry_count)
            else:
                with allure.step("Ищем в результатах подходящие задачи для opponents"):
                    assert opponent_task_id in opponent_found_tasks_list, f"Task not found: {opponent_task_id}"
                break
        except AssertionError as error:
            opponent_account.logger.warning(error)
            if retry_count > 1:
                raise error


@allure.id("79754")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Задачи")
@allure.feature("Фильтры задач")
@allure.title("Поиск задачи через быстрые фильтры")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("task_tags", TASK_TAGS_CASES)
@pytest.mark.parametrize("task_priority", TASK_PRIORITY_CASES)
@pytest.mark.parametrize("task_label", TASK_LABEL_CASES)
def test_search_task_by_quick_filter(
    auth_account,
    opponent_account,
    task_tags,
    task_label,
    task_priority,
):
    task_title = f"Fitting task {lorem.sentence()}"

    with allure.step("Создаем задачу, подходящую под быстрый фильтр"):
        fitting_task_id = auth_account.task_add_by_add(
            title=task_title,
            assignee=auth_account.uin,
            tags=task_tags,
            label=task_label,
            priority=task_priority,
        )

    for retry_count in range(1, 6):
        time.sleep(retry_count)
        try:
            with allure.step("Проверяем фильтр задач"):
                result = auth_account.tasks_search(
                    keyword=task_title,
                    quick_tags=task_tags,
                    quick_labels=[task_label],
                    quick_priorities=[task_priority],
                )

            found_tasks_list = [task["task"]["taskId"] for task in result["results"]["foundTasks"]]
            if not found_tasks_list:
                time.sleep(retry_count)
            else:
                with allure.step("Ищем в результатах подходящие задачи"):
                    assert fitting_task_id in found_tasks_list, (
                        f"/api/v{auth_account.api_ver}/rapi/tasks/search:fitting_task_not_found:{fitting_task_id}"
                    )
                break
        except AssertionError as error:
            auth_account.logger.warning(error)
            if retry_count > 1:
                raise error
