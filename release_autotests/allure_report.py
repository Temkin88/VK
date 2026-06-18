import logging
import os
import time

import requests

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_jira_issue():
    JIRA_ISSUE = os.getenv("JIRA_ISSUE")
    logger.info(f"JIRA_ISSUE: {JIRA_ISSUE}")

    if JIRA_ISSUE is not None:
        return JIRA_ISSUE

    SANDBOX = os.getenv("SANDBOX")
    logger.info(f"SANDBOX: {SANDBOX}")

    if SANDBOX is not None:
        POTENCIAL_JIRA_ISSUE = SANDBOX.split(".")[0].upper()

        for JIRA_PROJECT_KEY in ("IMSERVER", "IMOPS", "IMDEVOPS", "IMQA"):
            if POTENCIAL_JIRA_ISSUE.startswith(JIRA_PROJECT_KEY):
                return POTENCIAL_JIRA_ISSUE

    return None


JIRA_ISSUE = get_jira_issue()


def launch_name(ALLURE_LAUNCH_ID) -> str:
    launch_info = session.get(
        url=f"https://allure.vk.team/api/rs/launch/{ALLURE_LAUNCH_ID}",
    ).json()

    name = launch_info["name"]

    return f"[{name}](https://allure.vk.team/launch/{ALLURE_LAUNCH_ID})"


def launch_tags(ALLURE_LAUNCH_ID) -> str:
    launch_info = session.get(
        url=f"https://allure.vk.team/api/rs/launch/{ALLURE_LAUNCH_ID}",
    ).json()

    return ",".join([x["name"] for x in launch_info["tags"]])


def is_launch_finished(ALLURE_LAUNCH_ID) -> bool:
    launch_jobs_info = session.get(
        url=f"https://allure.vk.team/api/rs/launch/{ALLURE_LAUNCH_ID}/job",
    ).json()

    common_result = sum([x["stage"] in ["run_failure", "finished"] for x in launch_jobs_info])

    return common_result == len(launch_jobs_info)


def unresolved_results_text(ALLURE_LAUNCH_ID) -> str:
    results = session.get(
        url=f"https://allure.vk.team/api/rs/launch/{ALLURE_LAUNCH_ID}/unresolved",
    ).json()

    results = results["content"]

    failed_tests = list(filter(lambda x: x["status"] == "failed", results))
    broken_tests = list(filter(lambda x: x["status"] == "broken", results))

    if len(failed_tests) + len(broken_tests) == 0:
        return "Новых ошибок не найдено"

    text = ""

    for kind in ("failed", "broken"):
        tests_list = failed_tests if kind == "failed" else broken_tests

        if len(tests_list) == 0:
            continue

        text += f'Тесты со статусом "{kind}":\n'
        text += "\n".join([x["name"] for x in tests_list])
        text += "\n\n"

    return text.strip()


def stats_text(ALLURE_LAUNCH_ID: int | str) -> str:
    session.post(url=f"https://allure.vk.team/api/launch/{ALLURE_LAUNCH_ID}/defect/apply")
    stats = session.get(
        f"https://allure.vk.team/api/rs/launch/{ALLURE_LAUNCH_ID}/statistic",
    ).json()

    total_count = sum([x["count"] for x in stats])
    total_half_count = int(total_count / 2)

    stats = {
        item["status"]: item["count"] for item in stats if item["status"] in ["passed", "skipped", "failed", "broken"]
    }

    stats_sum_failed = stats.get("failed", 0) + stats.get("broken", 0)

    text = ""

    if stats_sum_failed >= total_half_count:
        text += "\n🔥🔥🔥ALARM🔥🔥🔥: @[ivan.kulikov@corp.mail.ru], @[v.sindalovsky@vk.team]\n"

    text += "\n".join([f"{key}: {value}" for key, value in stats.items()])

    text += f"\n\nTotal: {total_count}"

    return text.strip()


def api_version():
    return os.getenv("API_VERSION")


with requests.Session() as session:
    ALLURE_TOKEN = os.getenv("ALLURE_TOKEN")

    if ALLURE_TOKEN is None:
        raise ValueError("ALLURE_TOKEN is not defined")

    session.headers = {
        "Authorization": f"Api-Token {ALLURE_TOKEN}",
    }
    BUILD_START_USER = os.getenv("BUILD_START_USER")
    if BUILD_START_USER is None or BUILD_START_USER == "null":
        BUILD_START_USER = "exec timer"
    else:
        BUILD_START_USER = f"@[{BUILD_START_USER}]"
    ALLURE_LAUNCH_ID = os.getenv("ALLURE_LAUNCH_ID")

    if ALLURE_LAUNCH_ID is None:
        raise ValueError("ALLURE_LAUNCH_ID is null")

    counter = 0

    while not is_launch_finished(ALLURE_LAUNCH_ID) and counter <= 20:
        logger.info("Waiting for launch to be finished ...")
        time.sleep(4)
        counter += 1

    LAUNCH_NAME = launch_name(ALLURE_LAUNCH_ID)
    LAUNCH_TAGS = launch_tags(ALLURE_LAUNCH_ID)
    LAUNCH_STATS = stats_text(ALLURE_LAUNCH_ID)
    LAUNCH_UNRESOLVED_RESULTS = unresolved_results_text(ALLURE_LAUNCH_ID)
    API_VERSION = api_version()
    TESTS_BRANCH = os.getenv("TESTS_BRANCH", "master")
    RUNNING_TIME = os.getenv("RUNNING_TIME", "Duration unknown")
    SUPPLY_URL = os.getenv("SUPPLY_URL")
    jira_tasks = "not defined"

    if JIRA_ISSUE is not None and JIRA_ISSUE:
        session.patch(
            url=f"https://allure.vk.team/api/rs/launch/{ALLURE_LAUNCH_ID}",
            json={
                "id": ALLURE_LAUNCH_ID,
                "issues": [{"integrationId": 2, "name": current_issue} for current_issue in JIRA_ISSUE.split(";")],
            },
        )
        jira_tasks = "\n" + "\n".join(
            [f"[{issue}](https://jira.vk.team/browse/{issue})" for issue in JIRA_ISSUE.split(";")]
        )


text = f"""
{LAUNCH_NAME}

Started by: {BUILD_START_USER}
Launch tags: {LAUNCH_TAGS}
PYTEST_MARKER: {os.getenv("PYTEST_MARKER", "NOT_DEFINED")}
API_VERSION: {API_VERSION}
TESTS_BRANCH: {TESTS_BRANCH}
SUPPLY_URL: {SUPPLY_URL}
Build duration: {RUNNING_TIME}
JIRA Tasks: {jira_tasks}

Статистика тестов:
{LAUNCH_UNRESOLVED_RESULTS}

{LAUNCH_STATS}""".strip()

print(text)  # noqa:T201
