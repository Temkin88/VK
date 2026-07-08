import math

import typer
import logging
import urllib3

import openapi_client as allure

from assign import assign_testresults
from database import User, TestResult
from extract import extract_testresults_from_launches
from process import (
    process_cases_by_team,
    process_cases_by_pf,
    process_cases_by_direction,
    process_all_lefted_cases,
    stat_user_assigned_testresult_count,
    check_if_unassigned_cases_left,
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)
app = typer.Typer()


@app.command()
def assign(token: str, launch_ids: list[int]):
    configuration = allure.Configuration()
    configuration.verify_ssl = False

    logger.info("[AllureAutoAssign] Starting pipeline")

    users_count = User.select().count()

    logger.info(f"[MATH] Users count: {users_count}")

    with allure.ApiClient(
        configuration=configuration,
        header_name="Authorization",
        # header_value="Api-Token f5aa95f7-50d2-48aa-bdbe-52854dc0ca3c",
        header_value=f"Api-Token {token}",
    ) as client:
        launch_ctlr = allure.LaunchControllerApi(api_client=client)
        testresult_tree_ctlr = allure.TestResultTreeControllerApi(api_client=client)
        testresult_run_ctlr = allure.TestResultRunControllerApi(api_client=client)

        extract_testresults_from_launches(
            launch_ctlr=launch_ctlr,
            testresult_tree_ctlr=testresult_tree_ctlr,
            launch_ids=launch_ids,
        )

        cases_count = TestResult.select().count()

        logger.info(f"[MATH] Cases count: {cases_count}")

        cases_per_user = math.ceil(cases_count / users_count)

        logger.info(f"[MATH] Cases per user: {cases_per_user}")

        process_cases_by_team(cases_per_user=cases_per_user)

        process_cases_by_pf(cases_per_user=cases_per_user)

        process_cases_by_direction(cases_per_user=cases_per_user)

        process_all_lefted_cases()

        stat_user_assigned_testresult_count()

        check_if_unassigned_cases_left()

        assign_testresults(testresult_run_ctlr=testresult_run_ctlr)

        logger.info("[FINISH] Success!")


if __name__ == "__main__":
    app()
