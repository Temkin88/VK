import allure
import pytest

from support.markers import SAAS, SANDBOX, PRE_SAAS


@allure.id("507927")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("idm")
@allure.feature("Удалить тип аутентификации из аккаунта")
@allure.title("Удаление типа аутентификации из аккаунта")
@SAAS
@PRE_SAAS
@SANDBOX
@pytest.mark.skip("Нужна аутентификация с ESIA")
def test_idm_admin_provider_account_delete(auth_account, create_admin_provider):
    with allure.step("Пробуем добавить новый вид аутентификации"):
        response = auth_account.idm_admin_provider_account_delete(
            user_sn=auth_account.uin, _type="test", domain="test@test.ru"
        )

        assert response["status"]["code"] == 20000, "Response code error"
