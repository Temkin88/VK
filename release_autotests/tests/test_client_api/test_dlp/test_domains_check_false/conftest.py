import pytest

from tests.test_client_api.test_dlp.common import create_chats


@pytest.fixture(scope="session")
def config_option():
    return "domains_check_false"


@pytest.fixture(scope="session", autouse=True)
def skip_if_option_not_in_config(config_option, dlp_config):
    if "adapters" not in dlp_config or config_option not in dlp_config["adapters"]:
        pytest.skip("Domains for this cases not described")


@pytest.fixture(scope="session")
def chat_entities_multidomain(main_acc, first_opponent_acc, second_opponent_acc):
    chats = create_chats(main_acc=main_acc, opponent_acc=[first_opponent_acc, second_opponent_acc])
    return main_acc, first_opponent_acc, second_opponent_acc, chats


@pytest.fixture(scope="session")
def main_acc(account_fabric, dlp_config, config_option, internal_header, default_main_acc):
    domain = dlp_config["adapters"][config_option]["domain"]
    if default_main_acc is not None and domain in default_main_acc.uin:
        return default_main_acc
    header = {"User-Agent": internal_header} if internal_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )


@pytest.fixture(scope="session")
def first_opponent_acc(account_fabric, dlp_config, config_option, internal_header, default_opponent_acc):
    domain = dlp_config["adapters"][config_option]["domains"][0]
    if default_opponent_acc is not None and domain in default_opponent_acc.uin:
        return default_opponent_acc
    header = {"User-Agent": internal_header} if internal_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )


@pytest.fixture(scope="session")
def second_opponent_acc(account_fabric, dlp_config, config_option, internal_header):
    domain = dlp_config["adapters"][config_option]["domains"][1]
    header = {"User-Agent": internal_header} if internal_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )
