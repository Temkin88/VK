import allure
import pytest

from pyvkteamsclient.client.exceptions import OrgstructureException
from support.markers import SANDBOX, PRE_TARM, TARM, SAAS, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.ORGSTRUCTURE)]


@allure.id("79901")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Оргструктура")
@allure.feature("Загрузка подразделений в формате excel")
@allure.title("Загрузка дочерних подразделений организации в формате excel")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_unit_excel(
    auth_account,
    default_unit_id,
    excel_id_positive,
):
    with allure.step("Пытаемся загрузить подразделение в формате excel"):
        assert (
            auth_account.rapi_orgstructure_admin_unit_excel(
                unitId=default_unit_id,
                fileId=excel_id_positive,
            )["status"]["code"]
            == 20000
        )


@allure.id("80578")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Оргструктура")
@allure.feature("Загрузка подразделений в формате excel")
@allure.title("Загрузка дочерних подразделений организации в формате excel без обязательных полей")
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.last
@pytest.mark.xdist_group(name="orgstructure")
def test_org_admin_unit_excel_not_existent(
    auth_account,
    default_unit_id,
    excel_id_negative,
):
    with (
        allure.step("Пытаемся загрузить подразделение в формате excel без обязательных полей"),
        pytest.raises(OrgstructureException),
    ):
        auth_account.rapi_orgstructure_admin_unit_excel(
            unitId=default_unit_id,
            fileId=excel_id_negative,
        )
