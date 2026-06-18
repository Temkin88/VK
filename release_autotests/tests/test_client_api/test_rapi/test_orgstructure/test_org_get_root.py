import allure
import pytest

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("80588")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр корня оргструктуры")
@allure.title("Посмотреть корня оргструктуры: головная организация и ее дети")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_get_root(
    auth_account,
    default_org_id,
    default_unit_id,
    default_subunit_id,
):
    with allure.step("Пробуем привязать пользователя на должность"):
        response = auth_account.rapi_orgstructure_get_root(
            orgstructureId=default_org_id,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert response["results"]["unitId"] == default_unit_id


@allure.id("80587")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр корня оргструктуры")
@allure.title("Посмотреть корня оргструктуры с невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", {}, None, 123])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_get_root_invalid_params(
    auth_account,
    invalid_params,
):
    with (
        allure.step("Пробуем посмотреть корень оргструктуры с невалидными параметрами"),
        pytest.raises(BadRequestException),
    ):
        auth_account.rapi_orgstructure_get_root(
            orgstructureId=invalid_params,
        )
