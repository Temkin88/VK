import allure

from support.markers import SANDBOX
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CORE_BACKEND)]


@allure.id("79678")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Раздел стартовой страницы")
@allure.title(
    "Документы и описание системы",
)
@SANDBOX
def test_api_dashboard(admin_account):
    with allure.step("Пробуем выполнить запрос"):
        response = admin_account.api_dashboard()
        assert "documents" in response["result"]
