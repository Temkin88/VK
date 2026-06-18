import allure

from support.markers import SAAS, PRE_SAAS


@allure.id("37504")
@allure.label("layer", "api_layer")
@allure.label("jira", "IMQA-1105")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("GDPR")
@allure.title("Скачивание GDPR отчета")
@SAAS
@PRE_SAAS
def test_gdpr_get(
    auth_account,
):
    with allure.step("Пробуем сделать запрос"):
        auth_account.files_gdpr_get(auth_account.uin)
