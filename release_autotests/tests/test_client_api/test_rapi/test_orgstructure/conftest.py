import time
from datetime import datetime
from typing import Literal

import allure
import pytest


@pytest.fixture(scope="session", autouse=True)
def is_orgstructure_enabled(
    ENV_PLATFORM,
    get_myteam_config,
) -> None:
    with allure.step("Проверяем что оргструктура включена"):
        if (
            "orgstructure"
            not in get_myteam_config.get("services", {}).get("disposition", {}).get("desktop", {})["leftbar"]
        ):
            pytest.skip(f"{ENV_PLATFORM}:Organization structure is disabled in config")


@pytest.fixture(scope="session", params=["organization", "department"])
def default_org_type(
    request,
) -> Literal["organization", "department"]:
    return request.param


@pytest.fixture(scope="session")
def default_org(
    auth_account,
    default_org_type,
) -> dict:
    org_name = f"Test unit {datetime.now()}"

    with allure.step("Пробуем создать оргструктуру"):
        response = auth_account.rapi_orgstructure_admin_create(
            name=org_name,
        )

        for i in range(5):
            time.sleep(i)

            with allure.step("Проверяем, что оргструктура создана"):
                org_list = auth_account.rapi_orgstructure_list()["results"][-1]["orgstructureId"]

                if org_list == response["results"]["orgstructureId"]:
                    break

        yield response
    with allure.step("Удаляем оргструктуру"):
        auth_account.rapi_orgstructure_admin_delete(
            orgstructureId=response["results"]["orgstructureId"],
        )


@pytest.fixture(scope="session")
def default_org_id(
    default_org,
    default_org_type,
) -> str:
    return default_org["results"]["orgstructureId"]


@pytest.fixture(scope="session")
def default_unit(
    auth_account,
    default_org_id,
    default_org_type,
    photo_id,
    SANDBOX,
) -> dict:
    with allure.step("Пробуем отправить запрос"):
        response = auth_account.rapi_orgstructure_admin_unit_create(
            name=f"Test unit {datetime.now()}",
            parentId="",
            _type="organization",
            orgstructureId=default_org_id,
            description="Test description",
            lead=auth_account.uin,
            logo=photo_id,
            domains=[
                "autotest.clients",
                "corp.mail.ru",
                "vk.team",
                SANDBOX,
            ],
        )
        unit_id = response["results"]["unitId"]

        for t in range(5):
            result = auth_account.rapi_orgstructure_unit_list(
                orgstructureId=default_org_id, view=default_org_type, unit_id=unit_id
            )
            if not result["results"]:
                time.sleep(t)
            else:
                break
    return response


@pytest.fixture(scope="session")
def default_unit_id(
    default_unit,
) -> str:
    return default_unit["results"]["unitId"]


@pytest.fixture(scope="session")
def default_subunit(
    default_unit_id,
    default_org_id,
    auth_account,
    photo_id,
    SANDBOX,
) -> dict:
    with allure.step("Пробуем отправить запрос"):
        response = auth_account.rapi_orgstructure_admin_unit_create(
            name=f"Test unit {datetime.now()}",
            parentId=default_unit_id,
            _type="department",
            orgstructureId=default_org_id,
            lead=auth_account.uin,
            logo=photo_id,
            domains=[
                "autotest.clients",
                "corp.mail.ru",
                "vk.team",
                SANDBOX,
            ],
        )
    return response


@pytest.fixture(scope="session")
def default_subunit_id(
    default_subunit,
) -> str:
    return default_subunit["results"]["unitId"]


@pytest.fixture
def default_post(
    default_subunit_id,
    auth_account,
) -> dict:
    with allure.step("Пробуем отправить запрос"):
        response = auth_account.rapi_orgstructure_admin_post_create(
            name=f"Test unit {datetime.now()}",
            unitId=default_subunit_id,
        )
    return response


@pytest.fixture
def default_post_id(
    default_post,
) -> str:
    return default_post["results"]["postId"]
