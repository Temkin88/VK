import pytest


@pytest.fixture(scope="session")
def conference_url(ENV_PLATFORM, auth_account):
    if auth_account.api_ver <= 99:
        response = auth_account.rapi_conference_create(
            name="Test guest auth",
            _type="equitable",
            participants=[auth_account.uin],
            callParticipants=True,
            pinRequired=False,
        )
    else:
        response = auth_account.rapi_conference_create_new(
            name="Test guest auth",
            type="equitable",
            members={
                "autotest005@autotest.clients": {
                    "role": "speaker",
                },
            },
            pinRequired=False,
            roles={
                "speaker": {
                    "permissions": 512,
                },
                "default": {
                    "permissions": 10,
                },
            },
        )

    return response["results"]["conferenceUrl"]
