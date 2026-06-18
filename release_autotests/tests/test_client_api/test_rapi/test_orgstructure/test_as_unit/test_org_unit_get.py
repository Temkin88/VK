import pytest
import allure

from pyvkteamsclient.client.exceptions import BadRequestException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("80580")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр профиля оргединицы")
@allure.title("Просматриваем профиля оргединицы")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("withParents", [True, False])
@pytest.mark.second_to_last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_unit_get(
    auth_account,
    withParents,
    default_org_id,
    default_unit_id,
    default_subunit_id,
    SANDBOX,
):
    domains_list = [
        "autotest.clients",
        "corp.mail.ru",
        "vk.team",
        SANDBOX,
    ]

    results = {
        "orgstructureId": default_org_id,
        "parentId": default_unit_id,
        "unitId": default_subunit_id,
    }

    with allure.step("Пробуем просмотреть профиля оргединицы"):
        response = auth_account.rapi_orgstructure_unit_get(
            unitId=default_subunit_id,
            withParents=withParents,
        )
        assert response["status"]["code"] == 20000, "Response code error"
        assert "Test unit" in response["results"]["name"], "Test unit not in name"
        assert all(response["results"][key] == value for key, value in results.items()), "Id dont match"
        assert all(domain in domains_list for domain in response["results"]["domains"]), "Domain not in domains list"


@allure.id("80579")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Оргструктура")
@allure.feature("Просмотр профиля оргединицы")
@allure.title("Просматриваем профиля оргединицы с невалидными параметрам")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("invalid_params", ["", [], {}, None, 123])
@pytest.mark.second_to_last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_unit_get_invalid_params(
    auth_account,
    invalid_params,
):
    with (
        allure.step("Пробуем просмотреть профиль оргединицы с невалидными параметрам"),
        pytest.raises(BadRequestException),
    ):
        auth_account.rapi_orgstructure_unit_get(
            unitId=invalid_params,
            withParents=invalid_params,
        )
