import logging
import os
import pathlib
import re
from typing import Optional
from imcommonsupplyclient.session import Session as SupplySession

import allure
import pytest
import requests

from _pytest.config import Config
from _pytest.nodes import Item

log = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def get_config():
    def _get_config(link: str) -> dict:
        urls = [
            f"https://{link}/myteam-config.json",
            f"http://{link}/myteam-config.json",
        ]

        last_exc: Exception | None = None

        for url in urls:
            try:
                resp = requests.get(url, timeout=10, verify=False)
                resp.raise_for_status()
                return resp.json()
            except Exception as e:
                last_exc = e

        # если обе попытки неудачны — пробрасываем последнюю ошибку
        raise RuntimeError(f"Не удалось получить конфиг с {link}") from last_exc

    return _get_config

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

@allure.title("Получение параметра --sandbox")
@pytest.fixture(scope="session")
def SANDBOX(pytestconfig: Config) -> str:
    return pytestconfig.getoption("--sandbox")

@pytest.fixture(scope="session")
def SUPPLY_URL(pytestconfig: Config):
    return pytestconfig.getoption("--supply-url")

@pytest.fixture(scope="session")
def USE_SSO(pytestconfig: Config):
    return pytestconfig.getoption("--use-sso", default=False)

@pytest.fixture(scope="session")
def USE_SWA(pytestconfig: Config):
    return pytestconfig.getoption("--use-swa", default=False)

@allure.title("Получение сессии supply-сервера")
@pytest.fixture(scope="session")
def supply_session(SANDBOX, SUPPLY_URL, USE_SSO):
    domain = SANDBOX.replace("https://", "u.vkt-", 1)
    with SupplySession(
        environment="SANDBOX",
        domain=domain,
        test_platform="IMSERVER",
        max_accounts_count=50,
        supply_url=SUPPLY_URL,
    ) as sup_session:
        yield sup_session

@allure.title("Получение аккаунта otp")
@pytest.fixture(scope="session")
def account_otp(
    USE_SSO,
    USE_SWA,
    supply_session,
):
    account = supply_session.acquire_account(as_dict=True, sso=USE_SSO, user_domain="otp.auth-test.vkteams.vkwm.ru", is_admin=False)
    return account

@allure.title("Получение аккаунта swa")
@pytest.fixture(scope="session")
def account_swa(
    USE_SSO,
    USE_SWA,
    supply_session,
):
    account = supply_session.acquire_account(as_dict=True, swa=USE_SWA, user_domain="swadup.auth-test.vkteams.vkwm.ru", is_admin=False)
    return account

@allure.title("Добавляем информацию о тестовой среде")
def pytest_collection_modifyitems(config: Config, items: list[Item]) -> None:
    global HERE_SLOW
    try:
        env_option = config.getoption("-m")

        if "TEAMS" in env_option:
            env = "TEAMS"

        elif "WS" in env_option:
            env = "WS"

        elif "BIZ" in env_option:
            env = "BIZ"

        else:
            raise ValueError(f"Unknown env value: {env_option}")
    except Exception as error:
        log.error(error)

    for item in items:  # Проходимся по списку кейсов
        log.info(item.name)
        allure_id = get_allure_id(item)

        if (
            allure_id is not None
            and {"allure_id": allure_id, "name": item.nodeid.replace("/", ".").replace("::", "#")}
        ):
            log.info(f"Skipping test with allure ID {allure_id}")
            # item.add_marker(  # Проставляем skip на тесты, присутствующие в списке
            #     pytest.mark.skip("Skipped by TestQuarantin API service")
            # )

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
        default="",
        help="Базовый URL тестируемого песка",
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
