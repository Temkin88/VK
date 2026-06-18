import allure

from support.markers import SANDBOX


@allure.id("491427")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Миниаппы")
@allure.title(
    "Задать ссылки для домена",
)
@SANDBOX
def test_api_miniapp_links_get_config(
    admin_account,
):
    """
    Задаем ссылки для домена
    """
    domain = "test.net"
    link_for_domain = "https://sbor.info.gov.ru/"
    name_for_domain = "test name miniapp"

    with allure.step("Пробуем создать ссылку для домена"):
        response = admin_account.api_miniapp_links_set_сonfig(
            domain=domain, links=[{"link": link_for_domain, "name": name_for_domain}]
        )

        assert response["status"]["code"] == 20000, "Response code error"

    with allure.step("Проверяем создалась ли ссылка для домена"):
        response = admin_account.api_miniapp_links_get_сonfig(domain=domain)
        results = response["result"]

        assert response["status"]["code"] == 20000, "Response code error"
        assert all(link_for_domain in links["link"] and name_for_domain in links["name"] for links in results["links"])
