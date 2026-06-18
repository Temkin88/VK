import pytest
import allure

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("79895")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Удаление оргединицы")
@allure.title("Удалить оргединицу")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_unit_delete(
    auth_account,
    default_unit_id,
):
    with allure.step("Пробуем редактировать оргединицы"):
        response = auth_account.rapi_orgstructure_admin_unit_delete(
            unitId=default_unit_id,
        )
        assert response["status"]["code"] == 20000, "Response code error"


@allure.id("79888")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Удаление оргединицы")
@allure.title("Удалить оргединицу c невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", [], {}, None, 123])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_unit_delete_invalid_params(
    auth_account,
    invalid_params,
):
    with allure.step("Пробуем удалить оргструктуру с невалидными параметрам"), pytest.raises(BadRequestException):
        auth_account.rapi_orgstructure_admin_unit_delete(
            unitId=invalid_params,
        )
