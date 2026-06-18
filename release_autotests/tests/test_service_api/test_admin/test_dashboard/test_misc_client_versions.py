import allure

from support.markers import SANDBOX
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CORE_BACKEND)]


@allure.id("79680")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Раздел стартовой страницы")
@allure.title(
    "Текущие версии клиентов",
)
@SANDBOX
def test_api_misc_client_version(admin_account):
    with allure.step("Пробуем выполнить запрос"):
        admin_account.api_misc_client_versions()
