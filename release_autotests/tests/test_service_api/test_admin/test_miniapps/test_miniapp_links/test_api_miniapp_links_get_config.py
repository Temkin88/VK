import allure

from support.markers import SANDBOX


@allure.id("491426")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Миниаппы")
@allure.title(
    "Получить ссылки для домена",
)
@SANDBOX
def test_api_miniapp_links_get_config(
    admin_account,
    create_link_domain,
):
    domain, link_for_domain, name_for_domain = create_link_domain

    with allure.step("Проверяем создалась ли ссылка для домена"):
        response = admin_account.api_miniapp_links_get_сonfig(domain=domain)
        results = response["result"]

        assert response["status"]["code"] == 20000, "Response code error"
        assert all(link_for_domain in links["link"] and name_for_domain in links["name"] for links in results["links"])
