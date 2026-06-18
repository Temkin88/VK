import json
import os
import time
from typing import Any

import allure
import pytest
import requests
import logging

from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

from pyvkteamsclient.client import DesktopClient
from imcommonsupplyclient import VoIPBot, Account, Session, voip

logger = logging.getLogger(__name__)


def get_config(link: str) -> dict:
    response = None

    try:
        response = requests.get(
            f"https://{link}/myteam-config.json",
            timeout=10,
            verify=False,
        )
    except Exception as error:
        logger.error(error)
        response = requests.get(
            f"http://{link}/myteam-config.json",
            timeout=10,
            verify=False,
        )
    if response is not None:
        response.raise_for_status()
        return response.json()

    else:
        raise ValueError


@pytest.fixture(scope="session")
def voip_config(myteam_config):
    voip_config = myteam_config.get(
        "voip-config",
        {
            "voip-api-version": 2,
            "callstat.impl": "callmon",
            "monitoring.recording_level_treshold": 2000,
        },
    )
    if isinstance(voip_config, str):
        voip_config = json.loads(voip_config.replace("\\", ""))

    if "voip-api-version" not in voip_config:
        voip_config["voip-api-version"] = myteam_config.get("voip-api-version", 2)

    return voip_config


@allure.title("Получение сессии supply-сервера")
@pytest.fixture(scope="session")
def voip_supply_session(
    ENV_PLATFORM,
    SANDBOX,
    api_version,
    SUPPLY_URL,
):
    if os.getenv("PUPPET_TESTS"):
        domain = get_config(SANDBOX).get("api-urls").get("main-api").replace("https://u-", "")
    else:
        domain = SANDBOX

    with Session(
        environment=ENV_PLATFORM,
        domain=domain,
        api_version=api_version,
        test_platform="IMSERVER",
        max_accounts_count=320,
        supply_url=SUPPLY_URL,
    ) as sup_session:
        yield sup_session


@pytest.fixture(scope="session")
def max_workers_count(worker_id):
    if worker_id == "master":
        return voip.VOIP_WORKERS_COUNT
    else:
        return 2


@allure.title("Получение VoIP ботов")
@pytest.fixture(scope="session")
def get_voip_bots(voip_supply_session, ENV_PLATFORM, SANDBOX, LIBVOIP_VERSION, voip_config, max_workers_count):
    if voip_supply_session is None:
        pytest.skip(f"Tests currently not working for env: {ENV_PLATFORM}")

    accounts: list[Account] = []
    bots_to_return: list[VoIPBot] = []

    @allure.step("Получение VoIP-бота")
    def get_bot(**kwargs):
        nonlocal accounts

        account = voip_supply_session.acquire_account()

        if "voip-config" not in kwargs:
            kwargs["voip_config"] = voip_config
        if "libvoip_version" not in kwargs:
            kwargs["libvoip_version"] = LIBVOIP_VERSION

        bot = account.get_voip_bot(**kwargs)

        accounts.append(account)
        bots_to_return.append(bot)

        return bot

    @allure.step("Получение {count} VoIP-ботов")
    def _get_voip_bots(count: int = 1, **kwargs) -> list[VoIPBot] | VoIPBot:
        if count == 1:
            if bots_to_return:
                return bots_to_return[0]
            else:
                return get_bot(**kwargs)
        elif count <= len(bots_to_return):
            return bots_to_return[:count]

        def get_bots(count: int):
            get_bot(**kwargs)

        with ThreadPoolExecutor(max_workers=max_workers_count) as executer:
            tasks = [executer.submit(get_bots, c) for c in range(count)]
            for future in futures.as_completed(tasks):
                try:
                    future.result()
                except ValueError as error:
                    pytest.skip(str(error))

        return bots_to_return[:count]

    yield _get_voip_bots

    with ThreadPoolExecutor(max_workers=max_workers_count) as executer:

        def release_voip_bot(local_voip_bot: VoIPBot):
            local_voip_bot.release()

        for _ in executer.map(release_voip_bot, bots_to_return):
            continue

    with ThreadPoolExecutor(max_workers=max_workers_count) as executer:

        def release_account(local_account: Account):
            local_account.release_account()

        for _ in executer.map(release_account, accounts):
            continue


