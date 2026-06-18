import pytest


@pytest.fixture(scope="session", autouse=True)
def skip_idm_on_sandbox(ENV_PLATFORM, USE_SSO):
    if (not USE_SSO and ENV_PLATFORM == "SANDBOX") or (not USE_SSO and ENV_PLATFORM == "SAAS"):
        pytest.skip("На песках без sso не находим аккаунты")
