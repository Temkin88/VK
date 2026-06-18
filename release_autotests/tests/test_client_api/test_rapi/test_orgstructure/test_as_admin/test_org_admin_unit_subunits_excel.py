import pytest
import allure

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("79832")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Оргструктура")
@allure.feature("Выгрузка подразделений в формате excel")
@allure.title("Выгрузить подразделение в формате excel")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_unit_subunits_excel(
    default_unit_id,
    auth_account,
    SANDBOX,
    photo_id,
):
    with allure.step("Пытаемся загрузить подразделение в формате excel"):
        auth_account.rapi_orgstructure_admin_unit_subunits_excel(
            unitId=default_unit_id,
        )


@allure.id("79831")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Оргструктура")
@allure.feature("Выгрузить подразделение в формате excel")
@allure.title("Выгружаем подразделение в формате excel с невадидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_param", ["", 12345, [], {}, None])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_unit_subunits_excel_not_existent(
    auth_account,
    invalid_param,
):
    with allure.step("Пробуем выгрузить excel с невалидными параметрами"), pytest.raises(BadRequestException):
        auth_account.rapi_orgstructure_admin_unit_subunits_excel(unitId=invalid_param)