@allure.title("Получение VoIP ботов")
@pytest.fixture(scope="session")
def get_voip_bots_isolation(
    voip_supply_session, ENV_PLATFORM, SANDBOX, LIBVOIP_VERSION, voip_config, max_workers_count
):
    if voip_supply_session is None:
        pytest.skip(f"Tests currently not working for env: {ENV_PLATFORM}")

    accounts: list[Account] = []
    bots_to_return: list[VoIPBot] = []

    @allure.step("Получение VoIP-бота")
    def get_bot(**kwargs):
        nonlocal accounts

        account_testbiz = voip_supply_session.acquire_account(user_domain="test-testbiz-vkteams-qa-02.bizml.ru")
        account_testb1iz = voip_supply_session.acquire_account(user_domain="testb1iz.bizml.ru")
        account_lalalalalalal = voip_supply_session.acquire_account(user_domain="lalalalalalal.bizml.ru")

        if "voip-config" not in kwargs:
            kwargs["voip_config"] = voip_config
        if "libvoip_version" not in kwargs:
            kwargs["libvoip_version"] = LIBVOIP_VERSION

        bot_testbiz = account_testbiz.get_voip_bot(**kwargs)
        bot_testb1iz = account_testb1iz.get_voip_bot(**kwargs)
        bot_lalalalalalal = account_lalalalalalal.get_voip_bot(**kwargs)

        accounts.append(account_testbiz)
        accounts.append(account_testb1iz)
        accounts.append(account_lalalalalalal)
        bots_to_return.append(bot_testbiz)
        bots_to_return.append(bot_testb1iz)
        bots_to_return.append(bot_lalalalalalal)

        return bots_to_return

    @allure.step("Получение {count} VoIP-ботов")
    def _get_voip_bots(count: int = 1, **kwargs) -> tuple[VoIPBot, VoIPBot, VoIPBot] | list[VoIPBot]:
        if count == 1:
            if bots_to_return:
                return bots_to_return[0], bots_to_return[1], bots_to_return[2]
            else:
                return get_bot(**kwargs)
        elif count <= len(bots_to_return):
            return bots_to_return[:count]

        def get_bots(count: int):
            get_bot(**kwargs)

        with ThreadPoolExecutor(max_workers=max_workers_count) as executer:
            tasks = [executer.submit(get_bots, c) for c in range(count)]
            for future in futures.as_completed(tasks):
                try:
                    future.result()
                except ValueError as error:
                    pytest.skip(str(error))

        return bots_to_return[:count]

    yield _get_voip_bots

    with ThreadPoolExecutor(max_workers=max_workers_count) as executer:

        def release_voip_bot(local_voip_bot: VoIPBot):
            local_voip_bot.release()

        for _ in executer.map(release_voip_bot, bots_to_return):
            continue

    with ThreadPoolExecutor(max_workers=max_workers_count) as executer:

        def release_account(local_account: Account):
            local_account.release_account()

        for _ in executer.map(release_account, accounts):
            continue


@allure.title("Получение гостевых VoIP ботов")
@pytest.fixture(scope="session")
def get_guest_bots(voip_supply_session, ENV_PLATFORM, SANDBOX, max_workers_count):
    if voip_supply_session is None:
        pytest.skip(f"Tests currently not working for env: {ENV_PLATFORM}")

    accounts: list[Account] = []
    bots_to_return: list[VoIPBot] = []

    @allure.step("Получение VoIP-бота")
    def get_bot(call_link: str, *args):
        nonlocal accounts

        account = voip_supply_session.acquire_account()
        bot = account.get_guest_voip_bot(call_link=call_link)

        accounts.append(account)
        bots_to_return.append(bot)

        return bot

    @allure.step("Получение {count} VoIP-ботов")
    def _get_voip_bots(call_link: str, count: int = 1) -> list[VoIPBot] | VoIPBot:
        if count == 1:
            if bots_to_return:
                return bots_to_return[0]
            else:
                return get_bot(call_link=call_link)
        elif count <= len(bots_to_return):
            return bots_to_return[:count]

        with ThreadPoolExecutor(max_workers=max_workers_count) as executer:
            for _ in executer.map(lambda x: get_bot(call_link=call_link, x=x), range(count - len(bots_to_return))):
                continue

        return bots_to_return[:count]

    yield _get_voip_bots

    with ThreadPoolExecutor(max_workers=max_workers_count) as executer:

        def release_voip_bot(local_voip_bot: VoIPBot):
            local_voip_bot.release()

        for _ in executer.map(release_voip_bot, bots_to_return):
            continue

    with ThreadPoolExecutor(max_workers=max_workers_count) as executer:

        def release_account(local_account: Account):
            local_account.release_account()

        for _ in executer.map(release_account, accounts):
            continue


