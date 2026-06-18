import pytest
import allure

from datetime import datetime

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("79818")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Редактирование оргструктуры")
@allure.title("Редактировать оргструктуру")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("default", [True, False])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_edit(
    auth_account,
    default,
):
    with allure.step("Создаем оргструктуру"):
        org_id = auth_account.rapi_orgstructure_admin_create(
            name=f"Test unit {datetime.now()}",
        )["results"]["orgstructureId"]

    with allure.step("Редактируем оргструктуру"):
        org_name = f"Test unit {datetime.now()}"
        response = auth_account.rapi_orgstructure_admin_edit(
            name=org_name,
            orgstructureId=org_id,
            default=not default,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert response["results"]["name"] == org_name, "Response code error"
        assert response["results"]["orgstructureId"] == org_id, "Response code error"


@allure.id("79887")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Редактирование оргструктуры")
@allure.title("Редактировать оргструктуру с невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", [], {}, None, 123])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_edit_invalid_params(
    auth_account,
    invalid_params,
):
    with allure.step("Пробуем редактировать оргструктуру с невалидными параметрам"), pytest.raises(BadRequestException):
        auth_account.rapi_orgstructure_admin_edit(
            name=invalid_params,
            orgstructureId=invalid_params,
            default=not invalid_params,
        )
