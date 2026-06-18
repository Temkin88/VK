import pytest
import allure

from datetime import datetime

from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("79873")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Удаление должности (штатной единицы)")
@allure.title("Удалить должность (штатную единицу)")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_post_delete(
    auth_account,
    default_unit_id,
):
    with allure.step("Пробуем создать должность"):
        post_id = auth_account.rapi_orgstructure_admin_post_create(
            name=f"Test unit {datetime.now()}",
            unitId=default_unit_id,
        )["results"]["postId"]

    with allure.step("Пробуем удалить должность"):
        auth_account.rapi_orgstructure_admin_post_delete(postId=post_id)
