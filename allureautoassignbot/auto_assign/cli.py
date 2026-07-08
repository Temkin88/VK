import math
import urllib3

import openapi_client as allure
from loguru import logger
from pyvkteamsbot.bot.bot import Bot

from auto_assign.assign import assign_testresults
from auto_assign.database import User, TestResult
from auto_assign.extract import extract_testresults_from_launches
from auto_assign.process import (
    process_cases_by_team,
    process_cases_by_pf,
    process_cases_by_direction,
    process_all_lefted_cases,
    stat_user_assigned_testresult_count,
    check_if_unassigned_cases_left,
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def assign(
    launch_ids: list[int],
    bot: Bot,
    chat_id: str,
    msg_id: str | int,
    launch_ctlr: allure.LaunchControllerApi,
    testresult_tree_ctlr: allure.TestResultTreeControllerApi,
    testresult_run_ctlr: allure.TestResultRunControllerApi,
):
    configuration = allure.Configuration()
    configuration.verify_ssl = False

    stage_name = "[AllureAutoAssign] Starting pipeline"
    logger.info(stage_name)
    bot.edit_text(chat_id=chat_id, msg_id=msg_id, text=stage_name)

    users_count = User.select().count()

    stage_name = f"[MATH] Users count: {users_count}"
    logger.info(stage_name)
    bot.edit_text(chat_id=chat_id, msg_id=msg_id, text=stage_name)

    extract_testresults_from_launches(
        launch_ctlr=launch_ctlr,
        testresult_tree_ctlr=testresult_tree_ctlr,
        launch_ids=launch_ids,
    )

    cases_count = TestResult.select().count()

    stage_name = f"[MATH] Cases to assign count: {cases_count}"
    logger.info(stage_name)
    bot.edit_text(chat_id=chat_id, msg_id=msg_id, text=stage_name)

    cases_per_user = int(cases_count / users_count)

    if cases_per_user % 1 != 0:
        min_cases_per_user = int(cases_per_user)
        max_cases_per_user = math.ceil(cases_per_user)

        string_cases_per_user = f"{min_cases_per_user}-{max_cases_per_user}"
    else:
        string_cases_per_user = str(cases_per_user)

    stage_name = f"[MATH] Cases to assign per user: ~ {string_cases_per_user}"
    logger.info(stage_name)
    bot.edit_text(chat_id=chat_id, msg_id=msg_id, text=stage_name)

    process_cases_by_team(cases_per_user=cases_per_user)

    process_cases_by_pf(cases_per_user=cases_per_user)

    process_cases_by_direction(cases_per_user=cases_per_user)

    process_all_lefted_cases()

    stat_user_assigned_testresult_count()

    check_if_unassigned_cases_left()

    assign_testresults(testresult_run_ctlr=testresult_run_ctlr)

    stage_name = "[FINISH] Success!"
    logger.info(stage_name)
    bot.edit_text(chat_id=chat_id, msg_id=msg_id, text=stage_name)
