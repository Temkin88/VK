import pytest
import allure

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("79890")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Привязка пользователя")
@allure.title("Привязка пользователя на должность в рамках оргединицы")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.second_to_last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_user_link(
    auth_account,
    default_post_id,
):
    with allure.step("Пробуем привязать пользователя на должность"):
        response = auth_account.rapi_orgstructure_admin_user_link(
            email=auth_account.uin,
            postId=default_post_id,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert response["results"]["email"] == auth_account.uin, "email not found"


@allure.id("79884")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Привязка пользователя")
@allure.title("Привязка пользователя на должность с невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", [], {}, None, 123])
@pytest.mark.second_to_last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_user_link_invalid_params(
    auth_account,
    invalid_params,
):
    with allure.step("Пробуем привязать пользователя с невалидными параметрам"), pytest.raises(BadRequestException):
        auth_account.rapi_orgstructure_admin_user_link(
            email=invalid_params,
            postId=invalid_params,
        )
