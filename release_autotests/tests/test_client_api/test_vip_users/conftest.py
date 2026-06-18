import pytest

from pyvkteamsclient.client import DesktopClient


@pytest.fixture(scope="session")
def get_vip_accounts(
    get_myteam_config: dict,
    pytestconfig: pytest.Config,
):
    if (
        "vip_accounts" not in get_myteam_config
        or pytestconfig.getoption("--ignore-vip")
        or get_myteam_config.get("ignore-vip", False)
    ):
        pytest.skip("No vip accounts in tests config")

    return get_myteam_config["vip_accounts"]


@pytest.fixture(scope="session")
def vip_one(
    get_vip_accounts,
    ENV_PLATFORM,
    session,
    main_api,
    api_version,
    forced_ip,
    imap_serv,
    alter_sandbox,
):
    account = get_vip_accounts["1"]

    if ENV_PLATFORM == "SANDBOX":
        main_account = DesktopClient(
            uin=account.get("uin") or account.get("username"),
            session=session,
            otp_token=account["password"],
            api_url=main_api,
            api_ver=api_version,
            product_name=ENV_PLATFORM,
            forced_ip=forced_ip,
            is_alter_sandbox=alter_sandbox,
        )
    else:
        main_account = DesktopClient(
            uin=account["username"],
            session=session,
            otp_token="1",
            api_url=main_api,
            api_ver=api_version,
            product_name=ENV_PLATFORM,
            forced_ip=forced_ip,
            env=ENV_PLATFORM,
            email_password=account["password"],
            email_url=imap_serv,
            is_alter_sandbox=alter_sandbox,
        )

    main_account.restore_privacy_settings()

    return main_account


@pytest.fixture(scope="session")
def vip_two(
    get_vip_accounts,
    ENV_PLATFORM,
    session,
    main_api,
    api_version,
    forced_ip,
    imap_serv,
    alter_sandbox,
):
    account = get_vip_accounts["2"]

    if ENV_PLATFORM == "SANDBOX":
        main_account = DesktopClient(
            uin=account.get("uin") or account.get("username"),
            session=session,
            otp_token=account["password"],
            api_url=main_api,
            api_ver=api_version,
            product_name=ENV_PLATFORM,
            forced_ip=forced_ip,
            is_alter_sandbox=alter_sandbox,
        )
    else:
        main_account = DesktopClient(
            uin=account["username"],
            session=session,
            otp_token="1",
            api_url=main_api,
            api_ver=api_version,
            product_name=ENV_PLATFORM,
            forced_ip=forced_ip,
            env=ENV_PLATFORM,
            email_password=account["password"],
            email_url=imap_serv,
            is_alter_sandbox=alter_sandbox,
        )

    main_account.restore_privacy_settings()

    return main_account
