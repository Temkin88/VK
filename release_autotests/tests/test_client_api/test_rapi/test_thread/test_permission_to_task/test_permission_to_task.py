import datetime
import time

import allure
import pytest

from pyvkteamsclient.client.exceptions import AccessDeniedException, BadRequestException
from support.cases.tasks import TASK_TITLE_CASES, TASK_DURATION_CASES
from support.markers import SANDBOX, SAAS, VKTI, PRE_VKTI, TARM, PRE_TARM, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.MESSAGING)]


@pytest.fixture(scope="session", autouse=True)
def skip_test(ignore_task_restrictions):
    if ignore_task_restrictions:
        pytest.skip("Skipping tests for task thread restrictions")


@allure.id("66310")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Задачи")
@allure.feature("Доступность задач только участникам")
@allure.title("Создание задачи, доступ в обсуждение только участникам")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("task_title", TASK_TITLE_CASES)
@pytest.mark.parametrize("task_duration", TASK_DURATION_CASES)
def test_permission_to_thread_subs(
    task_title,
    task_duration,
    auth_account,
    opponent_account,
    third_account,
    event_filter,
    fetch_until_empty_answer_with_filter,
    ENV_PLATFORM,
):
    """
    Создание задачи
    """
    if ENV_PLATFORM == "TARM":
        pytest.skip("Отключается до устранения проблем по баге https://jira.vk.team/browse/IMSERVER-19077")

    task_assignee = opponent_account.uin

    with allure.step("Создаем задачу"):
        task_id = auth_account.task_add_by_add(
            title=task_title,
            assignee=task_assignee,
            endTime=int(datetime.datetime.now().timestamp()) + task_duration,
        )

    with allure.step("Ищем событие о создании задачи"):
        event_found_thread_id = False

        for _ in range(3):
            with allure.step(f"Попытка #{_}"):
                for event in fetch_until_empty_answer_with_filter(auth_account, "task"):
                    data = event["eventData"]
                    if data["taskId"] == task_id:
                        threadId = data["threadId"]
                        event_found_thread_id = True
                    if event_found_thread_id:
                        break
            if event_found_thread_id:
                break
            else:
                time.sleep(1)

    assert event_found_thread_id, f"{auth_account.env}:task_event not found"

    with allure.step("Создатель имеют доступ к обсуждению задачи"):
        response = auth_account.rapi_thread_get(
            threadId=threadId,
        )

        assert response["status"]["code"] == 20000, f"Failed to get thread info {threadId} for task {task_id}"

        assert response["results"]["threadId"] == threadId, "Wrong threadId in thread info"

        response = auth_account.rapi_getHistory(
            sn=threadId,
            count=-20,
        )
        assert response["status"]["code"] == 20000, f"Failed to getHistory on thread {threadId} for task {task_id}"

    with allure.step("Исполнитель имеют доступ к обсуждению задачи"):
        response = opponent_account.rapi_thread_get(
            threadId=threadId,
        )

        assert response["status"]["code"] == 20000, f"Failed to get thread info {threadId} for task {task_id}"

        assert response["results"]["threadId"] == threadId, "Wrong threadId in thread info"

        response = opponent_account.rapi_getHistory(
            sn=threadId,
            count=-20,
        )
        assert response["status"]["code"] == 20000, f"Failed to getHistory on thread {threadId} for task {task_id}"

    with allure.step("Третий пользователь не имеет доступ к обсуждению задачи"):
        with pytest.raises((AccessDeniedException, BadRequestException)):
            third_account.rapi_thread_get(threadId)

        with pytest.raises((AccessDeniedException, BadRequestException)):
            third_account.rapi_getHistory(
                sn=threadId,
                count=-20,
            )

    with allure.step("Указываем третьего пользователя в обсуждении"):
        assert (
            auth_account.wim_im_sendIM(
                t=threadId,
                message=f"hi @[{third_account.uin}]",
            )["response"]["statusCode"]
            == 200
        )

    with allure.step("Третьему пользователю доступно обсуждение, может писать в тред"):
        response = third_account.rapi_thread_get(threadId)
        assert response["status"]["code"] == 20000, f"Failed to get thread info {threadId} for task {task_id}"

        response = third_account.rapi_getHistory(
            sn=threadId,
            count=-20,
        )
        assert response["status"]["code"] == 20000, f"Failed to getHistory on thread {threadId} for task {task_id}"

        assert (
            third_account.wim_im_sendIM(
                t=threadId,
                message="hi i can send message to thread",
            )["response"]["statusCode"]
            == 200
        )

    with allure.step("Третий пользователь отписывается от обсуждения"):
        response = third_account.rapi_thread_unsubscribe(
            threadId=threadId,
        )

        assert response["status"]["code"] == 20000, f"Failed to unsubscribe from thread {threadId} for task {task_id}"

    with allure.step("Третий пользователь не имеет доступ к обсуждению задачи"):
        with pytest.raises((AccessDeniedException, BadRequestException)):
            third_account.rapi_thread_get(threadId)

        with pytest.raises(AccessDeniedException):
            third_account.rapi_getHistory(
                sn=threadId,
                count=-20,
            )

    with allure.step("Третий пользователь не может писать в тред"):
        assert (
            third_account.wim_im_sendIM(
                t=threadId,
                message="i can`t send message to thread",
            )["response"]["statusCode"]
            != 200
        )
