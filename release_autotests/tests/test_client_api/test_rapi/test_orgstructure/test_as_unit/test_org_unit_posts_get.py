import uuid

import pytest
import allure

from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("483209")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр штатных единиц юнита")
@allure.title("Просмотриваем штатную единицу юнита")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.second_to_last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_unit_posts_get(
    auth_account,
    default_unit_id,
    default_post_id,
    SANDBOX,
):
    with allure.step("Пробуем создать должность"):
        response = auth_account.rapi_orgstructure_admin_post_create(
            name=f"Test unit {uuid.uuid4().hex}",
            unitId=default_unit_id,
        )
        post_id = response["results"]["postId"]
        assert response["status"]["code"] == 20000, "Response code error"

    with allure.step("Пробуем просмотреть профиля оргединицы"):
        response = auth_account.rapi_orgstructure_unit_posts_get(
            unitId=default_unit_id,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert all(post["postId"] == post_id for post in response["results"]), "Post id dont match"
        assert all("Test unit" in post["postName"] for post in response["results"]), "Test unit not in post name"
