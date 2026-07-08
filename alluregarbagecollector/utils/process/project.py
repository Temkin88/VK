"""
Проверка тест кейсов проекта в статусах ACTIVE и OUTDATED
"""

from typing import Callable

from loguru import logger

from concurrent.futures import ThreadPoolExecutor

import openapi_client as allure

from enums import (
    AllureProjects,
    all_manual_search_str,
    active_search_str,
    outdated_search_str,
    need_review_and_draft_search_str,
)
from utils.config import configuration as cfg
from utils.process.test_case import (
    process_all_test_cases_for_pd_from_jira,
    process_active_test_case,
    process_outdated_test_case,
    process_need_review_cases,
    process_need_to_archive_cases,
)


def iter_testcase_tree_pages_content(
    testcase_tree_controller,
    stage_name: str,
    project_id: AllureProjects,
    search_str: str,
    page_size: int,
):
    """
    Итератор по страницам дерева с кейсами
    :param testcase_tree_controller: API Controller
    :param stage_name: Название этапа, для которого получает страницы
    :param project_id: ID проекта
    :param search_str: Строка поиска, по которой должны отбираться кейсы
    :param page_size: размер страницы с кейсами
    :return: итератор по кейсам
    """

    i = 1

    logger.info(f"[{stage_name}] Requesting first page of tree")

    testcase_tree = testcase_tree_controller.get_leaves1(
        project_id=project_id.value,
        search=search_str,
        page=i,
        size=page_size,
    )

    logger.info(
        f"[{stage_name}] "
        f"Total pages count - {testcase_tree.total_pages}, "
        f"page size - {page_size}"
    )

    while True:
        i += 1

        for testcase in testcase_tree.content:
            yield testcase

        if testcase_tree.last:
            break

        logger.info(
            f"[{stage_name}] "
            f"Requesting {i}/{testcase_tree.total_pages} page of tree"
        )

        testcase_tree = testcase_tree_controller.get_leaves1(
            project_id=project_id.value,
            search=search_str,
            page=i,
            size=page_size,
        )


def process_cases(
    process_test_cases_generic_callable: Callable,
    stage_name: str,
    project_id: AllureProjects,
    search_str: str,
    page_size: int,
    executor: ThreadPoolExecutor,
    testcase_tree_controller: allure.TestCaseTreeControllerApi,
):
    """
    Process generic callable in executer
    :param process_test_cases_generic_callable:
    :param stage_name:
    :param project_id:
    :param search_str:
    :param page_size:
    :param executor:
    :param testcase_tree_controller:
    :return:
    """
    with logger.contextualize(project_id=str(project_id).split(".")[-1]):
        logger.info(f"[{stage_name}] Trying to get test cases tree")
        with logger.catch(Exception):
            futures = []

            for future in executor.map(
                process_test_cases_generic_callable,
                iter_testcase_tree_pages_content(
                    testcase_tree_controller=testcase_tree_controller,
                    stage_name=stage_name,
                    project_id=project_id,
                    search_str=search_str,
                    page_size=page_size,
                ),
            ):
                futures.append(future)

            for future in futures:
                if future is not None:
                    future.result()

            logger.info(f"[{stage_name}] Finished")


def process_project(
    testcase_tree_controller: allure.TestCaseTreeControllerApi,
    testcase_controller: allure.TestCaseControllerApi,
    testcase_bulk_controller: allure.TestCaseBulkControllerApi,
    testcase_overview_controller: allure.TestCaseOverviewControllerApi,
    comment_controller: allure.CommentControllerApi,
    audit_controller: allure.TestCaseAuditControllerApi,
    project_id: AllureProjects,
):
    """
    Проверка тест кейсов проекта в статусах Active/Actual/Need Review/OUTDATED
    :param testcase_tree_controller: API Controller
    :param testcase_controller: API Controller
    :param testcase_bulk_controller: API Controller
    :param testcase_overview_controller: API Controller
    :param comment_controller: API Controller
    :param audit_controller: API Controller
    :param project_id: ID проекта
    :return:
    """
    with logger.contextualize(project_id=str(project_id).split(".")[-1]):  # noqa: SIM117
        with ThreadPoolExecutor(max_workers=2) as executor:
            page_size = cfg["allure.extra"]["page_size"]

            process_cases(
                lambda x: process_need_to_archive_cases(
                    project_id=project_id,
                    testcase_controller=testcase_controller,
                    testcase_from_tree=x,
                    testcase_overview_controller=testcase_overview_controller,
                    comment_controller=comment_controller,
                    audit_controller=audit_controller,
                ),
                stage_name="[Archive] Checking Active/Actual cases usage",
                project_id=project_id,
                search_str=active_search_str,
                page_size=page_size,
                executor=executor,
                testcase_tree_controller=testcase_tree_controller,
            )

            process_cases(
                lambda x: process_need_review_cases(
                    project_id=project_id,
                    testcase_from_tree=x,
                    comment_controller=comment_controller,
                    testcase_controller=testcase_controller,
                    testcase_overview_controller=testcase_overview_controller,
                ),
                stage_name="[Need Review] Checking "
                "forgotten test cases in Draft/Need review",
                project_id=project_id,
                search_str=need_review_and_draft_search_str,
                page_size=page_size,
                executor=executor,
                testcase_tree_controller=testcase_tree_controller,
            )

            process_cases(
                lambda x: process_all_test_cases_for_pd_from_jira(
                    testcase_from_tree=x,
                    testcase_bulk_controller=testcase_bulk_controller,
                    testcase_overview_controller=testcase_overview_controller,
                    comment_controller=comment_controller,
                    project_id=project_id,
                ),
                stage_name="[PDF Matching] Match pdf from jira to allure",
                project_id=project_id,
                search_str=all_manual_search_str,
                page_size=page_size,
                executor=executor,
                testcase_tree_controller=testcase_tree_controller,
            )

            process_cases(
                lambda x: process_active_test_case(
                    testcase_from_tree=x,
                    testcase_controller=testcase_controller,
                    testcase_overview_controller=testcase_overview_controller,
                    comment_controller=comment_controller,
                    project_id=project_id,
                ),
                stage_name="Check cases in ACTIVE/ACTUAL status",
                project_id=project_id,
                search_str=active_search_str,
                page_size=page_size,
                executor=executor,
                testcase_tree_controller=testcase_tree_controller,
            )

            process_cases(
                lambda x: process_outdated_test_case(
                    testcase_from_tree=x,
                    testcase_overview_controller=testcase_overview_controller,
                    project_id=project_id,
                ),
                stage_name="Check cases in OUTDATED status",
                project_id=project_id,
                search_str=outdated_search_str,
                page_size=page_size,
                executor=executor,
                testcase_tree_controller=testcase_tree_controller,
            )
