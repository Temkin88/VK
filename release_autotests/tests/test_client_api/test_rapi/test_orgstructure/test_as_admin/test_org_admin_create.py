import pytest
import allure

from datetime import datetime

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("79819")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Создание оргструктуры")
@allure.title("Создать оргструктуру")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("default", [True, False])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_create(
    auth_account,
    default,
):
    with allure.step("Пробуем  создать оргструктуру"):
        response = auth_account.rapi_orgstructure_admin_create(
            name=f"Test unit {datetime.now()}",
            default=default,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert response["results"]["orgstructureId"], "Org structure not created"


@allure.id("79893")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Создание оргструктуры")
@allure.title("Создать оргструктуру с невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", [], {}, None, 123])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_create_invalid_params(
    auth_account,
    invalid_params,
):
    with allure.step("Пробуем создать оргструктуру с невалидными параметрам"), pytest.raises(BadRequestException):
        auth_account.rapi_orgstructure_admin_create(
            name=f"Test unit {datetime.now()}",
            default=invalid_params,
        )
