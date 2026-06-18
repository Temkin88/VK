import allure
import pytest

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("80593")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Получение информации о сотрудниках")
@allure.title("Получение информации о нахождении сотрудников в оргструктуре")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_users_get(
    auth_account,
    default_unit_id,
):
    with allure.step("Пробуем привязать пользователя на должность"):
        response = auth_account.rapi_orgstructure_users_get(
            emails=[auth_account.uin],
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert response["results"][0]["email"] == auth_account.uin, "email not found"


@allure.id("80592")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Получение информации о сотрудниках")
@allure.title("Получение информации о нахождении сотрудников в оргструктуре с невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", {}, None, 123])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_users_get_invalid_params(
    auth_account,
    invalid_params,
):
    with (
        allure.step("Пробуем получить информацию о сотрудниках с невалидными параметрам"),
        pytest.raises(BadRequestException),
    ):
        auth_account.rapi_orgstructure_users_get(
            emails=invalid_params,
        )
