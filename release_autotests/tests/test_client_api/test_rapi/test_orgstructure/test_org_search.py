import allure
import pytest

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("80591")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Поиск по оргструктуре")
@allure.title("Поиск по юнитам и людям в оргструктуре")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_search(
    auth_account,
    default_org_id,
    default_subunit_id,
):
    with allure.step("Пробуем найти пользователей"):
        response = auth_account.rapi_orgstructure_search(
            search="autotest",
            orgstructureId=default_org_id,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert all("autotest" in user["email"] for user in response["results"]["users"])

    with allure.step("Пробуем найти units"):
        response = auth_account.rapi_orgstructure_search(
            search="Test unit",
            orgstructureId=default_org_id,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert all("Test unit" in user["name"] for user in response["results"]["units"])


@allure.id("80590")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Поиск по оргструктуре")
@allure.title("Поиск по юнитам и людям в оргструктуре с невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", {}, None, 123])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_get_own_invalid_params(
    auth_account,
    invalid_params,
):
    with allure.step("Пробуем найти по оргструктуре с невалидными параметрами"), pytest.raises(BadRequestException):
        auth_account.rapi_orgstructure_search(
            search=invalid_params,
            orgstructureId=invalid_params,
        )
