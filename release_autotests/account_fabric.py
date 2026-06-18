import os
from typing import Optional

from imcommonsupplyclient.session import Session as SupplySession
import pytest
import allure
import requests
from pyvkteamsclient.client import DesktopClient

from conftest import get_config


@pytest.fixture(scope="session")
def account_collection():
    accounts = {}
    return accounts


@pytest.fixture(scope="session")
def supply_sessions_dict(supply_session):
    supply_sessions = {}
    if supply_session is not None and supply_session.domain not in supply_sessions:
        supply_sessions[supply_session.domain] = supply_session
    yield supply_sessions
    for supply_session in supply_sessions.values():
        supply_session.end_session()


@pytest.fixture(scope="session")
def account_cleaner(ENV_PLATFORM):
    accounts = []
    yield accounts
    for acc in accounts:
        if ENV_PLATFORM not in ["SANDBOX", "PRE_TARM", "PRE_VKTI", "VKTI", "PRE_SAAS"]:
            acc.clean_account()


@allure.title("Получение сессии")
@pytest.fixture(scope="session")
def get_session_with_specific_headers(web_url, set_rate_limit):
    def func(swagger_http_spy, headers, PROXY=None):
        with requests.Session() as session:
            default_heades = {
                "User-Agent": "Mozilla/5.0 () AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
                "Referer": web_url,
                "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "macOS",
            }
            if headers is None:
                headers = {}
            headers = default_heades | headers
            session.headers = headers
            session.verify = False

            if PROXY is not None:
                session.proxies = {
                    "http": PROXY,
                    "https": PROXY,
                }

            if swagger_http_spy is not None:
                swagger_http_spy.register_as_hook(session)

            set_rate_limit(session=session, url="wim/auth/clientLogin", limit_per_minute=10)
            set_rate_limit(session=session, url="rapi/message/send", limit_per_second=9, limit_per_minute=99)
            return session

    return func


@pytest.fixture(scope="session")
def account_with_specific_session(api_version):
    def func(
        session,
        account_from_supply_server,
    ):
        api_ver = (account_from_supply_server.pop("api_ver", None), account_from_supply_server)
        api_ver = api_version if api_version else api_ver
        if "session" in account_from_supply_server:
            account_from_supply_server.pop("session")
        account = DesktopClient(session=session, polling=False, api_ver=api_ver, **account_from_supply_server)
        account.restore_privacy_settings()
        return account

    return func


@pytest.fixture(scope="session")
def get_account_from_supply_server(ENV_PLATFORM):
    def func(supply_session, USE_SSO, domain, vip_type="BASIC", is_template=False) -> dict[str, str]:
        is_admin = ENV_PLATFORM == "SANDBOX"
        if is_template:
            return supply_session.acquire_account_by_regexp(
                as_dict=True, uin_template=domain, is_admin=is_admin, vip_type=vip_type
            )
        else:
            return supply_session.acquire_account(
                as_dict=True, sso=USE_SSO, user_domain=domain, is_admin=is_admin, vip_type=vip_type
            )

    return func


@allure.title("Получение сессии supply-сервера")
@pytest.fixture(scope="session")
def get_supply_session(ENV_PLATFORM, SANDBOX, api_version, SUPPLY_URL, USE_SSO, DOMAIN_PAID, supply_sessions_dict):
    def func(domain=None):
        if domain is not None and domain in supply_sessions_dict:
            return supply_sessions_dict[domain]
        else:
            if (
                ENV_PLATFORM in ["SANDBOX", "PRE_TARM", "PRE_VKTI", "VKTI", "PRE_SAAS"]
                or (ENV_PLATFORM == "SAAS" and USE_SSO)
                or (ENV_PLATFORM == "SAAS" and DOMAIN_PAID)
            ):
                if domain is None:
                    if os.getenv("PUPPET_TESTS"):
                        domain = get_config(SANDBOX).get("api-urls").get("main-api").replace("https://u-", "")
                    else:
                        domain = SANDBOX

                sup_session = SupplySession(
                    environment=ENV_PLATFORM,
                    domain=domain,
                    api_version=api_version,
                    test_platform="IMSERVER",
                    max_accounts_count=50,
                    supply_url=SUPPLY_URL,
                )
                sup_session.init_session()
                supply_sessions_dict[domain] = sup_session
                return sup_session

            else:
                return

    return func


@pytest.fixture(scope="session")
def account_fabric(
    supply_session,
    USE_SSO,
    swagger_http_spy,
    get_session_with_specific_headers,
    account_with_specific_session,
    account_collection,
    account_cleaner,
    get_account_from_supply_server,
):
    def func(
        domain: Optional[str] = None,
        account_dict=None,
        header=None,
        account_uin=None,
        vip_type="BASIC",
        supply_session=supply_session,
        is_template=False,
    ):
        if account_dict is None:
            if account_uin is None:
                account_dict = get_account_from_supply_server(supply_session, USE_SSO, domain, vip_type, is_template)
            else:
                if account_uin in account_collection:
                    account_dict = account_collection[account_uin]
                else:
                    raise Exception("wrong required account_uin")
        account_collection[account_dict["uin"]] = account_dict
        session = get_session_with_specific_headers(swagger_http_spy, headers=header)
        account = account_with_specific_session(session, account_dict)
        account_cleaner.append(account)
        return account

    return func
