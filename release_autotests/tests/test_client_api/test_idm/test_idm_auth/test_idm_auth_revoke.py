import allure
import pytest

from support.markers import SAAS, SANDBOX, PRE_SAAS

client_info = {
    "SAAS": ["calendar", "1d07901a61fef602c159dc04aa85e8d07b33cf280804988a3c1434c237da2dca"],
    "SANDBOX": [
        "miniapp-997fc1dc-de3c-41c2-9a0e-51b439bf079d",
        "d1f14be008f7a4ec8b3e59633d9ca77ec8982b75baa51ffcc82c9854dc382c28",
    ],
}


@allure.id("508197")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("idm")
@allure.feature("Отзыв токена")
@allure.title("Отзыв токена")
@SAAS
@PRE_SAAS
@SANDBOX
@pytest.mark.last
def test_idm_auth_revoke(auth_account, opponent_account):
    response = auth_account.idm_auth_revoke(client_id=opponent_account.uin, token=opponent_account.refresh_token)

    assert response["status"]["code"] == 20000, "Response code error"
