import pytest

from tests.test_client_api.test_dlp.common import create_chats


@pytest.fixture(scope="session")
def config_option():
    return "debug_mode_true"


@pytest.fixture(scope="session", autouse=True)
def skip_if_option_not_in_config(config_option, dlp_config):
    if "adapters" not in dlp_config or config_option not in dlp_config["adapters"]:
        pytest.skip("Domains for this cases not described")


@pytest.fixture(scope="session")
def chat_entities(main_acc, opponent_acc):
    chats = create_chats(main_acc=main_acc, opponent_acc=opponent_acc)
    return main_acc, opponent_acc, chats


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
def main_acc_second_instance(account_fabric, main_acc, internal_header, default_main_acc_second_instance):
    domain = main_acc.uin.split("@")[1]
    if default_main_acc_second_instance is not None and domain in default_main_acc_second_instance.uin:
        return default_main_acc_second_instance
    header = {"User-Agent": internal_header} if internal_header is not None else {}
    return account_fabric(
        header=header,
        account_uin=main_acc.uin,
        domain=domain,
    )


@pytest.fixture(scope="session")
def opponent_acc(account_fabric, dlp_config, config_option, internal_header, default_opponent_acc):
    domain = dlp_config["adapters"][config_option]["domain"]
    if default_opponent_acc is not None and domain in default_opponent_acc.uin:
        return default_opponent_acc
    header = {"User-Agent": internal_header} if internal_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )
