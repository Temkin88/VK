"""
Проверка тест кейсов в разных проектах Allure TestOps
"""

import sys

import urllib3
from concurrent.futures import ThreadPoolExecutor

from loguru import logger

import openapi_client as allure

from enums import AllureProjects
from utils.config.config import configuration as cfg
from utils.load import load_test_cases
from utils.process.defect import process_defects
from utils.process.project import process_project


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


logger.remove()
logger.add(sink=sys.stderr, **cfg["loguru.std"])
logger.add(**cfg["loguru.file"])
logger.configure(extra=cfg["loguru.extra"])


configuration = allure.Configuration()
configuration.verify_ssl = False


logger.info("Starting pipeline")

with allure.ApiClient(
    configuration=configuration,
    header_name="Authorization",
    header_value=cfg["allure"]["token"],
) as client:
    audit_controller = allure.TestCaseAuditControllerApi(api_client=client)
    defect_controller = allure.DefectControllerApi(api_client=client)
    testcase_tree_controller = allure.TestCaseTreeControllerApi(
        api_client=client
    )
    testcase_controller = allure.TestCaseControllerApi(api_client=client)
    testcase_bulk_controller = allure.TestCaseBulkControllerApi(
        api_client=client
    )
    testcase_overview_controller = allure.TestCaseOverviewControllerApi(
        api_client=client
    )
    testcase_issue_controller = allure.TestCaseIssueControllerApi(
        api_client=client
    )
    comment_controller = allure.CommentControllerApi(api_client=client)

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []

        for future in executor.map(
            lambda x: process_defects(
                defect_controller=defect_controller,
                project_id=x,
                stage_name=f"Check defects in {x}",
            ),
            AllureProjects,
        ):
            futures.append(future)

        for future in executor.map(
            lambda x: process_project(
                project_id=x,
                testcase_controller=testcase_controller,
                testcase_tree_controller=testcase_tree_controller,
                testcase_bulk_controller=testcase_bulk_controller,
                testcase_overview_controller=testcase_overview_controller,
                comment_controller=comment_controller,
                audit_controller=audit_controller,
            ),
            AllureProjects,
        ):
            futures.append(future)

        for future in futures:
            if future is not None:
                future.result()

    load_test_cases(
        comment_controller=comment_controller,
        testcase_issue_controller=testcase_issue_controller,
    )


logger.info("Finished pipeline")
