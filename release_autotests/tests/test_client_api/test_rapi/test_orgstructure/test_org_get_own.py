import time
from datetime import datetime

import allure
import pytest

from pyvkteamsclient.client.exceptions import OrgstructureException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("80577")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр моей оргструктуры")
@allure.title("Посмотреть дерево оргструктуры. Возможно выбрать вид: дерево подразделений, дерево организаций")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.second_to_last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_get_own(
    auth_account,
    default_org_id,
    default_subunit_id,
    default_post_id,
):
    with allure.step("Пробуем привязать пользователя на должность"):
        try:
            response = auth_account.rapi_orgstructure_admin_user_link(
                email=auth_account.uin,
                postId=default_post_id,
            )
            assert response["status"]["code"] == 20000, "Response code error"
            assert response["results"]["email"] == auth_account.uin, "email not found"
        except Exception as error:
            if error.response_status_text != "post already linked to user":
                raise error

    with allure.step("Пробуем получить дерево оргструктуры"):
        response = auth_account.rapi_orgstructure_get_own(
            orgstructureId=default_org_id,
            view="department",
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert default_subunit_id in [unit["unitId"] for unit in response["results"]["subunits"]]
        assert all("Test unit" in name["name"] for name in response["results"]["subunits"])


@allure.id("80598")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр моей оргструктуры")
@allure.title("Посмотреть дерево оргструктуры. без привязки пользователя")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("view", ["organization", "department"])
@pytest.mark.second_to_last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_get_own_without_user_binding(
    auth_account,
    view,
):
    org_name = f"Test unit {datetime.now()}"

    with allure.step("Пробуем создать оргструктуру"):
        response = auth_account.rapi_orgstructure_admin_create(
            name=org_name,
        )

        for i in range(5):
            time.sleep(i)

            with allure.step("Проверяем, что оргструктура создана"):
                org_list = auth_account.rapi_orgstructure_list()["results"][-1]["orgstructureId"]

                if org_list == response["results"]["orgstructureId"]:
                    break

    with allure.step("Пробуем получить дерево без привязки пользователя"), pytest.raises(OrgstructureException):
        auth_account.rapi_orgstructure_get_own(
            orgstructureId=response["results"]["orgstructureId"],
            view=view,
        )

    with allure.step("Удаляем оргструктуру"):
        auth_account.rapi_orgstructure_admin_delete(
            orgstructureId=response["results"]["orgstructureId"],
        )
