from datetime import datetime

import allure

from support.markers import SANDBOX
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CORE_BACKEND)]


@allure.id("95596")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Аналитика")
@allure.title("Получение метрик по ее названию")
@SANDBOX
def test_api_analytics_metric_name(
    admin_account,
):
    """
    Получаем метрику по ее названию
    :param admin_account: аккаунт с правами администратора
    """
    with allure.step("Пробуем получить метрикe по ее названию"):
        admin_account.api_analytics_metric_name(
            metric_name="",
            start=int(datetime.now().timestamp()),
            step=1,
        )
