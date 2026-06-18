import pytest


@pytest.fixture
def setup_contact_add(auth_account, opponent_account):
    opponent_account.send_basic_message(auth_account.uin, "ping")

    yield

    auth_account.rapi_contacts_delete([opponent_account.uin])
