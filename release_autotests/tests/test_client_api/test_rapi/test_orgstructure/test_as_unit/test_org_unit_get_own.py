import pytest
import allure

from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("483211")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр информации о моем юните")
@allure.title("Просмотриваем информацию о своем юните")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("view", ["organization", "department"])
@pytest.mark.second
@pytest.mark.xdist_group(name="orgstructure")
def test_org_unit_get_own(
    auth_account, view, default_org_id, default_unit_id, default_subunit_id, default_post_id, SANDBOX
):
    domains_list = [
        "autotest.clients",
        "corp.mail.ru",
        "vk.team",
        SANDBOX,
    ]
    results = {"orgstructureId": default_org_id}

    if view == "organization":
        results["unitId"] = default_unit_id
    else:
        results["parentId"] = default_unit_id
        results["unitId"] = default_subunit_id

    with allure.step("Пробуем привязать пользователя на должность"):
        response = auth_account.rapi_orgstructure_admin_user_link(
            email=auth_account.uin,
            postId=default_post_id,
        )
        assert response["status"]["code"] == 20000, "Response code error"

    with allure.step("Пробуем просмотреть список созданных ОЕ"):
        response = auth_account.rapi_orgstructure_unit_get_own(
            orgstructure_id=default_org_id,
            view=view,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert "Test unit" in response["results"]["name"], "Test unit not in name"
        assert all(response["results"][key] == value for key, value in results.items()), "Id dont match"
        assert all(domain in domains_list for domain in response["results"]["domains"]), "Domain not in domains list"
