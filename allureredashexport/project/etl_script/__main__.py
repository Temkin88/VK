import os

import openapi_client as allure

from common.logger import logger

from project.etl_script.extract import extract_data
from project.etl_script.transform import transform_data
from project.etl_script.load import load_data


ALLURE_TOKEN = os.getenv('ALLURE_TOKEN')

if ALLURE_TOKEN is None:
    raise ValueError('ALLURE_TOKEN is not defined in env')

PROJECT_IDS = os.getenv('PROJECT_IDS')

if PROJECT_IDS is None:
    raise ValueError('PROJECT_IDS is not defined in env')


PROJECT_IDS = [int(i) for i in PROJECT_IDS.split(',')]


if __name__ == "__main__":
    logger.success("Pipeline started")

    configuration = allure.Configuration()
    configuration.verify_ssl = False

    with allure.ApiClient(
            configuration=configuration,
            header_name="Authorization",
            header_value=f"Api-Token {ALLURE_TOKEN}",
    ) as client:
        pass

        testcase_ctlr = allure.TestCaseControllerApi(api_client=client)
        testcase_issue_ctlr = allure.TestCaseIssueControllerApi(api_client=client)
        testcase_tree_ctlr = allure.TestCaseTreeControllerApi(api_client=client)
        testcase_cfv_ctlr = allure.TestCaseCustomFieldControllerApi(api_client=client)

        for project_id in PROJECT_IDS:
            logger.info(f'Starting process for project ID {project_id}')
            for case, issues, cfv_values in extract_data(
                    project_id=project_id,
                    testcase_ctlr=testcase_ctlr,
                    testcase_issue_ctlr=testcase_issue_ctlr,
                    testcase_tree_ctlr=testcase_tree_ctlr,
                    testcase_cfv_ctlr=testcase_cfv_ctlr
            ):
                result = transform_data(case, issues, cfv_values)
                load_data(result)
