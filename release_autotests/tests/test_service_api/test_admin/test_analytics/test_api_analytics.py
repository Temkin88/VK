import allure

from support.markers import SANDBOX
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CORE_BACKEND)]


@allure.id("28781")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Аналитика")
@allure.title(
    "Получение групп метрик",
)
@SANDBOX
def test_api_analytics(admin_account):
    with allure.step("Пробуем получить список метрик"):
        admin_account.api_analytics()
