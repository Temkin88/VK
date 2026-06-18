import allure
import pytest

from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("483210")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Отфильтровать оргструктуру")
@allure.title("Отфильтровываем оргструктуру")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_filter(
    auth_account,
    default_unit_id,
):
    with allure.step("Пробуем найти пользователей"):
        response = auth_account.rapi_orgstructure_filter(
            unitId=default_unit_id,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert auth_account.uin == response["results"]["organization"]["lead"]["email"], (
            f"{auth_account.uin} dont match"
        )
        assert "Test unit" in response["results"]["organization"]["name"], "Test unit not in name"
        assert default_unit_id == response["results"]["organization"]["unitId"], f"{default_unit_id} dont match"
