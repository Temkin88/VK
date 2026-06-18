import pytest

from tests.test_client_api.test_dlp.common import create_chats


@pytest.fixture(scope="session")
def config_option():
    return "internal_files"


@pytest.fixture(scope="session", autouse=True)
def skip_if_option_not_in_config(config_option, dlp_config):
    if "adapters" not in dlp_config or config_option not in dlp_config["adapters"]:
        pytest.skip("Domains for this cases not described")


@pytest.fixture(scope="session")
def chat_entities_with_internal_accounts(first_account_with_internal_session, second_account_with_internal_session):
    chats = create_chats(
        main_acc=first_account_with_internal_session, opponent_acc=second_account_with_internal_session
    )
    return first_account_with_internal_session, second_account_with_internal_session, chats


@pytest.fixture(scope="session")
def chat_entities_with_external_accounts(first_account_with_external_session, second_account_with_external_session):
    chats = create_chats(
        main_acc=first_account_with_external_session, opponent_acc=second_account_with_external_session
    )
    return first_account_with_external_session, second_account_with_external_session, chats


@pytest.fixture(scope="session")
def first_account_with_external_session(account_fabric, dlp_config, config_option, external_header):
    domain = dlp_config["adapters"][config_option]["domain"]
    header = {"User-Agent": external_header} if external_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )


@pytest.fixture(scope="session")
def first_account_with_internal_session(first_account_with_external_session, account_fabric, internal_header):
    domain = first_account_with_external_session.uin.split("@")[1]
    header = {"User-Agent": internal_header} if internal_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )


@pytest.fixture(scope="session")
def first_account_with_second_external_session(first_account_with_external_session, account_fabric, external_header):
    domain = first_account_with_external_session.uin.split("@")[1]
    header = {"User-Agent": external_header} if external_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )


@pytest.fixture(scope="session")
def first_account_with_second_internal_session(first_account_with_external_session, account_fabric, internal_header):
    domain = first_account_with_external_session.uin.split("@")[1]
    header = {"User-Agent": internal_header} if internal_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )


@pytest.fixture(scope="session")
def second_account_with_external_session(account_fabric, dlp_config, config_option, external_header):
    domain = dlp_config["adapters"][config_option]["domain"]
    header = {"User-Agent": external_header} if external_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )


@pytest.fixture(scope="session")
def second_account_with_internal_session(second_account_with_external_session, account_fabric, internal_header):
    domain = second_account_with_external_session.uin.split("@")[1]
    header = {"User-Agent": internal_header} if internal_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )
