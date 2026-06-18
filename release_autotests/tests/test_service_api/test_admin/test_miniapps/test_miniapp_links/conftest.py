import allure
import pytest


@pytest.fixture(scope="session")
def create_link_domain(admin_account):
    with allure.step("Создать ссылку для домена"):
        response = admin_account.api_miniapp_links_set_сonfig(
            domain="test.net", links=[{"link": "https://sbor.info.gov.ru/", "name": "test name miniapp"}]
        )
        assert response["status"]["code"] == 20000, "Response code error"

    return "test.net", "https://sbor.info.gov.ru/", "test name miniapp"


@pytest.fixture(scope="session", autouse=True)
def clean_links_domain(admin_account, logger):
    yield

    try:
        admin_account.api_miniapp_links_delete_domain(domain="test.net")
    except Exception as error:
        logger.error(error)