@allure.title("Получение гостевых VoIP ботов")
@pytest.fixture(scope="session")
def get_guest_bots_isolation(voip_supply_session, ENV_PLATFORM, SANDBOX, max_workers_count):
    if voip_supply_session is None:
        pytest.skip(f"Tests currently not working for env: {ENV_PLATFORM}")

    accounts: list[Account] = []
    bots_to_return: list[VoIPBot] = []

    @allure.step("Получение VoIP-бота")
    def get_bot(call_link: str, *args):
        nonlocal accounts

        account_testbiz = voip_supply_session.acquire_account(user_domain="autotest-01.clients")
        account_testb1iz = voip_supply_session.acquire_account(user_domain="autotest-02.clients")
        account_lalalalalalal = voip_supply_session.acquire_account(user_domain="autotest-03.clients")

        bot_testbiz = account_testbiz.get_guest_voip_bot(call_link=call_link)
        bot_testb1iz = account_testb1iz.get_guest_voip_bot(call_link=call_link)
        bot_lalalalalalal = account_lalalalalalal.get_guest_voip_bot(call_link=call_link)

        accounts.append(account_testbiz)
        accounts.append(account_testb1iz)
        accounts.append(account_lalalalalalal)
        bots_to_return.append(bot_testbiz)
        bots_to_return.append(bot_testb1iz)
        bots_to_return.append(bot_lalalalalalal)

        return bots_to_return

    @allure.step("Получение {count} VoIP-ботов")
    def _get_voip_bots(call_link: str, count: int = 1) -> list[VoIPBot] | tuple[VoIPBot, VoIPBot, VoIPBot] | Any:
        if count == 1:
            if bots_to_return:
                return bots_to_return[0], bots_to_return[1], bots_to_return[2]
            else:
                return get_bot(call_link=call_link)
        elif count <= len(bots_to_return):
            return bots_to_return[:count]

        with ThreadPoolExecutor(max_workers=max_workers_count) as executer:
            for _ in executer.map(lambda x: get_bot(call_link=call_link, x=x), range(count - len(bots_to_return))):
                continue

        return bots_to_return[:count]

    yield _get_voip_bots

    with ThreadPoolExecutor(max_workers=max_workers_count) as executer:

        def release_voip_bot(local_voip_bot: VoIPBot):
            local_voip_bot.release()

        for _ in executer.map(release_voip_bot, bots_to_return):
            continue

    with ThreadPoolExecutor(max_workers=max_workers_count) as executer:

        def release_account(local_account: Account):
            local_account.release_account()

        for _ in executer.map(release_account, accounts):
            continue


@pytest.fixture(scope="session")
def get_bot_account():
    def _get_api_wrapper(bot: VoIPBot) -> DesktopClient:
        wrapper = DesktopClient(
            uin=bot.account().uin,
            api_url=bot.account().api_url,
            binary_api_url=bot.account().binary_api_url,
            api_ver=bot.account().api_ver,
            fix_otp=bot.account().fix_otp,
            email_url=bot.account().email_url,
            email_password=bot.account().email_password,
        )

        return wrapper

    return _get_api_wrapper


@pytest.fixture
def check_recorded_call_video_file(fetch_until_empty_answer, event_filter):
    def _check_wrapper(bot_account: DesktopClient, recorder_bot_sn: str, min_file_size_mb: float = 0.5):
        with allure.step("Ждем входящих сообщений от RecorderBot"):
            event_found = False

            for _ in range(3):
                time.sleep(20)
                with allure.step(f"Попытка #{_}"):
                    fetch_until_empty_answer(bot_account)

                    for event in event_filter(bot_account.events, "histDlgState"):
                        if event["eventData"]["sn"] == recorder_bot_sn:
                            event_found = True
                            break

                    if event_found:
                        break

            assert event_found, "histDlgState event from RecorderBot not found"

        with allure.step("Проверить доступность и корректость записи"):
            history_response = bot_account.rapi_getHistory(sn=recorder_bot_sn)

            assert history_response.get("results", {}).get("messages", None) is not None, "No messages results"
            hist_msgs = history_response["results"]["messages"]

            assert len(hist_msgs) != 0, "There are no messages"
            last_hist_msg = hist_msgs[-1]

            assert len(last_hist_msg.get("filesharing", [])) != 0, "There are no 'filesharing'"
            assert "id" in last_hist_msg["filesharing"][-1], "There are no 'filesharing' id"

            record_file_id = last_hist_msg["filesharing"][-1]["id"]

            file_info_result = bot_account.files_info(file_id=record_file_id)

            assert file_info_result.get("result", {}).get("info", None) is not None, "No file info results"

            file_info = file_info_result["result"]["info"]

            assert "file_size" in file_info, "No file size info"
            assert "dlink" in file_info, "No file dlink info"

            file_size = file_info["file_size"]
            file_url = file_info["dlink"]

            assert file_size > min_file_size_mb * 1024 * 1024, "Record file size is less than 0.5 MB"

            logger.info(f"The file can be downloaded via link {file_url} ")

    return _check_wrapper
