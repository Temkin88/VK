from utils.config import configuration


def get_test_case_link(project_id: int | str, test_case_id: int | str) -> str:
    """
    Сборка ссылки на тест кейс в Allure TestOps
    :param project_id: ID проекта
    :param test_case_id: ID тест кейса
    :return: Ссылка на тест кейс
    """
    return configuration["allure.template.links"]["test_case"].format(
        project_id=project_id, test_case_id=test_case_id
    )
