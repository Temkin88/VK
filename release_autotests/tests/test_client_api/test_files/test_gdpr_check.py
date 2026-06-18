import allure
import pytest

from support.markers import SAAS, PRE_SAAS


@allure.id("37505")
@allure.label("layer", "api_layer")
@allure.label("jira", "IMQA-1105")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("GDPR")
@allure.title("Получение информации о доступности GDPR отчета для скачивания")
@SAAS
@PRE_SAAS
@pytest.mark.skip("IMQA-1105")
def test_gdpr_check(
    auth_account,
):
    with allure.step("Пробуем сделать запрос"):
        auth_account.files_gdpr_check(auth_account.uin)
