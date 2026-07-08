#!/usr/bin/env python
import json
import logging
import time

import typer
from requests import Session


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def is_launch_finished(allure_launch_id) -> bool:

    launch_jobs_info = session.get(
        url=f'https://allure.vkteam.ru/api/rs/launch/{allure_launch_id}/job'
    ).json()

    common_result = sum(map(lambda x: x['stage'] in ['run_failure', 'finished'], launch_jobs_info))

    return common_result == len(launch_jobs_info)


def launch_name(ALLURE_LAUNCH_ID) -> str:

    launch_info = session.get(
        url=f'https://allure.vkteam.ru/api/rs/launch/{ALLURE_LAUNCH_ID}'
    ).json()

    return launch_info['name']


def launch_stats(allure_launch_id: int) -> dict:


    sorted_results = {}
    total_count = 0
    for i in range(3):
        results = session.get(
            url=f'https://allure.vkteam.ru/api/rs/launch/{allure_launch_id}/statistic'
        )
        if results.status_code == 200:
            logger.info(f'[DEBUG] Allure response code: {results.status_code}')
            logger.info(f'[DEBUG] Launch "{allure_launch_id}" successfully fetched')
            for batch in results.json():
                sorted_results[batch['status']] = batch['count']
                total_count += batch['count']
            break
        else:
            logger.info(f'[DEBUG] Allure response code: {results.status_code}')
            time.sleep(5)

    sorted_results['total'] = total_count
    logger.info(f'[DEBUG] Launch "{allure_launch_id}" has results: {sorted_results}')

    return sorted_results


def unresolved_results_text(allure_launch_id: int, allure_token: str, report_path: str = 'allure-report.json'):
    session.headers = {
        'Authorization': f'Api-Token {allure_token}'
    }

    IS_LAUNCH_FAILED = False

    allure_launch_name = launch_name(allure_launch_id)

    while not is_launch_finished(allure_launch_id):
        logger.info(f'Waiting for launch ID {allure_launch_id} "{allure_launch_name}" to be finished ...')
        time.sleep(5)

    logger.info(f'Launch "{allure_launch_name}" is finished, fetching results')

    time.sleep(15)

    launch_final_stats = launch_stats(allure_launch_id)

    if (launch_final_stats.get('broken', 0) + launch_final_stats.get('failed', 0)) / launch_final_stats['total'] >= 0.5:
        results = {
            'report': 'Слишком много ошибок, проверьте лаунч вручную'
        }
        logger.info(f'Seems like there are too many fails due to infrastrusture problems, check report in Allure TestOps https://allure.vkteam.ru/launch/{allure_launch_id}')
        IS_LAUNCH_FAILED = True

    else:
        unresolved_results = session.get(
            url=f'https://allure.vkteam.ru/api/rs/launch/{allure_launch_id}/unresolved'
        ).json()

        unresolved_results = unresolved_results["content"]

        failed_tests = list(filter(lambda x: x['status'] == 'failed', unresolved_results))
        broken_tests = list(filter(lambda x: x['status'] == 'broken', unresolved_results))

        results = {
            "failed": {
                "content": failed_tests,
                "count": len(failed_tests)
            },
            "broken": {
                "content": broken_tests,
                "count": len(broken_tests)
            },
            "total_count": len(unresolved_results)
        }

        if len(unresolved_results):

            text = ''

            for kind in ('failed', 'broken'):

                tests_list = failed_tests if kind == 'failed' else broken_tests

                if len(tests_list) == 0:
                    continue

                text += f'Тесты со статусом "{kind}":\n'
                text += '\n'.join(map(lambda x: x['name'], tests_list))
                text += '\n\n'

            results['report'] = text

            IS_LAUNCH_FAILED = True
            logger.info(f'Looks like there are unresolved results in report, check full report in Allure TestOps https://allure.vkteam.ru/launch/{allure_launch_id}')

        else:

            results['report'] = 'Упавших тестов нет :)'

    with open(report_path, 'w') as f:
        json.dump(results, f)

    logger.info(f'Report saved to {report_path}, check it!')

    if IS_LAUNCH_FAILED:
        exit(-1)


if __name__ == "__main__":
    with Session() as session:
        typer.run(unresolved_results_text)
