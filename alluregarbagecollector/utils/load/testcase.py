"""
Методы для работы с тест кейсами в Allure TestOps
"""

from __future__ import annotations

from datetime import datetime, timedelta

from loguru import logger

import openapi_client as allure

from database import get_test_cases_by_f_pd, JiraIssue, TestCase
from enums import ProductFunctionality
from utils.matrix import get_pd_f_matrix
from utils.imbot import send_notification
from utils.allure import get_test_case_link
from utils.load.issue import create_issue


def get_test_case_comments(
    comment_controller: allure.CommentControllerApi, test_case_id: int | str
) -> list[allure.CommentDto]:
    """
    Получение комментариев к тест кейсу из Allure TestOps
    :param comment_controller: API Controller
    :param test_case_id: ID тест кейса
    :return: Список комментариев
    """
    comments_page_dto = comment_controller.find_all38(test_case_id=test_case_id)

    return comments_page_dto.content


def get_test_cases_models_by_f_pd(
    product_functionality: str, feature: str
) -> list[TestCase]:
    """
    Получить список найденных кейсов по продуктовой функциональности и фиче
    :param product_functionality: Продуктовая функциональность
    :param feature: Фича
    :return: Список кейсов
    """
    query = get_test_cases_by_f_pd(product_functionality, feature)

    return list(query)


def assemble_task_description(
    comment_controller: allure.CommentControllerApi,
    test_cases: list,
    pd_is_not_mentioned: bool = False,
) -> str:
    """
    Сборка описания для задачи в JIRA
    :param comment_controller: API Controller
    :param test_cases: Список тест-кейсов в задаче
    :param pd_is_not_mentioned: Флаг - нужно ли упоминать продукт в комментарии
    :return:
    """
    text = "\nНе забудьте поправить кейсы в других проектах !\n"
    if pd_is_not_mentioned:
        text += "Необходимо в кейсах проставить продуктовую функциональность\n"
    text += "\nСписок кейсов:\n"

    for test_case in test_cases:
        allure_link = get_test_case_link(
            project_id=test_case.project_id,
            test_case_id=test_case.test_case_id,
        )

        subtext = (
            f"* [#{test_case.test_case_id} {test_case.name}|{allure_link}]"
        )

        comments = get_test_case_comments(
            comment_controller=comment_controller,
            test_case_id=test_case.test_case_id,
        )

        text += "\n".join(
            [subtext]
            + [
                f"** {comment.created_by}: {comment.body}"
                for comment in comments[::-1][:2][::-1]
            ]
        )

        text += "\n"

    return text


def load_test_cases(
    comment_controller: allure.CommentControllerApi,
    testcase_issue_controller: allure.TestCaseIssueControllerApi,
):
    """
    Проход по тест кейсам из базы для создания задачи в JIRA
    и прикрепления ее в Allure TestOps
    :param comment_controller: API Controller
    :param testcase_issue_controller: API Controller
    :return:
    """
    current_date = datetime.now()
    planned_end_date = current_date + timedelta(days=4)
    week_number = current_date.isocalendar().week

    for pd, f in get_pd_f_matrix():
        logger.info(
            f"Getting test cases for: product_functionality={pd}, feature={f}"
        )

        test_cases = get_test_cases_models_by_f_pd(
            product_functionality=pd, feature=f
        )

        logger.success(f"Got cases total: {len(test_cases)}")

        logger.info("Creating description for JIRA task")

        description = assemble_task_description(
            comment_controller=comment_controller,
            test_cases=test_cases,
            pd_is_not_mentioned=pd == ProductFunctionality.CORE_QA.value,
        )

        logger.success("Description created")

        logger.info("Creating JIRA task")

        created_issue_key = create_issue(
            title=f"[{f}] Кейсы на актуализацию (Неделя: {week_number})",
            description=description,
            product_functionality=pd,
        )

        logger.success(f"Task created: {created_issue_key}")

        logger.info("Linking test cases to JIRA task in Allure TestOps")

        for test_case in test_cases:
            test_case_issues = testcase_issue_controller.get_issues1(
                test_case_id=test_case.test_case_id
            )

            testcase_issue_controller.set_issues2(
                test_case_id=test_case.test_case_id,
                issue_dto=[
                    *test_case_issues,
                    allure.IssueDto(
                        integration_id=2,
                        name=created_issue_key,
                        url=f"https://jira.vk.team/browse/{created_issue_key}",
                    ),
                ],
            )

        logger.success("Test cases linked")

        issue_model = JiraIssue.create(jira_id=created_issue_key)

        logger.info("Creating link between test cases and JIRA task")

        TestCase.update(jira=issue_model).where(
            TestCase.product_functionality == pd,
            TestCase.feature == f,
            TestCase.jira.is_null(),
        ).execute()

        logger.success(f"Test cases linked to task {created_issue_key}")

        send_notification(
            jira_key=created_issue_key,
            product_functionality=pd,
            feature=f,
            week_number=week_number,
            planned_end=planned_end_date.date(),
        )
