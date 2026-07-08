from loguru import logger

import openapi_client as allure


def change_testcase_status_to_outdated(
    testcase_controller: allure.TestCaseControllerApi,
    test_case: allure.TestCaseOverviewDto,
):
    """
    Изменение статуса тест кейса на OUTDATED в Allure TestOps
    :param testcase_controller: API Controller
    :param test_case: тест кейс
    :return:
    """
    with logger.contextualize(
        project_id=test_case.project_id, test_case_id=test_case.id
    ):
        logger.debug("Trying to change test case status to OUTDATED")

        testcase_controller.patch12_with_http_info(
            id=test_case.id,
            test_case_patch_dto=allure.TestCasePatchDto(
                workflow_id=test_case.workflow.id, status_id=-4
            ),
        )

        logger.success("Status successfully changed")
