"""
Подготовленные запросы к базе данных
"""

from database import TestCase


pd_f_matrix_query = (
    TestCase.select(TestCase.product_functionality, TestCase.feature)
    .where(TestCase.jira.is_null())
    .group_by(TestCase.product_functionality, TestCase.feature)
)


def get_test_cases_by_f_pd(product_functionality: str, feature: str):
    """
    Получение списка тест кейсов по feature и product_functionality
    :param product_functionality: Product Functionality
    :param feature: Feature
    :return: Список кейсов из базы данных
    """
    return TestCase.select().where(
        TestCase.product_functionality == product_functionality,
        TestCase.feature == feature,
        TestCase.jira.is_null(),
    )
