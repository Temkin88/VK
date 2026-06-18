import pytest
import allure

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("79823")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Создание оргединицы")
@allure.title("Создать оргединицу")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("unit_type", ["organization", "department"])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_unit_create(
    auth_account,
    default_org_id,
    default_unit,
    default_unit_id,
    default_subunit,
    unit_type,
    SANDBOX,
    photo_id,
):
    with allure.step("Пробуем создать оргединицу с различными типами"):
        response = default_unit

    assert response["status"]["code"] == 20000, "Response code error"
    assert response["results"]["unitId"], "Unit not created"

    with allure.step("Проверяем что оргединица создана"):
        assert auth_account.rapi_orgstructure_unit_list(
            orgstructureId=default_org_id,
            unit_id=default_unit_id,
            view=unit_type,
        )["results"]


@allure.id("79885")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Создание оргединицы")
@allure.title("Создать оргединицу c невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", [], {}, None, 123])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_unit_create_invalid_params(
    auth_account,
    invalid_params,
):
    with allure.step("Пробуем создать оргединицу с невалидными параметрам"), pytest.raises(BadRequestException):
        auth_account.rapi_orgstructure_admin_unit_create(
            name=invalid_params,
            parentId=invalid_params,
            _type=invalid_params,
            orgstructureId=invalid_params,
            lead=invalid_params,
            logo=invalid_params,
            domains=invalid_params,
        )
