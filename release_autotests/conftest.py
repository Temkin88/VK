import json
import logging
import os
import pathlib
import random
import re

import time
import uuid
from typing import Optional

import urllib3

import allure
import pytest
import requests
import requests.exceptions
from filelock import FileLock
from quarantine_client import TestQuarantineApiClient

from imcommonsupplyclient.inner_types import EnvironmentType
from pyrate_limiter import SQLiteBucket
from requests_ratelimiter import LimiterAdapter
from _pytest.config import Config
from _pytest.nodes import Item
from faker import Faker
from urllib3.exceptions import InsecureRequestWarning

from pyvkteamsbot.bot.bot import Bot

from pyvkteamsclient.admin import AdminClient
from pyvkteamsclient.client import DesktopClient, IprosClient
from pyvkteamsclient.client.base import Client
from pyvkteamsclient.stentor import StentorClient

from imcommonsupplyclient.session import Session as SupplySession

from support.cases.metabot_keyboard import keyboard
from support.modules.events import EventFilter


urllib3.disable_warnings(InsecureRequestWarning)

log = logging.getLogger(__name__)

quarantine_cl = TestQuarantineApiClient(base_url="http://100.70.136.147")

HERE_SLOW: bool = True

efilter = EventFilter()

fake = Faker("en_US")
Faker.seed(0)

pytest_plugins = ["account_fabric", "checks_fixtures"]


