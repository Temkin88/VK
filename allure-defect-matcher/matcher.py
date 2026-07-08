from requests import Session

from loguru import logger


logger.add(
    "logs/file_{time}.log"
)


with Session() as client:
    client.headers = {
            "Authorization": "Api-Token {token}".format(
                token="f5aa95f7-50d2-48aa-bdbe-52854dc0ca3c"
            ),
    }

    results = set()

    for project_id in (6, 7, 8, 9, 10, 13, 14, 28):

        logger.info(f'Starting with project ID {project_id}')

        defects_json = client.get('https://allure.vk.team/api/rs/defect', params={
            'projectId': project_id,
            'size': 5
        }).json()
        for page in range(defects_json['totalPages'] + 1):
            logger.info(f'Page #{page}/{defects_json["totalPages"]}')
            for defect in client.get('https://allure.vk.team/api/rs/defect', params={
                'projectId': project_id,
                'size': 5,
                'page': page
            }).json().get('content', []):
                logger.info('Defect ID {id} {name}'.format(**defect))
                for testresult in client.get(
                        url=f'https://allure.vk.team/api/rs/defect/{defect["id"]}/testresult',
                        params={
                            'size': 50,
                        }
                ).json().get('content', []):
                    if f'{testresult["testCaseId"]}:{defect["id"]}' not in results:
                        logger.info('Testresult ID {id} {name}, caseId {testCaseId}'.format(**testresult))
                        logger.info(f'https://allure.vk.team/api/rs/testcase/{testresult["testCaseId"]}/defect/{defect["id"]}')
                        response = client.post(f'https://allure.vk.team/api/rs/testcase/{testresult["testCaseId"]}/defect/{defect["id"]}')
                        logger.info(f'{response.status_code} {response.reason} - {response.text}')
                        results.add(f'{testresult["testCaseId"]}:{defect["id"]}')
            logger.info('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

