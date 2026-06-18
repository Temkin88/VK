import allure
import pytest

from support.markers import SAAS, SANDBOX, PRE_SAAS


@allure.id("508345")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("idm")
@allure.feature("Добавить тип аутентификации пользователю")
@allure.title("Добавление нового провайдера аутентификации пользователю")
@SAAS
@PRE_SAAS
@SANDBOX
@pytest.mark.skip("Тест требует токен ESIA")
def test_idm_provider_create(auth_account, opponent_account):
    auth_account.idm_provider_create(token=auth_account.token)
