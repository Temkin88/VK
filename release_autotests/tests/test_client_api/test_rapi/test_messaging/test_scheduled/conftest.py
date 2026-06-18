import pathlib
import uuid
import time
import logging
from typing import Optional

import pytest
import allure

from datetime import datetime

import requests

from pyvkteamsclient.client import DesktopClient

logger = logging.getLogger(__name__)


@allure.title("Проверка включенности запланированной отправки сообщений")
@pytest.fixture(scope="session", autouse=True)
def is_scheduled_message_sending_enabled(
    myteam_config,
):
    if "scheduled-messages" in myteam_config and myteam_config["scheduled-messages"]["enabled"]:
        return True

    else:
        pytest.skip("Scheduled message sending is disabled")


@allure.title("Подготовка к тестам запланированных сообщений")
@pytest.fixture(
    params=[
        ("favorite", "basic"),
        ("private", "basic"),
        ("group", "basic"),
        ("channel", "basic"),
        ("favorite", "formatted"),
        ("private", "formatted"),
        ("group", "formatted"),
        ("channel", "formatted"),
        ("favorite", "file"),
        ("private", "file"),
        ("group", "file"),
        ("channel", "file"),
        ("favorite", "poll"),
        ("private", "poll"),
        ("group", "poll"),
        ("channel", "poll"),
    ],
    ids=lambda x: f"{x[0]}-{x[1]}",
)
def schedule_message_sending(
    request,
    prepare_test_chats,
    auth_account,
):
    auth_account, opponent_account, group, channel = prepare_test_chats

    chat_type, msg_type = request.param

    if chat_type == "favorite":
        chat = auth_account.uin
    elif chat_type == "private":
        chat = opponent_account.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    try:
        auth_account.rapi_message_scheduled_cancel(
            sn=chat,
        )
    except Exception as error:
        logger.warning(error)

    if msg_type == "basic":

        @allure.step("Запланируем отправку обычного сообщения")
        def schedule_message(
            scheduled_time: int,
            update_scheduled_msg_id: Optional[int] = None,
            sleep: bool = False,
        ):
            nonlocal chat

            schedule = {
                "scheduledTime": scheduled_time,
            }

            if update_scheduled_msg_id is not None:
                schedule["updateScheduledMsgId"] = update_scheduled_msg_id

            response = auth_account.wim_im_sendIM(
                t=chat,
                message=f"Test message for scheduled sending - {auth_account.getReqId()}",
                schedule=schedule,
            )

            if sleep:
                time.sleep(
                    scheduled_time - datetime.now().timestamp(),
                )

            return response["response"]["data"]["scheduled"]

    elif msg_type == "formatted":

        @allure.step("Запланируем отправку форматированного сообщения")
        def schedule_message(
            scheduled_time: int,
            update_scheduled_msg_id: Optional[int] = None,
            sleep: bool = False,
        ):
            nonlocal chat

            schedule = {
                "scheduledTime": scheduled_time,
            }

            if update_scheduled_msg_id is not None:
                schedule["updateScheduledMsgId"] = update_scheduled_msg_id

            response = auth_account.wim_im_sendIM(
                t=chat,
                parts=[
                    {
                        "mediaType": "text",
                        "text": f"Test message for scheduled sending - {auth_account.getReqId()}",
                        "format": {
                            "bold": [
                                {
                                    "offset": 0,
                                    "length": 4,
                                },
                                {
                                    "offset": 5,
                                    "length": 7,
                                },
                            ],
                        },
                    }
                ],
                schedule=schedule,
            )

            if sleep:
                time.sleep(
                    scheduled_time - datetime.now().timestamp(),
                )

            return response["response"]["data"]["scheduled"]

    elif msg_type == "file":

        @allure.step("Запланируем отправку сообщения с файлом")
        def schedule_message(
            scheduled_time: int,
            update_scheduled_msg_id: Optional[int] = None,
            sleep: bool = False,
        ):
            nonlocal chat

            schedule = {
                "scheduledTime": scheduled_time,
            }

            if update_scheduled_msg_id is not None:
                schedule["updateScheduledMsgId"] = update_scheduled_msg_id

            _, file_url = auth_account.upload_file(
                file_path=pathlib.Path("support").joinpath("files").joinpath("common").joinpath("crashdump.zip"),
            )

            response = auth_account.wim_im_sendIM(
                t=chat,
                message=file_url,
                schedule=schedule,
            )

            if sleep:
                time.sleep(
                    scheduled_time - datetime.now().timestamp(),
                )

            return response["response"]["data"]["scheduled"]

    elif msg_type == "poll":

        @allure.step("Запланируем отправку сообщения с опросом")
        def schedule_message(
            scheduled_time: int,
            update_scheduled_msg_id: Optional[int] = None,
            sleep: bool = False,
        ):
            nonlocal chat

            schedule = {
                "scheduledTime": scheduled_time,
            }

            if update_scheduled_msg_id is not None:
                schedule["updateScheduledMsgId"] = update_scheduled_msg_id

            response = auth_account.wim_im_sendIM(
                t=chat,
                parts=[
                    {
                        "mediaType": "text",
                        "text": f"Test poll for scheduled msg sending - {auth_account.getReqId()}",
                        "poll": {
                            "type": "anon",
                            "responses": [
                                "test_1",
                                "test_2",
                            ],
                        },
                    },
                ],
                schedule=schedule,
            )

            if sleep:
                time.sleep(
                    scheduled_time - datetime.now().timestamp(),
                )

            return response["response"]["data"]["scheduled"]

    else:
        raise ValueError(f"Unknown msg_type value: {msg_type}")

    return chat_type, msg_type, chat, schedule_message


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


