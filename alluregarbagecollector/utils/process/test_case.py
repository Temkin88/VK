"""
Методы для проверки тест кейсов на наличие определенных полей
"""

from functools import cache

import peewee as pw
from loguru import logger

import openapi_client as allure
from pydantic import ValidationError

from imjarvis import imjarvis
from enums import AllureProjects
from database import TestCase
from utils.attrs.test_case import (
    check_test_case_status,
    check_testresults_history,
)
from utils.config import configuration
from utils.allure import (
    create_allure_comment,
    change_testcase_status_to_outdated,
)
from utils.attrs import (
    check_test_case_custom_field,
    check_test_case_jira_issue,
    get_test_case_feature,
    get_test_case_product_functionality,
    get_test_case_jira_issue,
    check_last_modified_date,
)


def _get_test_case_overview_dto(
    testcase_overview_controller: allure.TestCaseOverviewControllerApi,
    testcase_id: int,
) -> allure.TestCaseOverviewDto:
    """
    Получение полной информации о тест кейсе
    :param testcase_overview_controller: API Controller
    :param testcase_id: ID тест кейса
    :return:
    """
    logger.info("Getting test case overview DTO")
    try:
        return testcase_overview_controller.get_overview(
            test_case_id=testcase_id
        )
    except ValidationError as error:
        logger.warning(f"ERROR: test case ID {testcase_id}")
        logger.exception(error)
        raise error


@logger.catch(reraise=True)
@cache
def _get_jira_issue_pds(
    issue: str,
) -> list[str]:
    result = []

    if not issue.startswith("IM"):
        logger.warning(f"Invalid issue link - {issue}")
        return result

    issue = imjarvis.issue(issue.replace(",", "").replace(".", ""))

    if (
        hasattr(issue.fields, "customfield_78005")
        and issue.fields.customfield_78005 is not None
        and len(issue.fields.customfield_78005) > 0
    ):
        for pd_f in issue.fields.customfield_78005:
            if pd_f.id not in ["37150", "37151", "37151"]:
                result.append(pd_f.value)

    else:
        logger.warning(
            f"Issue {issue.key} has no Product Functionality or Core QA"
        )

    return result


def _get_testcases_pds(testcase: allure.TestCaseOverviewDto) -> set[str]:
    result = [
        cfv.name
        for cfv in testcase.custom_fields
        if cfv.custom_field.name == "Product Functionality"
    ]

    return set(result)


def process_all_test_cases_for_pd_from_jira(
    testcase_from_tree: allure.TestCaseTreeLeafDto | int,
    testcase_bulk_controller: allure.TestCaseBulkControllerApi,
    testcase_overview_controller: allure.TestCaseOverviewControllerApi,
    comment_controller: allure.CommentControllerApi,
    project_id: AllureProjects,
):
    """
    Метод для проставки Custom field - Product Functionality из задач JIRA
    :param testcase_from_tree: Информация о кейсе со
    страницы списка кейсов из поиска
    :param testcase_bulk_controller: API Controller
    :param testcase_overview_controller: API Controller
    :param comment_controller: API Controller
    :param project_id: ID проекта тест кейса
    :return:
    """
    with logger.contextualize(
        project_id=str(project_id).split(".")[-1],
        test_case_id=testcase_from_tree
        if isinstance(testcase_from_tree, int)
        else testcase_from_tree.id,
    ):
        testcase = _get_test_case_overview_dto(
            testcase_overview_controller=testcase_overview_controller,
            testcase_id=testcase_from_tree
            if isinstance(testcase_from_tree, int)
            else testcase_from_tree.id,
        )

        if testcase.status.name in configuration["allure.extra"].get(
            "ignore_statuses", []
        ):
            logger.warning(f"Ignoring case in {testcase.status.name}")
            return

        if check_test_case_custom_field(
            test_case=testcase, custom_field_name="Product Functionality"
        ):
            logger.warning("Test case already have 'Product Functionality'")
            return

        if not check_test_case_jira_issue(test_case=testcase):
            logger.warning(f"Test case ID {testcase.id} has no issue links")
            return

        pd_f_from_jira_set = set()

        for issue_dto in testcase.issues:
            pd_f_list = _get_jira_issue_pds(issue_dto.name)

            logger.info(pd_f_list)

            pd_f_from_jira_set = pd_f_from_jira_set.union(pd_f_list)

        pd_f_from_jira_set = pd_f_from_jira_set - _get_testcases_pds(testcase)

        logger.info(pd_f_from_jira_set)

        if len(pd_f_from_jira_set) == 0:
            logger.warning("No Product Functionality to add")
            return

        logger.info("Trying to set pd_f to test case")
        logger.debug(list(pd_f_from_jira_set))
        testcase_bulk_controller.cfv_add(
            allure.TestCaseBulkCfvDto(
                selection={
                    "projectId": testcase.project_id,
                    "leafsInclude": [testcase.id],
                },
                cfv=[
                    {"name": name, "customField": {"id": 70}}
                    for name in pd_f_from_jira_set
                ],
            )
        )
        logger.success("Success")

        logger.info("Leaving comment in test case")
        comment_controller.create41(
            comment_create_dto=allure.CommentCreateDto(
                test_case_id=testcase.id,
                body="Product Functionality добавлена "
                "на основе прилинкованных Jira issue",
            )
        )
        logger.success("Success")


