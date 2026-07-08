import logging

import openapi_client as allure

from extract.testresult import (
    extract_testresults_with_pf,
    extract_testresults_without_pf,
)

logger = logging.getLogger(__name__)


def extract_testresults_from_launches(
    launch_ctlr: allure.LaunchControllerApi,
    testresult_tree_ctlr: allure.TestResultTreeControllerApi,
    launch_ids: list[int],
):
    logger.info("[EXTRACT] Extracting test results from launches")

    for launch_id in launch_ids:
        extract_launch(
            launch_ctlr=launch_ctlr,
            testresult_tree_ctlr=testresult_tree_ctlr,
            launch_id=launch_id,
        )


def get_project_cases_tree_id(project_id: int) -> int:
    if project_id == 10:
        return 579
    elif project_id == 6:
        return 578
    elif project_id == 9:
        return 580
    elif project_id == 13:
        return 581
    elif project_id == 7:
        return 577
    elif project_id == 14:
        return 582
    elif project_id == 8:
        return 583
    else:
        raise ValueError(f"Unknown project_id: {project_id}")


def extract_launch(
    launch_ctlr: allure.LaunchControllerApi,
    testresult_tree_ctlr: allure.TestResultTreeControllerApi,
    launch_id: int,
):
    launch_info = launch_ctlr.find_one20(id=launch_id)

    logger.debug(
        f'[EXTRACT] Extracting test results from launch ID {launch_info.id} "{launch_info.name}"'
    )

    tree_id = get_project_cases_tree_id(launch_info.project_id)

    extract_testresults_with_pf(
        testresult_tree_ctlr=testresult_tree_ctlr, launch_id=launch_id, tree_id=tree_id
    )

    extract_testresults_without_pf(
        testresult_tree_ctlr=testresult_tree_ctlr,
        launch_id=launch_id,
    )
