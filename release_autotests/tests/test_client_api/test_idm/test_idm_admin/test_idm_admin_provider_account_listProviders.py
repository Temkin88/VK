import allure
import pytest

from support.markers import SAAS, SANDBOX, PRE_SAAS


@allure.id("507925")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("idm")
@allure.feature("Показать список типов аутентификаций у пользователя")
@allure.title("Показать список типов аутентификаций у пользователя")
@SAAS
@PRE_SAAS
@SANDBOX
@pytest.mark.skip("Нужна аутентификация с ESIA")
def test_idm_admin_provider_account_list_providers(auth_account, create_admin_provider):
    with allure.step("Пробуем получить список типов аутентификаций у пользователя"):
        response = auth_account.idm_admin_provider_account_listProviders(
            user_sn=auth_account.uin, domain="test@test.ru"
        )

        assert response["status"]["code"] == 20000, "Response code error"
