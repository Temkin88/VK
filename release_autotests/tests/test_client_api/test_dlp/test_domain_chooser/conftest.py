import pytest

from tests.test_client_api.test_dlp.common import create_chats


@pytest.fixture(scope="session", autouse=True)
def skip_if_option_not_in_config(dlp_config):
    if (
        "adapters" not in dlp_config
        or "strategy_on_fail_block" not in dlp_config["adapters"]
        or "strategy_on_fail_ok" not in dlp_config["adapters"]
        or "debug_mode_true" not in dlp_config["adapters"]
        or "internal_files" not in dlp_config["adapters"]
    ):
        pytest.skip("Domains for this cases not described")


@pytest.fixture(scope="session")
def chat_entities_multidomain(
    acc_strategy_on_fail_block_adapter, acc_strategy_on_fail_ok_adapter, acc_debug_mode_true_adapter
):
    chats = create_chats(
        main_acc=acc_strategy_on_fail_block_adapter,
        opponent_acc=[acc_strategy_on_fail_ok_adapter, acc_debug_mode_true_adapter],
    )
    return acc_strategy_on_fail_block_adapter, acc_strategy_on_fail_ok_adapter, acc_debug_mode_true_adapter, chats


@pytest.fixture(scope="session")
def acc_strategy_on_fail_ok_adapter(account_fabric, dlp_config, external_header, default_main_acc):
    domain = dlp_config["adapters"]["strategy_on_fail_ok"]["domain"]
    if default_main_acc is not None and domain in default_main_acc.uin:
        return default_main_acc
    header = {"User-Agent": external_header} if external_header is not None else {}

    return account_fabric(
        header=header,
        domain=domain,
    )


@pytest.fixture(scope="session")
def acc_strategy_on_fail_block_adapter(account_fabric, dlp_config, internal_header, default_opponent_acc):
    domain = dlp_config["adapters"]["strategy_on_fail_block"]["domain"]
    if default_opponent_acc is not None and domain in default_opponent_acc.uin:
        return default_opponent_acc
    header = {"User-Agent": internal_header} if internal_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )


@pytest.fixture(scope="session")
def acc_debug_mode_true_adapter(account_fabric, dlp_config, external_header):
    domain = dlp_config["adapters"]["debug_mode_true"]["domain"]
    header = {"User-Agent": external_header} if external_header is not None else {}
    return account_fabric(
        header=header,
        domain=domain,
    )
