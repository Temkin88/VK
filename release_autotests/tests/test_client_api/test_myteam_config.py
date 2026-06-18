import json
import pathlib
import typing

import allure
import pytest
import requests
from jsondiff import diff

from pyvkteamsclient.client.schemas.myteam_config import saas, sandbox, tarm, vkti
from support.markers import VKTI, SAAS, TARM, SLA, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.SETTINGS)]


def choose_config_schema(
    ENV_PLATFORM: str,
) -> typing.Union[
    typing.Type[saas.SaaSConfig],
    typing.Type[sandbox.SandboxConfig],
    typing.Type[vkti.VktiConfig],
    typing.Type[tarm.TarmConfig],
]:
    if ENV_PLATFORM == "SAAS":
        return saas.SaaSConfig
    elif ENV_PLATFORM == "SANDBOX":
        return sandbox.SandboxConfig
    elif ENV_PLATFORM in ["VKTI", "PRE_VKTI"]:
        return vkti.VktiConfig
    elif ENV_PLATFORM in ["TARM", "PRE_TARM"]:
        return tarm.TarmConfig
    else:
        raise ValueError(f"Unknown platform: {ENV_PLATFORM}")


@allure.id("48749")
@SAAS
@PRE_SAAS
@SLA
@allure.suite("myteam-config.json")
@allure.feature("Получение myteam-config.json")
@allure.title("Проверка схемы myteam-config.json")
def test_myteam_config_json_saas(session, main_api, ENV_PLATFORM):
    with allure.step("Запрашиваем myteam-config.json"):
        myteam_config = session.get(
            url=f"{main_api}/myteam-config.json",
            params={
                "domain": "test-testbiz-vkteams-qa.bizml.ru",
            },
        ).json()

    with allure.step("Считываем эталонный конфиг"):
        saas_config = json.loads(
            pathlib.Path("myteam-config-json/saas/myteam-config.json").read_text(),
        )

    for config in (saas_config, myteam_config):
        for key in (
            "mini-apps",
            "services",
            "task-creation-in-chat-enabled",
            "tasks-enabled",
            "threads-enabled",
        ):
            if key in config:
                del config[key]

    with allure.step("Сравниваем эталонный конфиг с полученным"):
        result = diff(saas_config, myteam_config)
        assert not result, "не правильные отличия в конфиге и эталоне"


@allure.id("48757")
@TARM
@SLA
@allure.suite("myteam-config.json")
@allure.feature("Получение myteam-config.json")
@allure.title("Проверка схемы myteam-config.json")
def test_myteam_config_json_tarm(session, main_api, ENV_PLATFORM):
    with allure.step("Запрашиваем myteam-config.json"):
        myteam_config = session.get(
            url=f"{main_api}/myteam-config.json",
        ).json()

    with allure.step("Считываем эталонный конфиг"):
        tarm_config = json.loads(
            pathlib.Path("myteam-config-json/tarm/myteam-config.json").read_text(),
        )

    for config in (tarm_config, myteam_config):
        for key in (
            "custom-miniapps",
            "services",
            "apps",
        ):
            if key in config:
                del config[key]

    with allure.step("Сравниваем эталонный конфиг с полученным"):
        result = diff(tarm_config, myteam_config)
        assert not result, "не правильные отличия в конфиге и эталоне"


@allure.id("48756")
@VKTI
@SLA
@allure.suite("myteam-config.json")
@allure.feature("Получение myteam-config.json")
@allure.title("Проверка схемы myteam-config.json")
def test_myteam_config_json_vkti(session, main_api, ENV_PLATFORM):
    with allure.step("Запрашиваем myteam-config.json"):
        myteam_config = session.get(
            url=f"{main_api}/myteam-config.json",
        ).json()

    with allure.step("Считываем эталонный конфиг"):
        tarm_config = json.loads(
            pathlib.Path("myteam-config-json/vk/myteam-config.json").read_text(),
        )

    for config in (tarm_config, myteam_config):
        for key in (
            "custom-miniapps",
            "services",
            "apps",
        ):
            if key in config:
                del config[key]

    with allure.step("Сравниваем эталонный конфиг с полученным"):
        result = diff(tarm_config, myteam_config)
        assert not result, "не правильные отличия в конфиге и эталоне"


@allure.id("38434")
@SAAS
@PRE_SAAS
@SLA
@allure.suite("myteam-config.json")
@allure.feature("Получение myteam-config.json")
@allure.title("Ошибка получение myteam-config.json если не указан домен")
def test_myteam_config_json_fail(session):
    with allure.step("Запрашиваем myteam-config.json"), pytest.raises(requests.HTTPError):
        response = session.get(
            url="https://u.myteam.vmailru.net/myteam-config.json",
        )
        response.raise_for_status()