def get_allure_id(item: Item) -> Optional[int]:
    """
    Получаем ID тест кейса из маркера Allure
    """
    markers = item.own_markers.copy()
    markers.reverse()

    for marker in markers:
        if marker.name == "allure_label" and "label_type" in marker.kwargs and marker.kwargs["label_type"] == "as_id":
            try:
                return int(marker.args[-1])
            except ValueError:
                log.warning(f'Broken id on test "{item.name}"')
                return None

    return None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item, call):
    """
    result_setup - setup result
    result_call - test result
    result_teardown - teardown result
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "result_" + rep.when, rep)  # noqa
    setattr(item, "result", rep)  # noqa
    if not hasattr(item, "duration"):
        setattr(item, "duration", rep.duration)  # noqa
    else:
        item.duration += rep.duration  # noqa

    if rep.outcome == "skipped" or rep.when == "call":
        env_option = item.config.getoption("-m")

        env: EnvironmentType

        if "SANDBOX" in env_option:
            env = "SANDBOX"

        elif "PRE_VKTI" in env_option:
            env = "PRE_VKTI"

        elif "VKTI" in env_option:
            env = "VKTI"

        elif "PRE_TARM" in env_option:
            env = "PRE_TARM"

        elif "TARM" in env_option:
            env = "TARM"

        elif "PRE_SAAS" in env_option:
            env = "PRE_SAAS"

        elif "SAAS" in env_option:
            env = "SAAS"

        else:
            raise ValueError(f"Unknown env value: {env_option}")

        allure_id = get_allure_id(item=item)

        name = item.nodeid.replace("/", ".").replace("::", "#")

        try:
            quarantine_cl.update_test_status(
                env=env,
                project="IMSERVER",
                allure_id=allure_id,
                allure_launch_id=os.getenv("ALLURE_LAUNCH_ID", 0),
                name=name,
                status=item.result_call.outcome if hasattr(item, "result_call") else item.result.outcome,
                duration=item.duration,
            )
        except Exception as error:
            log.error(error)


@pytest.fixture
def fetch_until_empty_answer_with_filter(event_filter):
    def fetch_until_empty(account: DesktopClient, *event_type: str):
        count_timer = 0
        counter = 0

        while count_timer < 5000:
            while account.fetch(timeout=500) and counter <= 100:
                counter += 1

            events_list = list(event_filter(account.events, *event_type))

            if events_list:
                return events_list

            count_timer += 200
        return []

    return fetch_until_empty


@pytest.fixture(scope="session")
def fetch_until_empty_answer():
    def fetch_until_empty(account: DesktopClient):
        counter = 0

        events = [1]

        while events and counter <= 1000:
            events = account.fetch(timeout=200)
            counter += 1

    return fetch_until_empty


def generate_random_bot_name():
    return "test_" + str(uuid.uuid1()).replace("-", "")[:21] + "_bot"


@allure.title("Написать Metabot /start")
@pytest.fixture(scope="session")
def start_metabot(auth_account, metabot):
    with allure.step("Написать Metabot /start"):
        msg_id = auth_account.send_basic_message(
            sn=metabot,
            text="/start",
        )

    with allure.step("Ждем ответа"):
        time.sleep(6)

    with allure.step("Получаем ID ответа бота"):
        result = auth_account.rapi_getHistory(
            sn=metabot,
            count=-1,
            fromMsgId=msg_id,
            patchVersion="init",
        )

    return msg_id, result["results"]["lastMsgId"]


@pytest.fixture(scope="session")
def bot_aimsid(
    auth_account,
    metabot,
    start_metabot,
):
    user_msg_id, bot_msg_id = start_metabot

    with allure.step("Отправляем callback создания бота"):
        auth_account.rapi_getBotCallbackAnswer(
            chatId=metabot,
            msgId=bot_msg_id,
            callbackData="newbot",
        )

    with allure.step("Ждем ответ"):
        time.sleep(6)

        msg_edited = False

        result = auth_account.rapi_getHistory(
            sn=metabot,
            count=1,
            fromMsgId=user_msg_id,
            patchVersion=str(bot_msg_id),
        )

        for message in result["results"]["messages"]:
            bot_keyboard = message.get("inlineKeyboardMarkup")
            if bot_keyboard != keyboard["ru"] and bot_keyboard != keyboard["en"]:
                msg_edited = True

        assert msg_edited, "bots:metabot_msg_keyboard_not_edited"

    bot_name = generate_random_bot_name()

    with allure.step("Отправляем ник бота"):
        auth_account.send_basic_message(
            sn=metabot,
            text=bot_name,
        )

    with allure.step("Ждем ответа"):
        time.sleep(5)

    with allure.step("Проверяем ответ"):

        def get_bot_token(msg_text: str) -> str:
            for entry in re.findall(r"\d+\.\d+\.\d+\:\d+", msg_text):
                return entry

        result = auth_account.rapi_getHistory(
            sn=metabot,
            count=-1,
        )

        for message in result["results"]["messages"]:
            if get_bot_token(message["text"]):
                return get_bot_token(message["text"])


@pytest.fixture(scope="session")
def clean_contact_list(auth_account, opponent_account):
    for account in (auth_account, opponent_account):
        account.clear_contacts_list()

    return


@pytest.fixture(scope="session")
def bot_class(
    ENV_PLATFORM,
    supply_session,
    get_myteam_config,
    alter_sandbox,
    prepare_test_chats,
    swagger_http_spy,
    USE_SSO,
    DOMAIN_PAID,
):
    if supply_session is not None:
        if ENV_PLATFORM == "SANDBOX":
            bot_uin = "auto001bot"
        elif ENV_PLATFORM == "PRE_TARM":
            bot_uin = "1000000055"
        elif ENV_PLATFORM == "VKTI":
            bot_uin = "1000001106"
        elif ENV_PLATFORM == "PRE_VKTI":
            bot_uin = "1000002902"
        elif ENV_PLATFORM == "SAAS" and USE_SSO:
            bot_uin = "1011867422"
        elif ENV_PLATFORM == "SAAS" and DOMAIN_PAID:
            bot_uin = "1011969528"
        elif ENV_PLATFORM == "SAAS":
            bot_uin = "1011969131"
        else:
            raise ValueError(f"Unsupported env: {ENV_PLATFORM}")

        supply_bot = supply_session.acquire_bot(uin=bot_uin)

        bot_ = Bot(
            env=ENV_PLATFORM,
            api_url_base=supply_bot.api_url_base,
            token=supply_bot.token,
            name=supply_bot.nickname,
            is_myteam=True,
        )
    elif (ENV_PLATFORM != "SANDBOX" and "bot" not in get_myteam_config) or (
        "bot" not in get_myteam_config and alter_sandbox
    ):
        pytest.skip("Bot token/API URL not found in config")
    else:
        bot_ = Bot(is_myteam=True, **get_myteam_config["bot"])

    user, opponent, group, channel = prepare_test_chats

    for chat_type in (group, channel):
        user.rapi_group_members_add(
            sn=chat_type,
            members=[bot_.uin],
        )
        user.rapi_modChatMember(
            sn=chat_type,
            memberSn=bot_.uin,
            role="moder",
        )

    if swagger_http_spy is not None:
        swagger_http_spy.register_as_hook(bot_.http_session)

    bot_.http_session.verify = False

    return bot_


@allure.title("Замедление тестов")
@pytest.fixture
def show_stop(SLOW):
    Client.slow_time = 1


@pytest.fixture(scope="session")
def metabot():
    return "70001"


@pytest.fixture(scope="session")
def stickers_bot():
    return "100500"


@pytest.fixture
def event_filter():
    efilter.start_point()

    return efilter


def get_config(link: str) -> dict:
    response = None

    response = requests.get(
        f"https://{link}/myteam-config.json",
        timeout=10,
        verify=False,
    )

    if response.status_code != 200:
        log.error(response.text)
        response = requests.get(
            f"http://{link}/myteam-config.json",
            timeout=10,
            verify=False,
        )

        if response.status_code != 200:
            pytest.raises(Exception)

    if response is not None:
        response.raise_for_status()
        return response.json()

    else:
        raise ValueError


def get_config_saas(link: str, domain: str) -> dict:
    response = None

    response = requests.get(
        f"https://{link}/myteam-config.json",
        params={"domain": domain},
        timeout=10,
        verify=False,
    )

    if response.status_code != 200:
        log.error(response.text)
        response = requests.get(
            f"http://{link}/myteam-config.json",
            params={"domain": domain},
            timeout=10,
            verify=False,
        )

        if response.status_code != 200:
            pytest.fail("Failed to get config")

    if response is not None:
        response.raise_for_status()
        return response.json()

    else:
        raise ValueError


def get_imqa_config(ENV_PLATFORM, SUPPLY_URL):
    try:
        response = requests.get(
            url=f"{SUPPLY_URL}/config.e2e/{ENV_PLATFORM}",
            timeout=5,
            verify=False,
        )

        response.raise_for_status()

        return response.json()
    except Exception as error:
        log.error(error)
        response = requests.get(
            url=f"http://100.70.81.177/api/config.e2e/{ENV_PLATFORM}",
            headers={
                "X-Token": "X-Tests",
            },
            timeout=5,
            verify=False,
        )

        response.raise_for_status()

        return response.json()


def get_account(template: str) -> str:
    number = random.randint(1, 51)
    number = f"00{number}" if number < 10 else f"0{number}"
    return template.format(number)


def get_vip_one_account() -> str:
    number = str(random.randint(1, 51))
    return f"autotest.vip.1.{number}@autotest.clients"


def get_vip_two_account() -> str:
    number = str(random.randint(1, 51))
    return f"autotest.vip.2.{number}@autotest.clients"


def get_account_alter(domain: str) -> str:
    number = str(random.randint(1, 51))
    if len(number) < 2:
        number = f"0{number}"
    return f"u0{number}@{domain}"


def get_vip_one_account_alter(domain: str) -> str:
    number = str(random.randint(1, 51))
    return f"u{number}@{domain}"


def get_vip_two_account_alter(domain: str) -> str:
    number = str(random.randint(1, 51))
    return f"u{number}@{domain}"


@pytest.fixture(scope="session")
def sandbox_account_template(pytestconfig: Config):
    return pytestconfig.getoption("--sb-account-template")


@pytest.fixture(scope="session")
def sandbox_account_fix_otp(pytestconfig: Config):
    return pytestconfig.getoption("--sb-account-fix-otp")


@allure.title("Получение сессии supply-сервера")
@pytest.fixture(scope="session")
def supply_session(ENV_PLATFORM, SANDBOX, api_version, SUPPLY_URL, USE_SSO, DOMAIN_PAID):
    if (
        ENV_PLATFORM in ["SANDBOX", "PRE_TARM", "PRE_VKTI", "VKTI", "PRE_SAAS"]
        or (ENV_PLATFORM == "SAAS" and USE_SSO)
        or (ENV_PLATFORM == "SAAS" and DOMAIN_PAID)
    ):
        if os.getenv("PUPPET_TESTS"):
            domain = get_config(SANDBOX).get("api-urls").get("main-api").replace("https://u-", "")
        else:
            domain = SANDBOX

        with SupplySession(
            environment=ENV_PLATFORM,
            domain=domain,
            api_version=api_version,
            test_platform="IMSERVER",
            max_accounts_count=50,
            supply_url=SUPPLY_URL,
        ) as sup_session:
            yield sup_session
    else:
        yield


@allure.title("Получение сессии supply-сервера")
@pytest.fixture(scope="session")
def supply_session_isolation(ENV_PLATFORM, SANDBOX, api_version, SUPPLY_URL, USE_SSO, DOMAIN_PAID):
    if ENV_PLATFORM in ["PRE_SAAS", "SAAS"]:
        if os.getenv("PUPPET_TESTS"):
            domain = get_config(SANDBOX).get("api-urls").get("main-api").replace("https://u-", "")
        else:
            domain = SANDBOX

        with SupplySession(
            environment=ENV_PLATFORM,
            domain=domain,
            api_version=api_version,
            test_platform="IMSERVER",
            max_accounts_count=50,
            supply_url=SUPPLY_URL,
        ) as sup_session:
            yield sup_session
    else:
        yield


@allure.title("Получение конфигурации автотестов")
@pytest.fixture(scope="session")
def get_myteam_config(
    ENV_PLATFORM,
    USE_SSO,
    DOMAIN_PAID,
    SANDBOX,
    IGNORE_CONFIG,
    logger,
    pytestconfig,
    alter_sandbox,
    sandbox_account_template,
    sandbox_account_fix_otp,
    # init_account_db,
    supply_session,
    SUPPLY_URL,
):
    if (
        ENV_PLATFORM in ["SANDBOX", "PRE_TARM", "PRE_VKTI", "VKTI", "PRE_SAAS"]
        or (ENV_PLATFORM == "SAAS" and USE_SSO)
        or (ENV_PLATFORM == "SAAS" and DOMAIN_PAID)
    ):
        if os.getenv("PUPPET_TESTS", False):
            sandbox_config = get_config(SANDBOX)
        elif ENV_PLATFORM in ["PRE_VKTI", "VKTI"]:
            sandbox_config = get_config("u.internal.myteam.mail.ru")
        elif ENV_PLATFORM in ["PRE_SAAS", "SAAS"] and DOMAIN_PAID:
            sandbox_config = get_config_saas(link="u.internal.myteam.mail.ru", domain=DOMAIN_PAID)
        elif ENV_PLATFORM in ["PRE_SAAS", "SAAS"]:
            account = get_imqa_config(ENV_PLATFORM, SUPPLY_URL)
            domain = account["accounts"][0]["username"].split("@")[1]
            sandbox_config = get_config_saas(link="u.internal.myteam.mail.ru", domain=domain)
        else:
            sandbox_config = supply_session.get_myteam_config()

    elif ENV_PLATFORM in ["TARM"]:
        config = get_imqa_config(ENV_PLATFORM, SUPPLY_URL)
        sandbox_config = requests.get(url=config["myteam-config.json.url"]).json()
    elif ENV_PLATFORM in ["PRE_SAAS", "SAAS"]:
        account = get_imqa_config(ENV_PLATFORM, SUPPLY_URL)
        domain = account["accounts"][0]["username"].split("@")[1]
        sandbox_config = get_config_saas(link="u.internal.myteam.mail.ru", domain=domain)
    else:
        raise ValueError(f"Unknown env: {ENV_PLATFORM}")

    return sandbox_config


@allure.title("Получение конфигурации автотестов")
@pytest.fixture(scope="session")
def get_myteam_config_admin(
    ENV_PLATFORM,
    USE_SSO,
    DOMAIN_PAID,
    SANDBOX,
    IGNORE_CONFIG,
    logger,
    pytestconfig,
    alter_sandbox,
    sandbox_account_template,
    sandbox_account_fix_otp,
    # init_account_db,
    supply_session,
    SUPPLY_URL,
):
    if ENV_PLATFORM in ["SANDBOX", "PRE_TARM", "PRE_VKTI", "VKTI", "PRE_SAAS"]:
        if os.getenv("PUPPET_TESTS", False):
            sandbox_config = get_config(SANDBOX)
        elif ENV_PLATFORM in ["PRE_VKTI", "VKTI"]:
            sandbox_config = get_config("u.internal.myteam.mail.ru")
        else:
            sandbox_config = supply_session.get_myteam_config()
        accounts_data = {
            "im_api": sandbox_config,
            "accounts": [supply_session.acquire_account(as_dict=True, is_admin=True)],
        }
        for account in accounts_data["accounts"]:
            account["api_url"] = account["api_url"].rstrip("/")  # noqa
            account["binary_api_url"] = account["binary_api_url"].rstrip("/")  # noqa

    elif ENV_PLATFORM in ["TARM", "SAAS"]:
        accounts_data = get_imqa_config(ENV_PLATFORM, SUPPLY_URL)

        accounts_data = requests.get(accounts_data["myteam-config.json.url"]).json()

    else:
        raise ValueError(f"Unknown env: {ENV_PLATFORM}")

    return accounts_data


@pytest.fixture(scope="session")
def myteam_config(get_myteam_config, ENV_PLATFORM):
    return get_myteam_config


@allure.title("Получение параметра ENV_PLATFORM из -m")
@pytest.fixture(scope="session")
def ENV_PLATFORM(pytestconfig: Config) -> EnvironmentType:
    env = pytestconfig.getoption("-m")

    if "SANDBOX" in env:
        return "SANDBOX"

    elif "ICQ" in env:
        return "ICQ"

    elif "PRE_VKTI" in env:
        return "PRE_VKTI"

    elif "VKTI" in env:
        return "VKTI"

    elif "PRE_TARM" in env:
        return "PRE_TARM"

    elif "TARM" in env:
        return "TARM"

    elif "PRE_SAAS" in env:
        return "PRE_SAAS"

    elif "SAAS" in env:
        return "SAAS"
    else:
        raise ValueError(f"Unknown env value: {env}")


@allure.title("Получение параметра --sandbox")
@pytest.fixture(scope="session")
def SANDBOX(pytestconfig: Config) -> str:
    return pytestconfig.getoption("--sandbox")


@allure.title("Получение параметра --slow")
@pytest.fixture(scope="session")
def SLOW(pytestconfig: Config):
    result = pytestconfig.getoption("--slow")

    return HERE_SLOW or result


@allure.title("Игнорировать accounts.json")
@pytest.fixture(scope="session")
def IGNORE_CONFIG(pytestconfig: Config):
    return pytestconfig.getoption("--ignore-config")


@allure.title("Получение аккаунтов для автотестов")
@pytest.fixture(scope="session")
def accounts_data_admin(get_myteam_config_admin):
    return get_myteam_config_admin["accounts"]


@allure.title("Получение версии API в тестах")
@pytest.fixture(scope="session")
def api_version(
    ENV_PLATFORM,
    pytestconfig: Config,
    SANDBOX,
):
    if pytestconfig.getoption("--api"):
        api_ver = pytestconfig.getoption("--api")
    elif get_config(SANDBOX).get("api-version"):
        api_ver = get_config(SANDBOX).get("api-version")
    else:
        api_ver = 120
    return api_ver


@allure.title("Получение настроек IMAP")
@pytest.fixture(scope="session")
def imap_serv(
    get_myteam_config,
    ENV_PLATFORM,
):
    return get_myteam_config.get("imap")


@allure.title("Получение API-URL")
@pytest.fixture(scope="session")
def main_api(get_myteam_config, ENV_PLATFORM):
    myteam_config_url = get_myteam_config.get("myteam-config.json.url", None)
    if ENV_PLATFORM in ["TARM", "SAAS"] and myteam_config_url is not None:
        get_myteam_config = requests.get(get_myteam_config["myteam-config.json.url"]).json()

    if "api-urls" in get_myteam_config:
        yield get_myteam_config["api-urls"]["main-api"]
    else:
        yield get_myteam_config["api_urls"]["main_api"]


@allure.title("Получение Binary API-URL")
@pytest.fixture(scope="session")
def binary_api(
    get_myteam_config,
    ENV_PLATFORM,
):
    myteam_config_url = get_myteam_config.get("myteam-config.json.url", None)
    if ENV_PLATFORM in ["TARM"] and myteam_config_url is not None:
        get_myteam_config = requests.get(get_myteam_config["myteam-config.json.url"]).json()

    if "api-urls" in get_myteam_config:
        yield get_myteam_config["api-urls"]["main-binary-api"]
    else:
        yield get_myteam_config["api_urls"]["binary_api"]


@allure.title("Получение Files API-URL")
@pytest.fixture(scope="session")
def files_api(
    get_myteam_config,
    ENV_PLATFORM,
):
    myteam_config_url = get_myteam_config.get("myteam-config.json.url", None)
    if ENV_PLATFORM in ["TARM"] and myteam_config_url is not None:
        get_myteam_config = requests.get(get_myteam_config["myteam-config.json.url"]).json()

    if "base-urls" in get_myteam_config:
        yield get_myteam_config["base-urls"]["files-parsing"]["main"]
    elif "base_urls" in get_myteam_config:
        yield get_myteam_config["base_urls"]["files-parsing"]["main"]
    elif "templates-urls" in get_myteam_config:
        yield get_myteam_config["templates-urls"]["files-parsing"]
    elif "templates_urls" in get_myteam_config:
        yield get_myteam_config["templates_urls"]["files-parsing"]
    else:
        raise ValueError("Can't get files-parsing URL")


@allure.title("Получение ID и URL стикера")
@pytest.fixture(
    scope="session",
    params=pathlib.Path("support").joinpath("files").joinpath("common").glob("*.webp"),
    ids=lambda x: x.name,
)
def sticker_send(
    auth_account,
    request,
):
    return auth_account.upload_file(request.param)


@allure.title("Получение URL стикера")
@pytest.fixture(scope="session")
def sticker(
    sticker_send,
):
    _, static_url = sticker_send

    return static_url


@allure.title("Получение ID стикера")
@pytest.fixture(scope="session")
def sticker_id(
    sticker_send,
):
    s, _ = sticker_send

    return s


@allure.title("Получение ID и URL на фото")
@pytest.fixture(
    scope="session",
    params=pathlib.Path("support").joinpath("files").joinpath("common").glob("download.png"),
    ids=lambda x: x.name,
)
def photo_upload(auth_account, request):
    return auth_account.upload_file(request.param)


@allure.title("Получение URL фото")
@pytest.fixture(scope="session")
def photo(
    photo_upload,
):
    _, static_url = photo_upload

    return static_url


@allure.title("Получение ID фото")
@pytest.fixture(scope="session")
def photo_id(photo_upload):
    file_id, _ = photo_upload

    return file_id


@allure.title("Получение ID и URL на фото")
@pytest.fixture(
    scope="session",
    params=pathlib.Path("support").joinpath("files").joinpath("orgstructure").joinpath("positive").glob("*.xlsx"),
    ids=lambda x: x.name,
)
def excel_upload_positive(auth_account, request):
    return auth_account.upload_file(request.param)


@allure.title("Получение URL фото")
@pytest.fixture(scope="session")
def excel_posotive(
    excel_upload_positive,
):
    _, static_url = excel_upload_positive

    return static_url


@allure.title("Получение ID фото")
@pytest.fixture(scope="session")
def excel_id_positive(excel_upload_positive):
    file_id, _ = excel_upload_positive

    return file_id


@allure.title("Получение ID и URL на фото")
@pytest.fixture(
    scope="session",
    params=pathlib.Path("support").joinpath("files").joinpath("orgstructure").joinpath("negative").glob("*.xlsx"),
    ids=lambda x: x.name,
)
def excel_upload_negative(auth_account, request):
    return auth_account.upload_file(request.param)


@allure.title("Получение URL фото")
@pytest.fixture(scope="session")
def excel_negative(
    excel_upload_negative,
):
    _, static_url = excel_upload_negative

    return static_url


@allure.title("Получение ID фото")
@pytest.fixture(scope="session")
def excel_id_negative(excel_upload_negative):
    file_id, _ = excel_upload_negative

    return file_id


@allure.title("Получение ID и URL голосового сообщения")
@pytest.fixture(
    scope="session",
    params=pathlib.Path("support").joinpath("files").joinpath("common").glob("*.aac"),
    ids=lambda x: x.name,
)
def voice_send(
    auth_account,
    request,
):
    return auth_account.upload_file(request.param, _type="ptt")


@allure.title("Получение URL голосового сообщения")
@pytest.fixture(scope="session")
def voice(voice_send):
    _, static_url = voice_send

    return static_url


@allure.title("Получение ID голосового сообщения")
@pytest.fixture(scope="session")
def voice_id(voice_send):
    voice_file_id, _ = voice_send

    return voice_file_id


@allure.title("Получение ID файла с логами")
@pytest.fixture(
    scope="session",
    params=pathlib.Path("support").joinpath("files").joinpath("common").glob("*.zip"),
    ids=lambda x: x.name,
)
def logs_file(
    auth_account,
    request,
):
    logs_id, _ = auth_account.upload_file(request.param)

    return logs_id


@allure.title("Получение URL WebIM")
@pytest.fixture(scope="session")
def web_url(get_myteam_config, ENV_PLATFORM):
    myteam_config_url = get_myteam_config.get("myteam-config.json.url", None)
    if ENV_PLATFORM in ["TARM"] and myteam_config_url is not None:
        get_myteam_config = requests.get(get_myteam_config["myteam-config.json.url"]).json()

    if "templates-urls" in get_myteam_config:
        yield get_myteam_config["templates-urls"]["web-view"].replace("/view.html", "")
    else:
        yield get_myteam_config["template_urls"]["web-view"].replace("/view.html", "")


@allure.title("Получение URL DI")
@pytest.fixture(scope="session", params=["di", "di-dark"])
def di_url(get_myteam_config, ENV_PLATFORM, request) -> str:
    if "templates-urls" in get_myteam_config:
        url = get_myteam_config["templates-urls"][request.param]
    else:
        url = get_myteam_config["template_urls"][request.param]

    return url[: len(url) - 10]


@allure.title("Получение URL proxy")
@pytest.fixture(scope="session")
def PROXY(pytestconfig):
    return pytestconfig.getoption("--proxy")


@pytest.fixture(
    scope="session",
    params=pathlib.Path("support").joinpath("files").joinpath("antivirus").glob("*.*"),
    ids=lambda x: x.name,
)
def antivirus_file(request) -> pathlib.Path:
    return request.param


@pytest.fixture(scope="session")
def uploaded_antivirus_file_url(auth_account, antivirus_file) -> str:
    _, static_url = auth_account.upload_file(
        str(antivirus_file.absolute()),
    )
    return static_url


@pytest.fixture(
    scope="session",
    params=pathlib.Path("support").joinpath("files").joinpath("common").glob("*.*"),
    ids=lambda x: x.name,
)
def common_file(request) -> pathlib.Path:
    return request.param


@pytest.fixture(
    scope="session",
    params=pathlib.Path("support").joinpath("files").joinpath("common").glob("*.jpg"),
    ids=lambda x: x.name,
)
def limited_common_file(request) -> pathlib.Path:
    return request.param


@pytest.fixture(scope="session")
def uploaded_common_file_url(auth_account, common_file) -> str:
    _, static_url = auth_account.upload_file(
        str(common_file.absolute()),
    )
    return static_url


@pytest.fixture(scope="session")
def limited_uploaded_common_file_url(auth_account, limited_common_file) -> str:
    _, static_url = auth_account.upload_file(
        str(limited_common_file.absolute()),
    )
    return static_url


@pytest.fixture(
    scope="session",
    params=pathlib.Path("support").joinpath("files").joinpath("for_miniapps_tests").glob("*.*"),
    ids=lambda x: x.name,
)
def for_miniapps_tests_file(request) -> pathlib.Path:
    return request.param


@pytest.fixture(scope="session")
def uploaded_for_miniapps_tests_file_url(auth_account, for_miniapps_tests_file) -> str:
    _, static_url = auth_account.upload_file(
        str(for_miniapps_tests_file.absolute()),
    )
    return static_url


@pytest.fixture(
    scope="session",
    params=pathlib.Path("support").joinpath("files").joinpath("speechtotext").glob("*.*"),
    ids=lambda x: x.name,
)
def speechtottext_file(request) -> pathlib.Path:
    return request.param


@pytest.fixture(scope="session")
def uploaded_speechtottext_file(auth_account, speechtottext_file) -> dict:
    return auth_account.upload_file(
        file_path=speechtottext_file,
        _type="ptt",
    )


@pytest.fixture(scope="session")
def uploaded_speechtottext_file_id(auth_account, uploaded_speechtottext_file) -> str:
    file_id, _ = uploaded_speechtottext_file
    return file_id


@pytest.fixture(scope="session")
def uploaded_speechtottext_file_url(auth_account, uploaded_speechtottext_file) -> str:
    _, url = uploaded_speechtottext_file
    return url


@pytest.fixture(
    scope="session",
    params=pathlib.Path("support").joinpath("files").joinpath("with_preview").glob("*.*"),
    ids=lambda x: x.name,
)
def with_preview_file(request) -> pathlib.Path:
    return request.param


@pytest.fixture(scope="session")
def uploaded_with_preview_file_url(auth_account, with_preview_file) -> str:
    _, static_url = auth_account.upload_file(
        str(with_preview_file.absolute()),
    )
    return static_url


@allure.title("Получение сессии для запросов")
@pytest.fixture(scope="session")
def set_rate_limit(main_api, api_version):
    def _set_limit(session, url: str, limit_per_second: Optional[int] = None, limit_per_minute: Optional[int] = None):
        if limit_per_second and limit_per_minute:
            adapter = LimiterAdapter(
                per_second=limit_per_second, bucket_class=SQLiteBucket, per_minute=limit_per_minute, per_host=True
            )
        elif limit_per_second:
            adapter = LimiterAdapter(per_second=limit_per_second, bucket_class=SQLiteBucket, per_host=True)
        elif limit_per_minute:
            adapter = LimiterAdapter(per_minute=limit_per_minute, bucket_class=SQLiteBucket, per_host=True)

        session.mount("/".join([f"{main_api}/api/v{api_version}", url]), adapter)

    return _set_limit


@pytest.fixture(scope="session")
def get_second_account(supply_session, DOMAIN_PAID, USE_SSO, ENV_PLATFORM, USE_SWA) -> dict[str, str]:
    is_admin = ENV_PLATFORM == "SANDBOX"
    is_domain = DOMAIN_PAID

    if (
        ENV_PLATFORM in ["SANDBOX", "PRE_VKTI", "VKTI", "PRE_TARM", "PRE_SAAS"]
        or (ENV_PLATFORM == "SAAS" and USE_SSO)
        or (ENV_PLATFORM == "SAAS" and DOMAIN_PAID)
        or (ENV_PLATFORM in ["TARM", "PRE_TARM"] and USE_SWA)
    ):
        account = supply_session.acquire_account(as_dict=True, sso=USE_SSO, user_domain=is_domain, is_admin=is_admin)

        return account
    else:
        return False


@allure.title("Получение сессии для запросов")
@pytest.fixture(scope="session")
def session(
    main_api,
    binary_api,
    files_api,
    swagger_http_spy,
    web_url,
    PROXY,
    set_rate_limit,
):
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "QtWebEngine/6.8.3 "
        "Chrome/122.0.0.0 Safari/537.36",
        "Referer": web_url,
        "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "macOS",
    }
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

    yield session

    session.close()


@pytest.fixture(scope="session")
def admin_url(main_api):
    return main_api.replace("u", "admin", 1)


@pytest.fixture(scope="session")
def admin_account(admin_url, accounts_data_admin, get_myteam_config_admin, ENV_PLATFORM, session):
    account = accounts_data_admin[0]

    return AdminClient(
        uin=account.get("uin") or account.get("username"),
        email_url=account["email_url"],
        email_password=account["email_password"],
        env=ENV_PLATFORM,
        api_url=admin_url,
        session=session,
    )


@allure.title("Получение сессии для запросов")
@pytest.fixture(scope="session")
def auth_account_session(
    main_api,
    binary_api,
    files_api,
    swagger_http_spy,
    web_url,
    PROXY,
    set_rate_limit,
):
    with requests.Session() as session:
        session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "QtWebEngine/6.8.3 "
            "Chrome/122.0.0.0 Safari/537.36",
            "Referer": web_url,
            "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS",
        }
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

        yield session


@allure.title("Получение клиента №1")
@pytest.fixture(scope="session")
def auth_account(
    ENV_PLATFORM,
    main_api,
    binary_api,
    api_version,
    auth_account_session,
    imap_serv,
    logger,
    alter_sandbox,
    USE_SSO,
    USE_SWA,
    get_myteam_config,
    supply_session,
    DOMAIN_PAID,
    get_second_account,
    SUPPLY_URL,
):
    if get_second_account:
        api_ver = (get_second_account.pop("api_ver", None), get_second_account)
        api_ver = api_version if api_version else api_ver
        get_second_account.pop("org_struct_admin_token", None)

        main_account = DesktopClient(
            session=auth_account_session,
            polling=False,
            api_ver=api_ver,
            **get_second_account,
        )

    else:
        config = get_imqa_config(ENV_PLATFORM, SUPPLY_URL)
        imap_serv = config.get("imap", None)
        account = config["accounts"][0]
        main_account = DesktopClient(
            uin=account.get("uin") or account.get("username"),
            session=auth_account_session,
            api_url=main_api,
            binary_api_url=binary_api,
            api_ver=api_version,
            env=ENV_PLATFORM,
            email_password=account["password"],
            email_url=imap_serv,
            polling=False,
        )

    main_account.restore_privacy_settings()

    yield main_account

    if ENV_PLATFORM not in ["SANDBOX", "PRE_TARM", "PRE_VKTI", "VKTI", "PRE_SAAS"]:
        main_account.clean_account()


@allure.title("Получение сессии для запросов")
@pytest.fixture(scope="session")
def second_auth_account_session(
    main_api,
    binary_api,
    files_api,
    swagger_http_spy,
    web_url,
    PROXY,
    set_rate_limit,
):
    with requests.Session() as session:
        session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "QtWebEngine/6.8.3 "
            "Chrome/122.0.0.0 Safari/537.36",
            "Referer": web_url,
            "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS",
        }
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

        yield session


@allure.title("Получение второго инстанса для клиента №1")
@pytest.fixture(scope="session")
def second_auth_account(
    ENV_PLATFORM,
    main_api,
    binary_api,
    api_version,
    second_auth_account_session,
    imap_serv,
    logger,
    alter_sandbox,
    USE_SSO,
    USE_SWA,
    get_myteam_config,
    supply_session,
    DOMAIN_PAID,
    get_second_account,
    SUPPLY_URL,
):
    if get_second_account:
        api_ver = (get_second_account.pop("api_ver", None), get_second_account)
        api_ver = api_version if api_version else api_ver

        get_second_account.pop("org_struct_admin_token", None)
        main_account = DesktopClient(
            session=second_auth_account_session,
            polling=False,
            api_ver=api_ver,
            **get_second_account,
        )

    else:
        config = get_imqa_config(ENV_PLATFORM, SUPPLY_URL)
        imap_serv = config.get("imap", None)
        account = config["accounts"][0]
        main_account = DesktopClient(
            uin=account.get("uin") or account.get("username"),
            session=second_auth_account_session,
            api_url=main_api,
            binary_api_url=binary_api,
            api_ver=api_version,
            env=ENV_PLATFORM,
            email_password=account["password"],
            email_url=imap_serv,
            polling=False,
        )

    main_account.restore_privacy_settings()

    yield main_account

    if ENV_PLATFORM not in ["SANDBOX", "PRE_TARM", "PRE_VKTI", "VKTI", "PRE_SAAS"]:
        main_account.clean_account()


@allure.title("Получение сессии для запросов")
@pytest.fixture(scope="session")
def opponent_account_session(
    main_api,
    binary_api,
    files_api,
    swagger_http_spy,
    web_url,
    PROXY,
    set_rate_limit,
):
    with requests.Session() as session:
        session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "QtWebEngine/6.8.3 "
            "Chrome/122.0.0.0 Safari/537.36",
            "Referer": web_url,
            "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS",
        }
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

        yield session


@allure.title("Получение клиента №2")
@pytest.fixture(scope="session")
def opponent_account(
    main_api,
    binary_api,
    api_version,
    opponent_account_session,
    ENV_PLATFORM,
    imap_serv,
    logger,
    alter_sandbox,
    USE_SSO,
    USE_SWA,
    get_myteam_config,
    supply_session,
    DOMAIN_PAID,
    SUPPLY_URL,
):
    is_admin = ENV_PLATFORM == "SANDBOX"
    is_domain = DOMAIN_PAID

    if (
        ENV_PLATFORM in ["SANDBOX", "PRE_VKTI", "VKTI", "PRE_TARM", "PRE_SAAS"]
        or (ENV_PLATFORM == "SAAS" and USE_SSO)
        or (ENV_PLATFORM == "SAAS" and DOMAIN_PAID)
        or (ENV_PLATFORM in ["TARM", "PRE_TARM"] and USE_SWA)
    ):
        account = supply_session.acquire_account(as_dict=True, sso=USE_SSO, user_domain=is_domain, is_admin=is_admin)
        api_ver = account.pop("api_ver", None)
        api_ver = api_version if api_version else api_ver

        account.pop("org_struct_admin_token", None)
        main_account = DesktopClient(session=opponent_account_session, polling=False, api_ver=api_ver, **account)

    else:
        config = get_imqa_config(ENV_PLATFORM, SUPPLY_URL)
        imap_serv = config.get("imap", None)
        account = config["accounts"][1]
        main_account = DesktopClient(
            uin=account.get("uin") or account.get("username"),
            session=opponent_account_session,
            api_url=main_api,
            binary_api_url=binary_api,
            api_ver=api_version,
            env=ENV_PLATFORM,
            email_password=account["password"],
            email_url=imap_serv,
            polling=False,
        )

    main_account.restore_privacy_settings()

    yield main_account

    if ENV_PLATFORM not in ["SANDBOX", "PRE_TARM", "PRE_VKTI", "VKTI", "PRE_SAAS"]:
        main_account.clean_account()


@allure.title("Получение сессии для запросов")
@pytest.fixture(scope="session")
def third_account_session(
    main_api,
    binary_api,
    files_api,
    swagger_http_spy,
    web_url,
    PROXY,
    set_rate_limit,
):
    with requests.Session() as session:
        session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "QtWebEngine/6.8.3 "
            "Chrome/122.0.0.0 Safari/537.36",
            "Referer": web_url,
            "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS",
        }
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

        yield session


@allure.title("Получение клиента №3")
@pytest.fixture(scope="session")
def third_account(
    ENV_PLATFORM,
    main_api,
    binary_api,
    api_version,
    third_account_session,
    imap_serv,
    logger,
    alter_sandbox,
    USE_SSO,
    USE_SWA,
    get_myteam_config,
    supply_session,
    DOMAIN_PAID,
    SUPPLY_URL,
):
    is_admin = ENV_PLATFORM == "SANDBOX"
    is_domain = DOMAIN_PAID

    try:
        account = supply_session.acquire_account(as_dict=True, sso=USE_SSO, user_domain=is_domain, is_admin=is_admin)
    except (IndexError, AttributeError):
        pytest.skip(f"{ENV_PLATFORM}: There is no third account")

    if (
        ENV_PLATFORM in ["SANDBOX", "PRE_VKTI", "VKTI", "PRE_TARM", "PRE_SAAS"]
        or (ENV_PLATFORM == "SAAS" and USE_SSO)
        or (ENV_PLATFORM in ["TARM", "PRE_TARM"] and USE_SWA)
    ):
        api_ver = (account.pop("api_ver", None), account)
        api_ver = api_version if api_version else api_ver

        account.pop("org_struct_admin_token", None)
        main_account = DesktopClient(session=third_account_session, polling=False, api_ver=api_ver, **account)

    else:
        config = get_imqa_config(ENV_PLATFORM, SUPPLY_URL)
        imap_serv = config.get("imap", None)
        account = config["accounts"][2]
        main_account = DesktopClient(
            uin=account.get("uin") or account.get("username"),
            session=third_account_session,
            api_url=main_api,
            binary_api_url=binary_api,
            api_ver=api_version,
            env=ENV_PLATFORM,
            email_password=account["password"],
            email_url=imap_serv,
            polling=False,
        )

    main_account.restore_privacy_settings()

    yield main_account

    if ENV_PLATFORM not in ["SANDBOX", "PRE_TARM", "PRE_VKTI", "VKTI", "PRE_SAAS"]:
        main_account.clean_account()


@allure.title("Получение сессии 1 для запросов Клиента 4")
@pytest.fixture(scope="session")
def fourth_account_first_session(
    main_api,
    binary_api,
    files_api,
    swagger_http_spy,
    web_url,
    PROXY,
    set_rate_limit,
):
    with requests.Session() as session:
        session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "QtWebEngine/6.8.3 "
            "Chrome/122.0.0.0 Safari/537.36",
            "Referer": web_url,
            "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS",
        }
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

        yield session


@allure.title("Получение сессии 2 для запросов Клиента 4")
@pytest.fixture(scope="session")
def fourth_account_second_session(
    main_api,
    binary_api,
    files_api,
    swagger_http_spy,
    web_url,
    PROXY,
    set_rate_limit,
):
    with requests.Session() as session:
        session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "QtWebEngine/6.8.3 "
            "Chrome/122.0.0.0 Safari/537.36",
            "Referer": web_url,
            "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "macOS",
        }
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

        yield session


@allure.title("Получение клиента 4 (для dropSessions)")
@pytest.fixture(scope="session")
def fourth_account(
    ENV_PLATFORM,
    main_api,
    binary_api,
    api_version,
    fourth_account_first_session,
    imap_serv,
    logger,
    alter_sandbox,
    USE_SSO,
    USE_SWA,
    get_myteam_config,
    supply_session,
    DOMAIN_PAID,
    get_second_account,
    SUPPLY_URL,
):
    if get_second_account:
        api_ver = (get_second_account.pop("api_ver", None), get_second_account)
        api_ver = api_version if api_version else api_ver

        get_second_account.pop("org_struct_admin_token", None)
        fourth_account = DesktopClient(
            session=fourth_account_first_session, polling=False, api_ver=api_ver, **get_second_account
        )
    else:
        config = get_imqa_config(ENV_PLATFORM, SUPPLY_URL)
        imap_serv = config.get("imap", None)
        account = config["accounts"][3]
        fourth_account = DesktopClient(
            uin=account.get("uin") or account.get("username"),
            session=fourth_account_first_session,
            api_url=main_api,
            binary_api_url=binary_api,
            api_ver=api_version,
            env=ENV_PLATFORM,
            email_password=account["password"],
            email_url=imap_serv,
            polling=False,
        )

    fourth_account.restore_privacy_settings()

    yield fourth_account

    if ENV_PLATFORM not in ["SANDBOX", "PRE_TARM", "PRE_VKTI", "VKTI", "PRE_SAAS"]:
        fourth_account.clean_account()


@allure.title("Получение второго инстанса для клиента 4 (для dropSessions)")
@pytest.fixture(scope="session")
def fourth_account_second_instance(
    ENV_PLATFORM,
    main_api,
    binary_api,
    api_version,
    fourth_account_second_session,
    imap_serv,
    logger,
    alter_sandbox,
    USE_SSO,
    USE_SWA,
    get_myteam_config,
    supply_session,
    DOMAIN_PAID,
    get_second_account,
    SUPPLY_URL,
):
    if get_second_account:
        api_ver = (get_second_account.pop("api_ver", None), get_second_account)
        api_ver = api_version if api_version else api_ver

        get_second_account.pop("org_struct_admin_token", None)
        main_account = DesktopClient(
            session=fourth_account_second_session, polling=False, api_ver=api_ver, **get_second_account
        )
    else:
        config = get_imqa_config(ENV_PLATFORM, SUPPLY_URL)
        imap_serv = config.get("imap", None)
        account = config["accounts"][3]
        main_account = DesktopClient(
            uin=account.get("uin") or account.get("username"),
            session=fourth_account_second_session,
            api_url=main_api,
            binary_api_url=binary_api,
            api_ver=api_version,
            env=ENV_PLATFORM,
            email_password=account["password"],
            email_url=imap_serv,
            polling=False,
        )

    main_account.restore_privacy_settings()

    yield main_account

    if ENV_PLATFORM not in ["SANDBOX", "PRE_TARM", "PRE_VKTI", "VKTI", "PRE_SAAS"]:
        main_account.clean_account()


@allure.title("Получение ipros клиента")
@pytest.fixture(scope="session")
def ipros_client(
    auth_account,
):
    return IprosClient(auth_account)


@allure.title("Получение логгера")
@pytest.fixture(scope="session")
def logger():
    global log

    return log


@allure.title("Подготовка чат только администратор")
@pytest.fixture(scope="session")
def prepare_test_chat_admin_only(
    request,
    opponent_account,
    auth_account,
):
    with allure.step("Создаем тестовую группу"):
        group = auth_account.create_chat(
            f"Test group - {request.node.name}",
        )

    return auth_account, opponent_account, group


@allure.title("Подготовка тестовых чатов")
@pytest.fixture(scope="session")
def prepare_test_chats(
    request,
    opponent_account,
    auth_account,
):
    with allure.step("Создаем тестовую группу"):
        group = auth_account.create_chat(
            f"Test group - {request.node.name}",
            members=[opponent_account],
        )

    with allure.step("Создаем тестовый канал"):
        channel = auth_account.create_chat(
            f"Test channel - {request.node.name}",
            defaultRole="readonly",
            members=[opponent_account],
        )

    return auth_account, opponent_account, group, channel


@allure.title("Подготовка тестовых чатов для администрирования")
@pytest.fixture(scope="session")
def prepare_test_chats_admin(
    request,
    opponent_account,
    auth_account,
):
    with allure.step("Создаем тестовую группу"):
        group = auth_account.create_chat(
            f"Test group - {request.node.name}",
            members=[opponent_account],
        )

    with allure.step("Создаем тестовый канал"):
        channel = auth_account.create_chat(
            f"Test channel - {request.node.name}",
            defaultRole="readonly",
            members=[opponent_account],
        )

    return group, channel


@allure.title("Подготовка тестовых чатов для администрирования")
@pytest.fixture(scope="session")
def prepare_test_chats_admin_readonly(
    request,
    opponent_account,
    auth_account,
):
    with allure.step("Создаем тестовую группу"):
        group = auth_account.create_chat(
            f"Test group - {request.node.name}",
            members=[opponent_account],
        )

    with allure.step("Создаем тестовый канал"):
        channel = auth_account.create_chat(
            f"Test channel - {request.node.name}",
            defaultRole="readonly",
            members=[opponent_account],
        )

    return group, channel


@allure.title("Подготовка тестовых чатов для передачи прав")
@pytest.fixture(scope="session")
def prepare_test_chats_owner_auto_reassign(
    request,
    opponent_account,
    auth_account,
):
    with allure.step("Создаем тестовую группу"):
        group = auth_account.create_chat(
            f"Test group - {request.node.name}",
            members=[opponent_account],
            joinModeration=False,
            public=True,
        )

    with allure.step("Создаем тестовый канал"):
        channel = auth_account.create_chat(
            f"Test channel - {request.node.name}",
            defaultRole="readonly",
            members=[opponent_account],
            joinModeration=False,
            public=True,
        )

    return group, channel


@pytest.fixture
def fetch_events_till_empty_queue(
    auth_account,
    opponent_account,
    logger,
    event_filter,
    fetch_until_empty_answer,
):
    with allure.step(f"Получаем последние события для {auth_account}"):
        fetch_until_empty_answer(auth_account)

    with allure.step(f"Получаем последние события для {opponent_account}"):
        fetch_until_empty_answer(opponent_account)

    return auth_account, opponent_account


@pytest.fixture(scope="session")
def start_bot(auth_account, bot_class):
    with allure.step("Отправляем /start боту"):
        RETRIES = 6

        for i in range(RETRIES):
            try:
                response = auth_account.rapi_startBot(
                    bot=bot_class.uin,
                    startParameter="test",
                )

                if response["status"]["code"] == 20000:
                    break

            except Exception as error:
                if i < RETRIES:
                    time.sleep(i)
                    continue
                else:
                    raise error

        auth_account.send_basic_message(
            sn=bot_class.uin,
            text="Test",
        )


def pytest_addoption(parser) -> None:
    """!
    Расширенные настройки Pytest
    @ingroup Framework
    @namespace conftest
    @memberof conftest
    """
    parser.getgroup("autotests").addoption(
        "--sandbox",
        action="store",
        default="stage-stable.v3.im-sandbox.devmail.ru",
        help="Базовый URL тестируемого песка",
    )
    parser.getgroup("autotests").addoption(
        "--sb-account-template",
        action="store",
        default="autotest{0}@autotest.clients",
        help="[SANDBOX] Шаблон аккаунта для автотестов",
    )
    parser.getgroup("autotests").addoption(
        "--sb-account-fix-otp",
        action="store",
        default="ONPREM",
        help="[SANDBOX] Фиксированный OTP-код аккаунта",
    )
    parser.getgroup("autotests").addoption(
        "--slow",
        action="store_true",
        help="Замедлять тесты для обхода ошибок по рейтлимитам?",
    )
    parser.getgroup("autotests").addoption(
        "--proxy",
        action="store",
        default=None,
        help="Адрес прокси для запросов к бэкенду",
    )
    parser.getgroup("autotests").addoption(
        "--ignore-config",
        action="store_true",
        help="Игнорировать accounts/accounts.json ?",
    )
    parser.getgroup("autotests").addoption(
        "--api",
        action="store",
        default=None,
        type=int,
        help="Какую версию API использовать?",
    )
    parser.getgroup("autotests").addoption(
        "--forced-ip",
        action="store",
        default=None,
        type=str,
        help="IP адрес для подмены IP-адреса доменов приложения",
    )
    parser.getgroup("autotests").addoption(
        "--sandbox-alter",
        action="store_true",
        help="Тип аккаунта для песка",
    )
    parser.getgroup("autotests").addoption(
        "--ignore-antivirus",
        action="store_true",
        help="Пропуск автотестов на антивирус",
    )
    parser.getgroup("autotests").addoption(
        "--ignore-vip",
        action="store_true",
        help="Пропуск автотестов на VIP",
    )
    parser.getgroup("autotests").addoption(
        "--ignore-task-restrictions",
        action="store_false",
        help="Доступность задач только участникам",
    )
    parser.getgroup("autotests").addoption(
        "--libvoip-version",
        action="store",
        help="Версия VoIP клиента для ботов",
    )
    parser.getgroup("autotests").addoption(
        "--use-sso",
        action="store_true",
        help="Получить аккаунты с авторизацией через SSO",
    )
    parser.getgroup("autotests").addoption(
        "--use-swa",
        action="store_true",
        help="Получить аккаунты с авторизацией через SWA",
    )
    parser.getgroup("autotests").addoption(
        "--supply-url",
        default="https://imqa-supply.mail.msk/api",
        action="store",
        help="URL supply сервера",
    )
    parser.getgroup("autotests").addoption(
        "--dlp-system",
        action="store",
        default="",
        help="DLP system: IW(InfoWatch), SI(SearchInform), SD(Solar Dozor)",
    )
    parser.getgroup("autotests").addoption(
        "--domain-paid",
        action="store",
        default=None,
        help="Получить платные аккаунты",
    )
    parser.getgroup("autotests").addoption(
        "--dlp-config-file",
        action="store",
        default=None,
        help="Path to dlp domain config as json file",
    )
    parser.getgroup("autotests").addoption(
        "--federation-config",
        action="store",
        default=None,
        help="Hostnames and user domain configs like host1:domain12,host2:domain21",
    )

    parser.getgroup("autotests").addoption(
        "--isolation-prepared-data",
        action="store",
        default=None,
        help="Prepared data for isolation tests on PRE_SAAS",
    )


@pytest.fixture(scope="session")
def alter_sandbox(pytestconfig: Config):
    return pytestconfig.getoption("--sandbox-alter")


@pytest.fixture(scope="session")
def ignore_task_restrictions(pytestconfig: Config):
    return pytestconfig.getoption("--ignore-task-restrictions")


@allure.title("Добавляем информацию о тестовой среде")
def pytest_collection_modifyitems(config: Config, items: list[Item]) -> None:
    global HERE_SLOW
    try:
        env_option = config.getoption("-m")

        if "SANDBOX" in env_option:
            env = "SANDBOX"

        elif "PRE_VKTI" in env_option:
            env = "PRE_VKTI"

        elif "VKTI" in env_option:
            env = "VKTI"

        elif "PRE_TARM" in env_option:
            env = "PRE_TARM"

        elif "TARM" in env_option:
            env = "TARM"

        elif "PRE_SAAS" in env_option:
            env = "PRE_SAAS"

        elif "SAAS" in env_option:
            env = "SAAS"

        else:
            raise ValueError(f"Unknown env value: {env_option}")
        unstable_tests = quarantine_cl.get_unstable_tests(
            env=env, project="IMSERVER"
        )  # Получаем список ID кейсов, упавших последние 5 прогонов
    except Exception as error:
        log.error(error)
        unstable_tests = []

    for item in items:  # Проходимся по списку кейсов
        log.info(item.name)
        allure_id = get_allure_id(item)

        if (
            allure_id is not None
            and {"allure_id": allure_id, "name": item.nodeid.replace("/", ".").replace("::", "#")} in unstable_tests
        ):
            log.info(f"Skipping test with allure ID {allure_id}")
            item.add_marker(  # Проставляем skip на тесты, присутствующие в списке
                pytest.mark.skip("Skipped by TestQuarantin API service")
            )

    ALLURE_LAUNCH_ID = os.getenv("ALLURE_LAUNCH_ID")

    sandbox_url: str = config.getoption("--sandbox")

    if (
        ALLURE_LAUNCH_ID is not None
        and sandbox_url is not None
        and (sandbox_url.startswith("imdevops") or sandbox_url.startswith("imserver"))
    ):
        regexp_jira_issue_from_url = re.findall(
            r"[A-Za-z]+\-[0-9]+",
            "imdevops-4426-el7.v3.im-sandbox.devmail.ru",
        )

        JIRA_ISSUE = regexp_jira_issue_from_url[0].upper()

        requests.patch(
            url=f"https://allure.vk.team/api/rs/launch/{ALLURE_LAUNCH_ID}",
            headers={
                "Authorization": "Api-Token 8874245f-3f1e-4dcc-afb1-190679b4d36a",
            },
            json={
                "id": ALLURE_LAUNCH_ID,
                "issues": [
                    {"integrationId": 2, "name": JIRA_ISSUE},
                ],
            },
        )

    with allure.step("Добавляем environment.properties в папку с отчетом allure"):
        file_path = pathlib.Path("reports").joinpath("allure-results").joinpath("environment.properties")

        with file_path.open(mode="w") as f:
            f.write(
                "\n".join(
                    [
                        f"{key}={value}"
                        for key, value in filter(
                            lambda x: x[0]
                            in [
                                "NODE_NAME",
                                "ENV_PLATFORM",
                                "STAGE_NAME",
                                "ALLURE_PROJECT_ID",
                                "SANDBOX",
                                "JOB_NAME",
                                "API_VERSION",
                            ],
                            os.environ.items(),
                        )
                    ]
                ),
            )

    target_workspace = config.getoption("-m")

    if target_workspace.startswith("PRE_"):
        target_workspace = target_workspace.replace("PRE_", "")

    if target_workspace not in ["ICQ", "VKTI", "PRE_VKTI", "TARM", "PRE_TARM"]:
        HERE_SLOW = False

    for item in items:
        folders = item.nodeid.split("/")
        folders = folders[1 : len(folders) - 1]

        for marker in [i.replace("test_", "").upper() for i in folders]:
            mark = getattr(pytest.mark, marker)
            item.add_marker(mark)


@pytest.fixture(scope="session")
def stentor_api_url(main_api):
    return main_api.replace("u", "stentor", 1)


@pytest.fixture(scope="session")
def save_to_cloud_enabled(myteam_config):
    return myteam_config.get("save-to-cloud-enabled", False)


@pytest.fixture(scope="session")
def bots_in_threads_enabled(myteam_config):
    return myteam_config.get("bots-in-threads", False)


@pytest.fixture(scope="session")
def stentor(stentor_api_url, session):
    return StentorClient(session, api_url=stentor_api_url)


def gen_email():
    return uuid.uuid4().hex[9:] + "@autotest.clients"


@pytest.fixture
def stentor_account(auth_account, stentor, logger):
    user_info = {
        "firstName": fake.first_name(),
        "middleName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": gen_email(),
        "phone": fake.phone_number(),
        "domainID": "test_domain",
        "disable": ["mail", "calendar", "teambox"],
    }

    with allure.step(f"Создаем аккаунт {user_info['email']}"):
        try:
            stentor.biz_createUser(
                **user_info,
            )
        except Exception as error:
            logger.error(error)

    yield user_info
    with allure.step(f"Удаляем аккаунт {user_info['email']}"):
        try:
            stentor.biz_deleteUser(
                email=user_info["email"],
            )
        except Exception as error:
            logger.error(error)


def pytest_sessionfinish(session, exitstatus):
    if not os.getenv("JENKINS_HOME"):
        session.exitstatus = 0
    else:
        session.exitstatus = exitstatus


@pytest.fixture(scope="session")
def LIBVOIP_VERSION(pytestconfig: Config):
    return pytestconfig.getoption("--libvoip-version", default=None)


@pytest.fixture(scope="session")
def SUPPLY_URL(pytestconfig: Config):
    return pytestconfig.getoption("--supply-url")


@pytest.fixture(scope="session")
def USE_SSO(pytestconfig: Config, ENV_PLATFORM):
    if ENV_PLATFORM in ["SANDBOX", "SAAS"]:
        return pytestconfig.getoption("--use-sso", default=False)

    return False


@pytest.fixture(scope="session")
def DOMAIN_PAID(pytestconfig: Config, ENV_PLATFORM):
    if ENV_PLATFORM in ["SAAS", "SANDBOX"]:
        return pytestconfig.getoption("--domain-paid", default=None)


@pytest.fixture(scope="session")
def USE_SWA(pytestconfig: Config, ENV_PLATFORM):
    if ENV_PLATFORM in ["PRE_TARM", "TARM"]:
        return pytestconfig.getoption("--use-swa", default=False)

    return False


def pytest_sessionstart(session):
    if os.getenv("PUPPET_TESTS"):
        sandbox_url = session.config.getoption("--sandbox")
        sandbox_url = (
            get_config(sandbox_url).get("api-urls").get("main-api").replace("https://u-", "").replace("https://u.", "")
        )

        url = "http://imqa-supply.mail.msk/api/"

        fn = pathlib.Path().joinpath(".hook_url")
        with FileLock(str(fn) + ".lock"):
            if not fn.is_file():
                fn.write_text(json.dumps(sandbox_url))

                response = requests.get(
                    url=url + "accounts/init_onp",
                    params={"domain": sandbox_url},
                    verify=False,
                )

                response_json = response.json()
                task_id = response_json["task_id"]
                response.raise_for_status()

                while True:
                    response = requests.get(
                        url=url + f"celery/task/{task_id}",
                        verify=False,
                    )

                    response.raise_for_status()
                    response_json = response.json()

                    if "status" in response_json and response_json["status"] == "SUCCESS":
                        break

                    time.sleep(10)


@pytest.fixture(scope="session")
def worker_index(worker_id):
    return 0 if worker_id == "master" else int(worker_id.replace("gw", ""))
