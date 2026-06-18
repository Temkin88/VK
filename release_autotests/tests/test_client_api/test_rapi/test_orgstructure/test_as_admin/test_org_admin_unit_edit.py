import pytest
import allure

from datetime import datetime

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("79827")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Редактирование оргединицы")
@allure.title("Редактировать оргединицу")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_unit_edit(
    auth_account,
    photo_id,
    SANDBOX,
):
    org_id = auth_account.rapi_orgstructure_admin_create(
        name=f"Test unit {datetime.now()}",
    )["results"]["orgstructureId"]

    unit_id = auth_account.rapi_orgstructure_admin_unit_create(
        name=f"Test unit {datetime.now()}",
        parentId="",
        _type="organization",
        orgstructureId=org_id,
        description="Test description",
        lead=auth_account.uin,
        logo=photo_id,
        domains=[
            "autotest.clients",
            "corp.mail.ru",
            "vk.team",
            SANDBOX,
        ],
    )["results"]["unitId"]

    sub_unit_id = auth_account.rapi_orgstructure_admin_unit_create(
        name=f"Test unit {datetime.now()}",
        parentId=unit_id,
        _type="department",
        orgstructureId=org_id,
        lead=auth_account.uin,
        logo=photo_id,
        domains=[
            "autotest.clients",
            "corp.mail.ru",
            "vk.team",
            SANDBOX,
        ],
    )["results"]["unitId"]

    domains = [
        "autotest.clients",
        "corp.mail.ru",
        "vk.team",
        SANDBOX,
    ]

    results = {
        "name": f"Test unit edit {datetime.now()}",
        "description": f"Test descripion edit {datetime.now()}",
        "unitId": sub_unit_id,
        "parentId": unit_id,
        "orgstructureId": org_id,
    }

    with allure.step("Пробуем редактировать оргединицы"):
        response = auth_account.rapi_orgstructure_admin_unit_edit(
            unitId=results["unitId"],
            name=results["name"],
            description=results["description"],
            parentId=results["parentId"],
            orgstructureId=results["orgstructureId"],
            lead=auth_account.uin,
            logo=photo_id,
            domains=domains,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert all(response["results"][key] == value for key, value in results.items())
        assert all(domain in response["results"]["domains"] for domain in domains)

    with allure.step("Проверяем что извенения произошли"):
        response = auth_account.rapi_orgstructure_unit_get(
            unitId=sub_unit_id,
            withParents=True,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert all(response["results"][key] == value for key, value in results.items())
        assert all(domain in response["results"]["domains"] for domain in domains)


@allure.id("79892")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Редактирование оргединицы")
@allure.title("Редактировать оргединицу c невалидными параметрами")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", [], {}, None, 123])
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_unit_edit_invalid_params(
    auth_account,
    invalid_params,
):
    with allure.step("Пробуем редактировать оргструктуру с невалидными параметрам"), pytest.raises(BadRequestException):
        auth_account.rapi_orgstructure_admin_unit_edit(
            unitId=invalid_params,
            name=invalid_params,
            description=invalid_params,
            parentId=invalid_params,
            orgstructureId=invalid_params,
            lead=invalid_params,
            logo=invalid_params,
            domains=invalid_params,
        )