@allure.title("Подготовка к тестам запланированных сообщений от заблокированного пользователя")
@pytest.fixture
def one_time_user(
    pytestconfig,
    ENV_PLATFORM,
    SANDBOX,
    sandbox_account_fix_otp,
    alter_sandbox,
    stentor,
):
    user = {
        "firstName": "Created",
        "middleName": "Random",
        "lastName": "User",
        "email": f"{uuid.uuid4().hex[8:]}@{'autotest.clients' if not alter_sandbox else SANDBOX}",
    }

    stentor.biz_createUser(**user)

    sandbox_config = get_config(SANDBOX)

    user_client = DesktopClient(
        uin=user["email"],
        api_url=sandbox_config["api-urls"]["main-api"],
        binary_api_url=sandbox_config["api-urls"]["main-binary-api"],
        api_ver=pytestconfig.getoption("--api") or sandbox_config.get("api-version", 108),
        fix_otp=sandbox_account_fix_otp if not alter_sandbox else None,
        env=ENV_PLATFORM,
        org_struct_admin_token="tr-gajEkwov-akesadmin",
    )

    yield user_client

    try:
        user_client.wim_aim_endSession()
        stentor.biz_deleteUser(user["email"])
    except Exception as error:
        logger.warning(error)
    finally:
        logger.info("User {email} was blocked".format(**user))


@pytest.fixture
def readonly_group(
    auth_account,
    one_time_user,
):
    chat_id = auth_account.create_chat(
        members=[one_time_user],
        check_members=False,
    )

    auth_account.rapi_modChatMember(
        sn=chat_id,
        memberSn=one_time_user.uin,
        role="readonly",
    )

    return chat_id


@pytest.fixture
def readonly_channel(
    auth_account,
    one_time_user,
):
    chat_id = auth_account.create_chat(
        members=[one_time_user],
        defaultRole="readonly",
        check_members=False,
    )

    return chat_id


@pytest.fixture
def for_readonly_group(
    auth_account,
    one_time_user,
):
    chat_id = auth_account.create_chat(
        members=[one_time_user],
    )

    return chat_id


@pytest.fixture
def for_readonly_channel(
    auth_account,
    one_time_user,
):
    chat_id = auth_account.create_chat(
        members=[one_time_user],
        defaultRole="readonly",
    )

    return chat_id