def process_active_test_case(
    testcase_from_tree: allure.TestCaseTreeLeafDto,
    testcase_controller: allure.TestCaseControllerApi,
    testcase_overview_controller: allure.TestCaseOverviewControllerApi,
    comment_controller: allure.CommentControllerApi,
    project_id: AllureProjects,
):
    """
    Проверка тест кейса в статусе ACTIVE

    Проверяем в кейсе наличие:
    - Custom field: Suite, Feature, Severity, Product, Product Functionality
    - Issue links
    :param testcase_from_tree: Информация о кейсе со
    страницы списка кейсов из поиска
    :param testcase_controller: API Controller
    :param testcase_overview_controller: API Controller
    :param comment_controller: API Controller
    :param project_id: ID проекта тест кейса
    :return:
    """

    with logger.contextualize(
        project_id=str(project_id).split(".")[-1],
        test_case_id=testcase_from_tree.id,
    ):
        testcase = _get_test_case_overview_dto(
            testcase_overview_controller=testcase_overview_controller,
            testcase_id=testcase_from_tree.id,
        )

        cfv_check = {
            key: check_test_case_custom_field(
                test_case=testcase, custom_field_name=key
            )
            for key in configuration["allure.extra"]["custom_fields_to_check"]
        }

        has_issues = check_test_case_jira_issue(
            test_case=testcase,
        )

        if all(cfv_check.values()):
            logger.success(f"Test case ID {testcase.id} is actually active")
        else:
            logger.info("Test case is outdated")

            create_allure_comment(
                comment_controller=comment_controller,
                test_case=testcase,
                Issues=has_issues,
                **cfv_check,
            )
            change_testcase_status_to_outdated(
                testcase_controller=testcase_controller, test_case=testcase
            )


def process_outdated_test_case(
    testcase_from_tree: allure.TestCaseTreeLeafDto,
    testcase_overview_controller: allure.TestCaseOverviewControllerApi,
    project_id: AllureProjects,
):
    """
    Проверка кейса в статусе OUTDATED

    Проверяем в кейсе наличие:
    - Custom field: Feature, Product Functionality
    - Issue links
    :param testcase_from_tree: Информация
    о кейсе со страницы списка кейсов из поиска
    :param testcase_overview_controller: Контроллер TestCase Overview API
    :param project_id: ID проекта кейса
    :return:
    """
    with logger.contextualize(
        project_id=str(project_id).split(".")[-1],
        test_case_id=testcase_from_tree.id,
    ):
        logger.info(
            f"Checking test case #{testcase_from_tree.id} "
            f"{testcase_from_tree.name}"
        )

        testcase = _get_test_case_overview_dto(
            testcase_overview_controller=testcase_overview_controller,
            testcase_id=testcase_from_tree.id,
        )

        product_functionality = get_test_case_product_functionality(
            test_case=testcase
        )

        feature = get_test_case_feature(test_case=testcase)

        jira_db_issue = get_test_case_jira_issue(test_case=testcase)

        logger.info("Creating test case model in DB")
        try:
            test_case_model, not_exists = TestCase.get_or_create(
                project_id=testcase.project_id,
                test_case_id=testcase.id,
                name=testcase.name,
                product_functionality=product_functionality,
                feature=feature,
                jira=jira_db_issue,
            )

            if not_exists:
                logger.info("Created new test case in DB")
            else:
                logger.warning("Test case already in DB")
        except pw.IntegrityError:
            logger.warning(
                "Test case already exists in DB, "
                "but with different params: "
                "name/product_functionality/feature/jira"
            )
            TestCase.update(
                name=testcase.name,
                product_functionality=product_functionality,
                feature=feature,
                jira=jira_db_issue,
            ).where(
                TestCase.project_id == testcase.project_id,
                TestCase.test_case_id == testcase.id,
            ).execute()

        logger.info(
            f"Finished checking test case "
            f"#{testcase_from_tree.id} {testcase_from_tree.name}"
        )


