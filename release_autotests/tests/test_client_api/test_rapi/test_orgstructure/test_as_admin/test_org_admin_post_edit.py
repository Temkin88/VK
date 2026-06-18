import pytest
import allure

from datetime import datetime

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


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
@pytest.mark.skip("Доделать когда устранят баг в ручке rapi/orgstructure/admin/post/edit. IMSERVER-19501")
def test_org_admin_post_edit(
    auth_account,
    default_unit_id,
):
    with allure.step("Пробуем создать должность"):
        post_name = f"Test unit {datetime.now()}"
        response = auth_account.rapi_orgstructure_admin_post_create(
            name=post_name,
            unitId=default_unit_id,
        )
        post_id = response["results"]["postId"]
        assert response["status"]["code"] == 20000, "Response code error"
        assert response["results"]["postId"], "Post not created"

    with allure.step("Пробуем изменить должность"):
        response = auth_account.rapi_orgstructure_admin_post_edit(
            name=f"Test unit {datetime.now()}",
            unitId=default_unit_id,
            postId=post_id,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert response["results"]["postId"], "Post not created"

    with allure.step("Проверяем изменилась ли должность"):
        auth_account.rapi_orgstructure_unit_posts_get(unitId=default_unit_id)


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
@pytest.mark.skip("Доделать когда устранят баг в ручке rapi/orgstructure/admin/post/edit. IMSERVER-19501")
def test_org_admin_post_edit_invalid_params(
    auth_account,
    invalid_params,
):
    with allure.step("Пробуем создать должность с невалидными параметрам"), pytest.raises(BadRequestException):
        auth_account.rapi_orgstructure_admin_post_edit(
            name=invalid_params,
            unitId=invalid_params,
        )
