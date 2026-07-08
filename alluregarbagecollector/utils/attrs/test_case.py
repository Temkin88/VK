from typing import Optional, TYPE_CHECKING
from datetime import datetime

from loguru import logger

if TYPE_CHECKING:
    from jira import Issue

import openapi_client as allure

from enums import ProductFunctionality, created_before, year_ago_date
from imjarvis import imjarvis
from database import JiraIssue
from utils.config import configuration


def check_test_case_custom_field(
    test_case: allure.TestCaseOverviewDto, custom_field_name: str
) -> bool:
    """
    Проверка наличия определенного custom field у тест кейса
    :param test_case: тест кейсов
    :param custom_field_name: Имя Custom field
    :return: True - если есть хотя бы одно значение, False - если нет вообще
    """

    for custom_field in filter(
        lambda x: x.custom_field.name == custom_field_name,
        test_case.custom_fields,
    ):
        logger.success(f"{custom_field_name} found - {custom_field.name}")
        return True

    return False


def check_test_case_jira_issue(test_case: allure.TestCaseOverviewDto) -> bool:
    """
    Проверка что к тест кейсу вообще прикреплены задачи из JIRA
    :param test_case: тест кейс
    :return: True - если прикреплены, False - если нет
    """
    return len(test_case.issues) > 0 or configuration["allure.extra"].get(
        "ignore_issues_count", False
    )


def get_test_case_product_functionality(
    test_case: allure.TestCaseOverviewDto,
) -> str:
    """
    Проверка наличия Custom Field - Product Functionality у тест кейса
    :param test_case: тест кейс
    :return: Product Functionality если указана, если нет - возвращает UNKNOWN
    """
    logger.info("Checking test case for product functionality")

    for custom_field in filter(
        lambda x: x.custom_field.name == "Product Functionality"
        and x.name in ProductFunctionality,
        test_case.custom_fields,
    ):
        logger.success(f"Found product functionality - {custom_field.name}")
        return custom_field.name
    else:
        logger.warning(
            "Product functionality not found, setting default - 35. Core QA"
        )
        return "35. Core QA"


def get_test_case_feature(test_case: allure.TestCaseOverviewDto) -> str:
    """
    Проверка наличия Custom Field - Feature у тест кейса
    :param test_case: тест кейс
    :return: Feature если указана, если нет - возвращает UNKNOWN
    """
    logger.info("Checking test case for Custom field - Feature")

    for custom_field in filter(
        lambda x: x.custom_field.name == "Feature", test_case.custom_fields
    ):
        logger.success(f"Feature found - {custom_field.name}")
        return custom_field.name
    else:
        logger.info("Feature not found - setting default - UNKNOWN")
        return "UNKNOWN"


def get_test_case_jira_issue(
    test_case: allure.TestCaseOverviewDto,
) -> Optional[JiraIssue]:
    """
    Проверка что к тест кейсу прикреплена задача в JIRA

    Задача должна быть в проекте IMQA и прикреплена
    к текущему эпику на актуализацию тест кейсов
    :param test_case: тест кейс
    :return: Номер задачи если она прикреплена
    """
    logger.info("Checking test case for linked task from Epic IMQA-3877")

    for t_issue in test_case.issues:
        if not t_issue.name.startswith("IMQA"):
            continue

        jira_key = t_issue.name.replace(",", "")
        jira_db_issue = JiraIssue.get_or_none(jira_id=jira_key)

        if jira_db_issue is not None:
            logger.success(f"Found existing task in DB - {jira_key}")
            return jira_db_issue

        j_issue: Issue = imjarvis.issue(jira_key)

        if (
            j_issue.fields.customfield_15500
            == configuration["jira.settings.extra"]["test_cases"][
                "customfield_15500"
            ]
            and j_issue.fields.resolution is None
        ):
            logger.success(f"Found existing task in JIRA - {jira_key}")
            jira_db_issue = JiraIssue.create(jira_id=j_issue.key)
            return jira_db_issue
    else:
        logger.warning("Linked task not found - setting default value - None")


def check_last_modified_date(testcase: allure.TestCaseOverviewDto) -> bool:
    """
    Проверяем что дата последнего изменения кейса не старее двух месяцев
    :param testcase: инфо о тест кейсе
    :return: True если старее
    """
    result = (
        datetime.fromtimestamp(testcase.last_modified_date / 1000)
        < created_before
    )

    logger.info(f"case not modified for 2 month: {result}")

    return result


def check_test_case_status(
    audit_controller: allure.TestCaseAuditControllerApi,
    test_case: allure.TestCaseOverviewDto,
) -> bool:
    """
    Проверка что последняя смена статуса произошла более года назад
    :param audit_controller: API Controller
    :param test_case: test case info
    :return: True - если более года назад
    """
    status_change_date = datetime.fromtimestamp(
        test_case.last_modified_date / 1000
    )

    audit_result = audit_controller.find_all12(
        test_case_id=test_case.id, size=300
    )

    for log in audit_result.content:
        for data in log.data:
            status_id = data.diff.actual_instance.status_id
            if status_id is not None and status_id.new_value in [-3, 36]:
                status_change_date = datetime.fromtimestamp(
                    log.timestamp / 1000
                )
                break

    return status_change_date <= year_ago_date


def check_testresults_history(
    testcase_controller: allure.TestCaseControllerApi, test_case_id: int
) -> bool:
    """
    Проверка что последний запуск теста был более года назад
    :param testcase_controller: API Controller
    :param test_case_id: ID кейса
    :return: True - если последний запуск был более года назад
    """
    history = testcase_controller.find_history1(id=test_case_id)

    if not history.content:
        return True

    launch = history.content[0]

    return (
        datetime.fromtimestamp(launch.last_modified_date / 1000)
        <= year_ago_date
    )
