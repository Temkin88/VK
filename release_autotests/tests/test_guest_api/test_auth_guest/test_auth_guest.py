from datetime import datetime, timedelta

import allure
import pytest

from pyvkteamsclient.client import CallGuestClient
from pyvkteamsclient.client.exceptions import RequestException, AccessDeniedException, BadRequestException

from support.markers import SAAS, VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CALLS)]


@allure.id("79713")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.suite("Гостевые звонки")
@allure.feature("Авторизация гостевого пользователя")
@allure.title("Авторизация гостевого пользователя")
def test_guest_auth_success(
    conference_url,
    session,
    main_api,
    binary_api,
    api_version,
    fetch_until_empty_answer,
):
    with allure.step("Пытаемся авторизовать гостя"):
        guest = CallGuestClient(
            name="Test guest 1",
            scopes=[
                conference_url.split("/")[-1],
            ],
            session=session,
            api_url=main_api,
            binary_api_url=binary_api,
            api_ver=api_version,
        )

    with allure.step("Получаем первые события"):
        fetch_until_empty_answer(guest)


@allure.id("30913")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.suite("Гостевые звонки")
@allure.feature("Авторизация гостевого пользователя")
@allure.title("Авторизация гостевого пользователя (fail - tasks)")
def test_guest_auth_fail_task(
    auth_account,
    conference_url,
    session,
    main_api,
    binary_api,
    api_version,
    fetch_until_empty_answer,
):
    with allure.step("Пытаемся авторизовать гостя"):
        guest = CallGuestClient(
            name="Test guest 1",
            scopes=[
                conference_url.split("/")[-1],
            ],
            session=session,
            api_url=main_api,
            binary_api_url=binary_api,
            api_ver=api_version,
        )

    with pytest.raises((RequestException, BadRequestException, AccessDeniedException)):
        guest.tasks_add(
            title="Task title",
            endTime=int((datetime.now() + timedelta(days=5)).timestamp()),
            assignee=auth_account.uin,
            label="none",
            priority="low",
            tags=("CVE",),
        )


@allure.id("30912")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.suite("Гостевые звонки")
@allure.feature("Авторизация гостевого пользователя")
@allure.title("Авторизация гостевого пользователя (fail - files)")
def test_guest_auth_fail_files(
    auth_account,
    conference_url,
    session,
    main_api,
    binary_api,
    api_version,
    fetch_until_empty_answer,
):
    with allure.step("Пытаемся авторизовать гостя"):
        guest = CallGuestClient(
            name="Test guest 1",
            scopes=[
                conference_url.split("/")[-1],
            ],
            session=session,
            api_url=main_api,
            binary_api_url=binary_api,
            api_ver=api_version,
        )

    with pytest.raises((RequestException, BadRequestException)):
        guest.upload_file("support/files/speechtotext/file_for_speechtotext.m4a")


@allure.id("30914")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.suite("Гостевые звонки")
@allure.feature("Авторизация гостевого пользователя")
@allure.title("Авторизация гостевого пользователя (fail - stickers)")
def test_guest_auth_fail_stickers(
    auth_account,
    conference_url,
    session,
    main_api,
    binary_api,
    api_version,
    fetch_until_empty_answer,
):
    with allure.step("Пытаемся авторизовать гостя"):
        guest = CallGuestClient(
            name="Test guest 1",
            scopes=[
                conference_url.split("/")[-1],
            ],
            session=session,
            api_url=main_api,
            binary_api_url=binary_api,
            api_ver=api_version,
        )

    response = auth_account.store_showcase()

    with pytest.raises(AccessDeniedException):
        guest.store_showcase()

    with pytest.raises(AccessDeniedException):
        guest.openstore_filespackinfowithmeta(response["result"]["showcase"][0]["id"])
