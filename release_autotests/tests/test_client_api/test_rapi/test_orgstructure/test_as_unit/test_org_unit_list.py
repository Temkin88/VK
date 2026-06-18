import pytest
import allure

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("80581")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр списка созданных ОЕ")
@allure.title("Просматриваем список созданных ОЕ")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("view", ["organization", "department"])
@pytest.mark.second_to_last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_unit_list(
    auth_account,
    view,
    default_org_id,
    default_unit_id,
    default_subunit_id,
):
    with allure.step("Пробуем просмотреть список созданных ОЕ"):
        response = auth_account.rapi_orgstructure_unit_list(
            orgstructureId=default_org_id,
            unit_id=default_unit_id,
            view=view,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert all(
            default_unit_id in event["unitId"] or default_subunit_id in event["unitId"] for event in response["results"]
        ), "Unit id dont match"


@allure.id("80582")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр списка созданных ОЕ")
@allure.title("Просматриваем список созданных ОЕ с невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", [], {}, None, 123])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_unit_list_invalid_params(
    auth_account,
    invalid_params,
):
    with (
        allure.step("Пробуем просмотреть список созданных ОЕ с невалидными параметрам"),
        pytest.raises(BadRequestException),
    ):
        auth_account.rapi_orgstructure_unit_list(
            orgstructureId=invalid_params,
            view=invalid_params,
        )
