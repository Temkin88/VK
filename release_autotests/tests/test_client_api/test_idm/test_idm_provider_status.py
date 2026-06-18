import allure
import pytest

from support.markers import SAAS, SANDBOX, PRE_SAAS


@allure.id("508344")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("idm")
@allure.feature("Получение списка статусов возможных аутентификаций для пользователя")
@allure.title("Получение списка статусов возможных аутентификаций для пользователя")
@SAAS
@PRE_SAAS
@SANDBOX
@pytest.mark.skip("Тест требует токен ESIA")
def test_idm_provider_status(auth_account, opponent_account):
    auth_account.idm_provider_status(token=auth_account.token)
