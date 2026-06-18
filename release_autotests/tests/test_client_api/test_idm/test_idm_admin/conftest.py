import pytest


@pytest.fixture(scope="session", autouse=True)
def skip_idm_admin():
    pytest.skip("Тесты требуют админских client_id, client_secret")


@pytest.fixture(scope="session", autouse=True)
def delete_admin_provider(auth_account, get_admin_token, USE_SSO):
    yield
    if USE_SSO:
        domain = "dev6.on-premise.ru"

        response = auth_account.idm_admin_provider_list(domain=domain, access_token=get_admin_token)
        result = response["results"]["providers"]

        otp_types = [_type for _type in result if _type["type"] == "OTP" and _type["available"]]

        for otp_type in otp_types:
            auth_account.idm_admin_provider_delete(_type=otp_type["type"], domain=domain, access_token=get_admin_token)


@pytest.fixture(scope="session")
def create_admin_provider(auth_account, get_admin_token, USE_SSO):
    if USE_SSO:
        auth_account.idm_admin_provider_create(_type="OTP", domain="dev6.on-premise.ru", access_token=get_admin_token)


@pytest.fixture(scope="session")
def get_admin_token(auth_account, USE_SSO, ENV_PLATFORM):
    if USE_SSO and ENV_PLATFORM == "SANDBOX":
        response = auth_account.idm_auth_token(
            client_id="4a22ab33f948e89a0568cf90af21c3bc",
            client_secret="e5f3859e61b3e7ec62a6d3314d8eb5187f8762a0503266e060c386b74cf0591e92faecf4cc5084b0efc464c933fc3ca21ca3495a6cefad43bd5bd475bc56c9b4",
            grant_type="client_credentials",
        )

        return response["access_token"]
    else:
        pytest.mark.skip("Работает только на песках")
