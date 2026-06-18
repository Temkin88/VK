import pytest
import allure

from datetime import datetime

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("79815")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Удаление оргструктуры")
@allure.title("Удалить оргструктуру")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("default", [True, False])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_delete(
    auth_account,
    default,
):
    with allure.step("Создаем оргструктуру"):
        org_id = auth_account.rapi_orgstructure_admin_create(
            name=f"Test unit {datetime.now()}",
        )["results"]["orgstructureId"]

    with allure.step("Пробуем удалить оргструктуру"):
        assert (
            auth_account.rapi_orgstructure_admin_delete(
                orgstructureId=org_id,
            )["status"]["code"]
            == 20000
        ), "Response code error"


@allure.id("79894")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Удаление оргструктуры")
@allure.title("Удалить оргструктуру с невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", [], {}, None, 123])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_delete_invalid_params(
    auth_account,
    invalid_params,
):
    with allure.step("Пробуем удалить оргструктуру с невалидными параметрам"), pytest.raises(BadRequestException):
        auth_account.rapi_orgstructure_admin_delete(
            orgstructureId=invalid_params,
        )
