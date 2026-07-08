import csv
import os
import time
from concurrent.futures import ThreadPoolExecutor

import openapi_client as allure

from loguru import logger
from bot.bot import Bot

from project.db import Defect


logger.add("logs/stats_{time}.log", level="DEBUG", colorize=True)

BOT_TOKEN = os.getenv("BOT_TOKEN")
ALLURE_TOKEN = os.getenv("ALLURE_TOKEN")

if BOT_TOKEN is None:
    raise ValueError("env BOT_TOKEN is None")

if ALLURE_TOKEN is None:
    raise ValueError("env ALLURE_TOKEN is None")

report_bot = Bot(
    api_url_base="https://api.internal.myteam.mail.ru/bot/v1",
    token=BOT_TOKEN
)


configuration = allure.Configuration()
configuration.verify_ssl = False


def process_defect(defect_row: allure.DefectCountRowDto):
    defect_overview = defect_ctlr.find_by_id3(id=defect_row.id)

    logger.info(f"Defect ID: {defect_overview.id}, name: {defect_overview.name}, issue: {defect_overview.issue}")

    defect_launch_overview = defect_ctlr.get_launches1(id=defect_row.id)
    defect_test_case_overview = defect_ctlr.get_test_cases1(id=defect_row.id)
    defect_test_result_overview = defect_ctlr.get_test_results1(id=defect_row.id)

    defect_model, created = Defect.get_or_create(
        id=defect_overview.id,
        project_id=defect_overview.project_id,
        name=defect_overview.name,
        issue=defect_overview.issue.name if defect_overview.issue is not None else None,
        launch_count=defect_launch_overview.total_elements,
        test_result_count=defect_test_result_overview.total_elements,
        test_case_count=defect_test_case_overview.total_elements
    )

    logger.info(f"Defect ID: {defect_overview.id}, model: {defect_model}, created: {created}")


def write_to_csv(data, filename):
    logger.info("Writing to csv: {} ...".format(filename))
    with open(filename, 'w', newline='') as out:
        csvOut = csv.writer(out)
        # column headers
        headers = ["name", "issue", "test cases", "test results", "launches"]
        csvOut.writerow(headers)

        # write data rows
        for row in data:
            csvOut.writerow(row)

    with open(filename, 'r') as f:

        response = report_bot.send_file(
            chat_id="702668@chat.agent",
            file=f,
            caption="Еженедельный отчет по дефектам"
        )

        logger.info(response.text)


with allure.ApiClient(
    configuration=configuration,
    header_name="Authorization",
    header_value=f"Api-Token {ALLURE_TOKEN}",
) as client:
    defect_ctlr = allure.DefectControllerApi(api_client=client)
    launch_ctlr = allure.LaunchControllerApi(api_client=client)
    test_result_ctlr = allure.TestResultControllerApi(api_client=client)

    with ThreadPoolExecutor(max_workers=20) as executer:

        for project_id in [6, 7, 8, 9, 10, 13, 14]:

            logger.info(f"Project ID: {project_id}")

            response = defect_ctlr.find_all_by_project_id(
                project_id=project_id,
                size=10000,
                status=["open"]
            )

            for result in executer.map(process_defect, response.content):
                continue

    data = Defect.select(
        Defect.name,
        Defect.issue,
        Defect.test_case_count,
        Defect.test_result_count,
        Defect.launch_count
    ).order_by(
        Defect.launch_count.desc()
    ).tuples()

    write_to_csv(data, f"allure_defect_stats_report_{time.time_ns()}.csv")
