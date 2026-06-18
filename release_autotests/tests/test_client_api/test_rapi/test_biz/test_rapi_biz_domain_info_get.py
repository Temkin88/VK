import allure

from support.markers import SANDBOX


@allure.id("544676")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("biz")
@allure.feature("Проверка домена")
@allure.title("Проверка домена")
@SANDBOX
def test_rapi_biz_domain_info_get(
    auth_account,
):
    """
    Проверка домена
    """
    with allure.step("Пробуем проверить домен"):
        response = auth_account.rapi_biz_domain_info_get(domain="@autotest.clients")

        assert response["status"]["code"] == 20000, "Response error code"
        assert "agent" in response["results"], "Field agent not in results"
