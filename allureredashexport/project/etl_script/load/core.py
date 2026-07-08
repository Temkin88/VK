from common.logger import logger
from common.db_schema import (
    TestCase,
    TestCaseLink,
    TestCaseStatus,
    TestCaseTag,
    TestCaseIssue,
    TestCaseWorkFlow,
    TestCaseCustomFieldValue
)


def load_data(result: dict[str, int | str | list[dict] | dict]):
    """
    Загрузка подготовленных данных о тест-кейсе в базу данных
    :param result: Подготовленные данные о тест-кейсе, его тегах/ссылка/статусе/workflow/cfv
    """

    logger.info(f'Loading data for case #{result["allure_id"]} "{result["name"]}"')

    status_model, _ = TestCaseStatus.get_or_create(**result["status"])
    workflow_model, _ = TestCaseWorkFlow.get_or_create(**result["workflow"])

    try:
        testcase_model, is_testcase_created = TestCase.get_or_create(
            project_id=result["project_id"],
            allure_id=result["allure_id"],
            automated=result["automated"],
            created_by=result["created_by"],
            created_date=result["created_date"],
            deleted=result["deleted"],
            name=result["name"],
            status=status_model,
            workflow=workflow_model,
            redash_date=result["redash_date"],
        )
    except Exception as error:
        logger.error("Skipping")
        logger.error(error)
        return

    logger.success(f'Test case created #{result["allure_id"]} in DB')

    for link in result["links"]:
        TestCaseLink.get_or_create(test_case=testcase_model, **link)

    logger.success(f'Test case links created #{result["allure_id"]} in DB')

    for tag in result["tags"]:
        tag_model, _ = TestCaseTag.get_or_create(**tag)

        if is_testcase_created:
            testcase_model.tags.add(tag_model)

    logger.success(f'Test case tags created #{result["allure_id"]} in DB')

    for cfv in result["cfv"]:
        cfv_model, _ = TestCaseCustomFieldValue.get_or_create(**cfv)

        if is_testcase_created:
            testcase_model.cfv.add(cfv_model)

    logger.success(f'Test case cfv values created #{result["allure_id"]} in DB')

    for issue in result["issues"]:
        issue_model, _ = TestCaseIssue.get_or_create(**issue)

        if is_testcase_created:
            testcase_model.issues.add(issue_model)

    logger.success(f'Test case issues created #{result["allure_id"]} in DB')
