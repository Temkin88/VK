import pytest
import allure

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("80583")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр списка дочерних элементов оргединицы")
@allure.title("Просматриваем список дочерних элементов оргединицы")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("view", ["organization", "department"])
@pytest.mark.second_to_last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_unit_subunits_get(
    auth_account,
    view,
    default_unit_id,
    default_subunit_id,
    photo_id,
    SANDBOX,
):
    with allure.step("Проверяем что можем просмтреть список дочерних элементов оргединицы"):
        response = auth_account.rapi_orgstructure_unit_subunits_get(
            unitId=default_unit_id if view == "organization" else default_subunit_id,
            view=view,
        )
        assert response["status"]["code"] == 20000, "Response code error"


@allure.id("80584")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр списка дочерних элементов оргединицы")
@allure.title("Просматриваем список дочерних элементов оргединицы с невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", [], {}, None, 123])
@pytest.mark.second_to_last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_unit_subunits_get_invalid_param(
    auth_account,
    invalid_params,
):
    with (
        allure.step("Пробуем просмотреть список дочерних элементов с невалидными параметрам"),
        pytest.raises(BadRequestException),
    ):
        auth_account.rapi_orgstructure_unit_subunits_get(
            unitId=invalid_params,
            view=invalid_params,
        )
