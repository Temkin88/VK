import pytest
import allure

from datetime import datetime

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("79899")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Создание должности (штатной единицы)")
@allure.title("Создать должность (штатную единицу) и добавить ее к существующей оргединице")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_post_create(
    auth_account,
    default_unit_id,
):
    with allure.step("Пробуем создать должность"):
        response = auth_account.rapi_orgstructure_admin_post_create(
            name=f"Test unit {datetime.now()}",
            unitId=default_unit_id,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert response["results"]["postId"], "Post not created"


@allure.id("79900")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Создание должности (штатной единицы)")
@allure.title("Создать должность (штатную единицу) с невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", [[], {}, None, 123])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_post_create_invalid_params(
    auth_account,
    invalid_params,
):
    with allure.step("Пробуем создать должность с невалидными параметрам"), pytest.raises(BadRequestException):
        auth_account.rapi_orgstructure_admin_post_create(
            name=invalid_params,
            unitId=invalid_params,
        )