def process_need_review_cases(
    project_id: AllureProjects,
    testcase_from_tree: allure.TestCaseTreeLeafDto,
    comment_controller: allure.CommentControllerApi,
    testcase_controller: allure.TestCaseControllerApi,
    testcase_overview_controller: allure.TestCaseOverviewControllerApi,
):
    """
    Проверка кейсов в статусе Draft/Need review

    Проверяем что кейс висит более 2х месяцев в подобном статусе.
    Если находим - переводим в OUTDATED с комментом
    :param project_id: ID проекта кейса
    :param testcase_from_tree: инфо о кейсе
    :param comment_controller: API Controller
    :param testcase_controller: API Controller
    :param testcase_overview_controller: API Controller
    :return:
    """
    with logger.contextualize(
        project_id=str(project_id).split(".")[-1],
        test_case_id=testcase_from_tree.id,
    ):
        testcase_overview = _get_test_case_overview_dto(
            testcase_overview_controller=testcase_overview_controller,
            testcase_id=testcase_from_tree.id,
        )

        if check_last_modified_date(testcase_overview):
            comment_controller.create41_with_http_info(
                comment_create_dto=allure.CommentCreateDto(
                    test_case_id=testcase_overview.id,
                    body=f"Этот кейс находился в статусе "
                    f"{testcase_overview.status.name} больше 2х месяцев. "
                    f"Требуется его актуализация.",
                )
            )

            change_testcase_status_to_outdated(
                testcase_controller=testcase_controller,
                test_case=testcase_overview,
            )


def process_need_to_archive_cases(
    project_id: AllureProjects,
    testcase_from_tree: allure.TestCaseTreeLeafDto,
    testcase_overview_controller: allure.TestCaseOverviewControllerApi,
    comment_controller: allure.CommentControllerApi,
    testcase_controller: allure.TestCaseControllerApi,
    audit_controller: allure.TestCaseAuditControllerApi,
):
    """
    Проверка кейсов на необходимость их архивации
    :param project_id: ID проекта
    :param testcase_from_tree: тест кейс
    :param testcase_overview_controller: API Controller
    :param comment_controller: API Controller
    :param testcase_controller: API Controller
    :param audit_controller: API Controller
    :return:
    """
    with logger.contextualize(
        project_id=str(project_id).split(".")[-1],
        test_case_id=testcase_from_tree.id,
    ):
        testcase_overview = _get_test_case_overview_dto(
            testcase_overview_controller=testcase_overview_controller,
            testcase_id=testcase_from_tree.id,
        )

        if not check_test_case_status(
            audit_controller=audit_controller, test_case=testcase_overview
        ):
            logger.info("Status of test case was updated less than year ago")
            return
        if not check_testresults_history(
            testcase_controller=testcase_controller,
            test_case_id=testcase_from_tree.id,
        ):
            logger.start("Last launch of test case was less than year ago")
            return

        comment_controller.create41_with_http_info(
            comment_create_dto=allure.CommentCreateDto(
                test_case_id=testcase_overview.id,
                body="Кейс в статусе Active/Actual более года, "
                "но ни разу не использовался. "
                "Требуется принять решение об архивации кейса.",
            )
        )
        change_testcase_status_to_outdated(
            testcase_controller=testcase_controller,
            test_case=testcase_overview,
        )
