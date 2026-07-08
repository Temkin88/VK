from loguru import logger  # noqa: D100

import openapi_client as allure


def create_allure_comment(
    comment_controller: allure.CommentControllerApi,
    test_case: allure.TestCaseOverviewDto,
    **kwargs: bool,
):
    """
    Создание комментария в Allure TestOps
    :param comment_controller: API Controller
    :param test_case: тест кейс
    :param kwargs: список полей у кейса
    :return:
    """
    with logger.contextualize(
        project_id=test_case.project_id, test_case_id=test_case.id
    ):
        logger.debug("Trying to create comment for test case")

        text = "Требуется добавить тест-кейсу следующие поля:\n"

        for key, value in kwargs.items():
            if not value:
                text += key + "\n"

        logger.debug(text.strip())

        comment_controller.create41_with_http_info(
            comment_create_dto=allure.CommentCreateDto(
                test_case_id=test_case.id, body=text.strip()
            )
        )

        logger.success("Comment successfully created")
