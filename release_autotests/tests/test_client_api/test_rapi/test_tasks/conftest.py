import concurrent.futures
import logging

import allure
import pytest

log = logging.getLogger(__name__)


@allure.title("Очистка списка задач")
@pytest.fixture(scope="session", autouse=True)
def clean_task_list(auth_account, opponent_account):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        for account in (auth_account, opponent_account):
            for task in account.iter_task_list_for_clean(page_size=50):
                if task["creator"] == account.uin and task["status"] != "closed":
                    futures.append(
                        executor.submit(
                            account.tasks_edit,
                            taskId=task["taskId"],
                            status="closed",
                        ),
                    )

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as error:
                log.error(error)

        futures = []

        for account in (auth_account, opponent_account):
            for task in account.iter_task_list_for_clean(page_size=50):
                if not task["isRead"]:
                    futures.append(executor.submit(account.tasks_setRead, [task["taskId"]]))

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as error:
                log.error(error)
