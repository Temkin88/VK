import time

import allure
import pytest
import datetime
import uuid

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX
from support.cases.tasks import TASK_TITLE_CASES, TASK_DURATION_CASES


@allure.id("814338")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Тред задачи")
@allure.title("Создатель и исполнитель имеют доступ к треду задач и могут туда писать")
@VKTI
@PRE_VKTI
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("task_title", TASK_TITLE_CASES)
@pytest.mark.parametrize("task_duration", TASK_DURATION_CASES)
@pytest.mark.first
def test_thread_task(
    auth_account,
    task_title,
    task_duration,
    opponent_account,
    ENV_PLATFORM,
    fetch_until_empty_answer_with_filter,
):
    """
    Создание задачи, доступ и отправка сообщений в тред задачи, создателем и исполнителем.
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
    with allure.step("Получения thread_id задачи"):
        event_found_thread_id = False

        for _ in range(3):
            with allure.step(f"Попытка #{_}"):
                for event in fetch_until_empty_answer_with_filter(auth_account, "task"):
                    data = event["eventData"]
                    if data["taskId"] == task_id:
                        thread_id = data["threadId"]
                        event_found_thread_id = True
                    if event_found_thread_id:
                        break
            if event_found_thread_id:
                break
            else:
                time.sleep(1)

    assert event_found_thread_id, f"{auth_account.env}:task_event not found"

    with allure.step("Создатель имеет доступ к треду задачи"):
        response = auth_account.rapi_thread_get(
            thread_id,
        )

        assert response["status"]["code"] == 20000, f"Failed to get thread info {thread_id} for task {task_id}"
        assert response["results"]["threadId"] == thread_id, "Wrong thread_id in thread info"

        response = auth_account.rapi_getHistory(
            sn=thread_id,
        )

        assert response["status"]["code"] == 20000, f"Failed to getHistory on thread {thread_id} for task {task_id}"

    with allure.step("Исполнитель имеют доступ к обсуждению задачи"):
        response = opponent_account.rapi_thread_get(
            thread_id,
        )

        assert response["status"]["code"] == 20000, f"Failed to get thread info {thread_id} for task {task_id}"
        assert response["results"]["threadId"] == thread_id, "Wrong thread_id in thread info"

        response = opponent_account.rapi_getHistory(
            sn=thread_id,
        )
        assert response["status"]["code"] == 20000, f"Failed to getHistory on thread {thread_id} for task {task_id}"

    with allure.step("Создатель может написать в обсуждение задачи"):
        creator_message = f"Creator text [{uuid.uuid4().hex[:6]}]"
        response = auth_account.wim_im_sendIM(
            t=thread_id,
            message=creator_message,
        )
        assert response["response"]["statusCode"] == 200, f"Failed to send message. Response: {response}"

    with allure.step("Исполнитель может написать в обсуждение задачи"):
        executor_message = f"Executor text [{uuid.uuid4().hex[:6]}]"
        response = opponent_account.wim_im_sendIM(
            t=thread_id,
            message=executor_message,
        )

        assert response["response"]["statusCode"] == 200, f"Failed to send message. Response: {response}"

    with allure.step("Получение истории треда задачи"):
        history = auth_account.rapi_getHistory(
            sn=thread_id,
        )

        assert history["status"]["code"] == 20000, "Failed to get thread history"

    with allure.step("Проверяем что в истории треда задачи есть сообщения от создателя и исполнителя"):
        messages = [msg["text"] for msg in history["results"]["messages"] if "text" in msg]

        assert creator_message in messages, f"Creator's message '{creator_message}' not found in history"
        assert executor_message in messages, f"Executor's message '{executor_message}'  not found in history"
