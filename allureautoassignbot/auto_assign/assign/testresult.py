from concurrent.futures import ThreadPoolExecutor

import openapi_client as allure
from loguru import logger

from ..database import TestResult, User


def assign_testresults(testresult_run_ctlr: allure.TestResultRunControllerApi):
    logger.info("[ASSIGN] Assigning cases in Allure from calculated data in DB")

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []

        for testresult in TestResult.select().where(
            TestResult.user.is_null(is_null=False)
        ):
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

    for user_model in User.select():
        for reason in [
            "Team",
            "Product Functionality",
            "Direction",
            "left after all other reasons",
        ]:
            log_text = f'Assigned to {user_model.email} because of "{reason}":\n'

            query = TestResult.select().where(
                TestResult.user == user_model,
                TestResult.reason == reason,
            )

            if query.count() == 0:
                continue

            for testresult_model in query:
                log_text += f"Test result ID {testresult_model.testresult_id}\n"

            logger.debug(log_text)
