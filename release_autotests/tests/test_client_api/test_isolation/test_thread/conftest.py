import logging

import allure
import pytest
import time

log = logging.getLogger(__name__)


@allure.title("Подготовка треда для тестов")
@pytest.fixture(scope="session", params=["group", "channel"])
def prepared_thread(request, prepare_test_chats_msg_isolation, ENV_PLATFORM):
    auth_account, _, group, channel = prepare_test_chats_msg_isolation

    target = group if request.param == "group" else channel

    msg_id = auth_account.send_basic_message(
        sn=target,
        text="Message for threads test",
    )

    thread_id = auth_account.add_thread(chat_id=target, msg_id=msg_id)

    return target, msg_id, thread_id


@allure.title("Получения threadId задачи")
@pytest.fixture(scope="session")
def thread_id_cache():
    return {}


@pytest.fixture
def fetch_thread_id(auth_account_with_domain_testbiz, fetch_until_empty_answer_with_filter, thread_id_cache):
    def get_thread_id(task_id):
        if task_id in thread_id_cache:
            return thread_id_cache[task_id]

        for attempt in range(3):
            with allure.step(f"Попытка #{attempt + 1}"):
                events = fetch_until_empty_answer_with_filter(auth_account_with_domain_testbiz, "task")
                for event in events:
                    data = event["eventData"]
                    if data["taskId"] == task_id:
                        thread_id = data["threadId"]
                        thread_id_cache[task_id] = thread_id
                        return thread_id
                time.sleep(1)

        pytest.fail(f"Could not find thread_id for task_id: {task_id}")

    return get_thread_id
