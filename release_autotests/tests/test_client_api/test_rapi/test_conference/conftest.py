import pytest


@pytest.fixture(scope="session")
def conference_create(auth_account, opponent_account):
    response = auth_account.rapi_conference_create_new(
        name="Test conference",
        type="equitable",
        pinRequired=True,
        members={
            opponent_account.uin: {
                "role": "moderator",
            },
        },
        roles={
            "moderator": {
                "permissions": 255,
            },
            "default": {
                "permissions": 10,
            },
        },
    )

    return response["results"]


@pytest.fixture(scope="session")
def conference_id(conference_create):
    return conference_create["conferenceId"]
