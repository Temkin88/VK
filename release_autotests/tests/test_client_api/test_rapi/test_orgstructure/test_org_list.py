import allure
import pytest

from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("80589")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр списка созданных оргструктур")
@allure.title("Просмотр списка созданных оргструктур")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_list(
    auth_account,
):
    with allure.step("Пробуем получить список созданных оргструктур"):
        response = auth_account.rapi_orgstructure_list()
        assert response["status"]["code"] == 20000, "Response code error"
