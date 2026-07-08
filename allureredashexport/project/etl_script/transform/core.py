from datetime import datetime

import openapi_client as allure

from common.logger import logger


def transform_data(
        case: allure.TestCaseDto,
        issues: list[allure.IssueDto],
        cfv_values: list[allure.CustomFieldValueDto]
) -> dict[str, int | str | list[dict] | dict]:
    """
    Преобразование DTO в словарь для загрузки моделей в базу данных
    :param case: DTO тест-кейса
    :param issues: DTO Jira-задач
    :param cfv_values: список DTO значений его custom field's
    :returns: dict с данными для загрузки в базу данных
    """

    logger.info(f'Transforming data for case #{case.id} "{case.name}"')

    return {
        "project_id": case.project_id,
        "allure_id": case.id,
        "automated": case.automated,
        "created_by": case.created_by,
        "created_date": datetime.fromtimestamp(case.created_date / 1000),
        "deleted": case.deleted,
        "name": case.name,
        "status": {
            "allure_id": case.status.id,
            "name": case.status.name,
        },
        "issues": [
            {
                "allure_id": issue.id,
                "name": issue.name,
                "url": issue.url,
                "closed": issue.closed
            } for issue in issues
        ],
        "workflow": {
            "allure_id": case.workflow.id,
            "name": case.workflow.name,
        },
        "links": [
            {
                "name": link.name,
                "type": link.type or 'url',
                "url": link.url,
            } for link in case.links
        ],
        "tags": [
            {
                "allure_id": tag.id,
                "name": tag.name,
            } for tag in case.tags
        ],
        "cfv": [
            {
                "allure_id": cfv.custom_field.id,
                "name": cfv.custom_field.name,
                "value": cfv.name
            } for cfv in cfv_values
        ],
        "redash_date": datetime.now().date()
    }
