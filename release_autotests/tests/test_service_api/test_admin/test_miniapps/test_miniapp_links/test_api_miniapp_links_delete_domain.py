import allure
import pytest
from pyvkteamsclient.admin.exceptions import RequestException

from support.markers import SANDBOX


@allure.id("491425")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Миниаппы")
@allure.title(
    "Удалить домен со ссылками",
)
@SANDBOX
@pytest.mark.last
def test_api_miniapp_links_delete_domain(
    admin_account,
    create_link_domain,
):
    domain, _, _ = create_link_domain

    with allure.step("Проверяем создалась ли ссылка для домена"):
        response = admin_account.api_miniapp_links_get_сonfig(domain=domain)

        assert response["status"]["code"] == 20000, "Response code error"

    with allure.step("Пробуем удалить ссылку на домен"):
        admin_account.api_miniapp_links_delete_domain(domain=domain)

        assert response["status"]["code"] == 20000, "Response code error"

    with allure.step("Проверяем что ссылка на домен удалилась"), pytest.raises(RequestException):
        admin_account.api_miniapp_links_get_сonfig(domain=domain)
