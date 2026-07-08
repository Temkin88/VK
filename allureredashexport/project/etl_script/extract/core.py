from typing import Any, Generator

import openapi_client as allure
from openapi_client import TestCaseDto, IssueDto, CustomFieldValueDto

from common.logger import logger

from .filters import FILTER_BY_SUITE_BASE64


def collect_all_pages(
    project_id: int,
    testcase_tree_ctlr: allure.TestCaseTreeControllerApi,
) -> Generator[allure.PageTestCaseTreeLeafDto, Any, None]:
    result = testcase_tree_ctlr.get_leaves1(
        project_id=project_id,  # noqa
        size=100,
        search=FILTER_BY_SUITE_BASE64,
        sort=['id,asc']
    )

    logger.info(f"Total pages count: {result.total_pages}")

    for i in range(result.total_pages + 1):

        logger.info(f"Current page: {i}")

        yield testcase_tree_ctlr.get_leaves1(
            project_id=project_id,  # noqa
            size=100,
            search=FILTER_BY_SUITE_BASE64,
            sort=['id,asc'],
            page=i,
        )


def extract_data(
        project_id: int,
        testcase_ctlr: allure.TestCaseControllerApi,
        testcase_issue_ctlr: allure.TestCaseIssueControllerApi,
        testcase_tree_ctlr: allure.TestCaseTreeControllerApi,
        testcase_cfv_ctlr: allure.TestCaseCustomFieldControllerApi
) -> Generator[tuple[TestCaseDto, list[IssueDto], list[CustomFieldValueDto]], Any, None]:
    """
    Извлечение информации о тест-кейсах и значения их custom fields
    :param project_id: ID проекта тест-кейсов
    :param testcase_ctlr: API-контроллер для получения информации о тест-кейсе (одном)
    :param testcase_issue_ctlr: API-контроллер для получения информации о JIRA-задачах
    :param testcase_tree_ctlr: API-контроллер для получения списка кейсов по фильтру
    :param testcase_cfv_ctlr: API-контроллер для получения информации о custom fields тест-кейса
    :returns: tuple из DTO тест-кейса и списка DTO значений его custom field's
    """

    for result in collect_all_pages(project_id, testcase_tree_ctlr):

        logger.info(f'Elements on page: {len(result.content)}')

        if not len(result.content):
            break

        for test_case_from_leaf in result.content:

            logger.info(f'Getting info for case #{test_case_from_leaf.id} "{test_case_from_leaf.name}"')

            test_case_dto = testcase_ctlr.find_one11(
                id=test_case_from_leaf.id
            )
            logger.success(f'Received case DTO for #{test_case_from_leaf.id}')

            test_case_issues_dto = testcase_issue_ctlr.get_issues1(
                test_case_id=test_case_from_leaf.id
            )

            logger.success(f'Received case issues-DTO for #{test_case_from_leaf.id}')

            cfv_dto = testcase_cfv_ctlr.get_cfv1(
                test_case_id=test_case_from_leaf.id
            )
            logger.success(f'Received case cfv-DTO for #{test_case_from_leaf.id}')

            yield test_case_dto, test_case_issues_dto, cfv_dto
