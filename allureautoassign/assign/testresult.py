import logging
from concurrent.futures import ThreadPoolExecutor

import openapi_client as allure

from database import TestResult

logger = logging.getLogger(__name__)


def assign_testresults(testresult_run_ctlr: allure.TestResultRunControllerApi):
    logger.info("[ASSIGN] Assigning cases in Allure from calculated data in DB")

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []

        for testresult in TestResult.select().where(
            TestResult.user.is_null(is_null=False)
        ):
            logger.debug(
                f'[ASSIGN] Testresult ID {testresult.testresult_id} assigned to {testresult.user.email} because of "{testresult.reason}"'
            )

            future = executor.submit(
                lambda x: testresult_run_ctlr.assign(
                    id=x.testresult_id,
                    assign_request_dto=allure.AssignRequestDto(username=x.user.email),
                ),
                testresult,
            )

            futures.append(future)

        for future in futures:
            if future is not None:
                future.result()
