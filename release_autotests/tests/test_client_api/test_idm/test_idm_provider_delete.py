import allure
import pytest

from support.markers import SAAS, SANDBOX, PRE_SAAS


@allure.id("50834")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("idm")
@allure.feature("Удаление типа аутентификации из аккаунта пользователя")
@allure.title("Удаление типа аутентификации из аккаунта пользователя")
@SAAS
@PRE_SAAS
@SANDBOX
@pytest.mark.skip("Тест требует токен ESIA")
def test_idm_provider_delete(auth_account, opponent_account):
    auth_account.idm_provider_delete(token=auth_account.token)
