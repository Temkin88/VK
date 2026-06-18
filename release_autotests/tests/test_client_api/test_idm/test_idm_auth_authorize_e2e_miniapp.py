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


@pytest.fixture(scope="session", autouse=True)
def skip_if_not_using_sso(USE_SSO):
    if not USE_SSO:
        pytest.skip("Skipping test if not using SSO")


@allure.id("501265")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("idm")
@allure.feature("Сквозная аутентификация через миниапп")
@allure.title("Сквозная аутентификация через миниапп")
@SAAS
@PRE_SAAS
@SANDBOX
def test_idm_auth_authorize_e2e_miniapp(ENV_PLATFORM, auth_account, api_version):
    client_id = client_info["SAAS"][0] if ENV_PLATFORM == "SAAS" else client_info["SANDBOX"][0]
    client_secret = client_info["SAAS"][1] if ENV_PLATFORM == "SAAS" else client_info["SANDBOX"][1]

    with allure.step("Пробуем получить silent_token"):
        response = auth_account.idm_auth_token_silent(
            client_id=client_id,
            grant_type="silent_token",
            access_token=auth_account.token,
        )
        acc_silent_token = response["silent_token"]
        assert acc_silent_token, "No silent token"
        assert response["token_type"] == "silent", "No silent token"

    with allure.step("Получение токена миниаппа"):
        response = auth_account.idm_auth_token(
            client_secret=client_secret,
            grant_type="exchange_silent_token",
            silent_token=acc_silent_token,
            miniapp_access_ttl=600,
        )
        miniapp_token = response["access_token"]
        assert miniapp_token, "No silent token"

    with allure.step("Проверка токена миниаппа"):
        response = auth_account.idm_auth_validate(access_token=miniapp_token)
        results = response["results"]

        assert results["user_sn"] == auth_account.uin, f"User={results['user_sn']} dont matched"
        assert results["target_id"] == client_id, "miniapp_id dont matched"

    if api_version >= 128:
        with allure.step("Проверка информации пользователя через токен миниаппа"):
            response = auth_account.idm_auth_userinfo(access_token=miniapp_token)

            assert response["email"] == auth_account.uin, "Email dont matched"
            assert response["given_name"] == auth_account.uin, "Name dont matched"
            assert response["family_name"] == auth_account.uin, "Family name dont matched"

    with allure.step("Пробуем создать чат"):
        name = "Test"
        about = "Test description"
        rules = "Test rules"
        default_role = "member"

        response = auth_account.rapi_createChat(
            name=name,
            members=[],
            about=about,
            rules=rules,
            defaultRole=default_role,
        )
        results = response["results"]
        assert response["status"]["code"] == 20000, "Response code error"
        assert isinstance(results["sn"], str), "sn not string"
        assert results["sn"], "No field sn"

        assert all(i["sn"] == auth_account.uin for i in results["persons"]), "Persons dont matched"
