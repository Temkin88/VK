"""
Работа с базой кейсов
"""

from database import pd_f_matrix_query


def get_pd_f_matrix() -> list[tuple[str, str]]:
    """
    Получение матрицы product_functionality X feature
    :return:
    """
    return [
        (model.product_functionality, model.feature)
        for model in pd_f_matrix_query
    ]
