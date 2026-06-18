import time
import uuid

import allure
import pytest

from support.markers import SAAS, SANDBOX, VKTI, PRE_VKTI, TARM, PRE_TARM, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CONTACTS)]


@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.id("218308")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Контакты")
@allure.feature("Изменение контакта")
@allure.title("Устанавливаем атрибут для приятеля")
@pytest.mark.parametrize("chat_type", ["group", "channel", "private"])
def test_buddylist_set_buddy_attribute(
    fetch_until_empty_answer,
    event_filter,
    chat_type,
    prepare_test_chats,
    second_auth_account,
):
    event_filter.start_point()

    auth_account, opponent_account, group, channel = prepare_test_chats

    fetch_until_empty_answer(auth_account)
    fetch_until_empty_answer(second_auth_account)

    if chat_type == "private":
        chat = opponent_account.uin
    elif chat_type == "favorite":
        chat = auth_account.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step(f"Пишем сообщение в чат {auth_account.uin}"):
        auth_account.send_basic_message(
            sn=auth_account.uin,
            text="Test",
        )

    with allure.step("Пробуем установить атрибут для приятеля"):
        response = auth_account.wim_buddyList_setBuddyAttribute(
            buddy=chat,
            friendly=auth_account.uin,
        )
        assert response["response"]["statusCode"] == 200, "Status code not 200"
        assert response["response"]["statusText"] == "Ok", "Status text not 'OK'"

    with allure.step("Проверяем что поле friendly изменилось"):
        response = auth_account.rapi_getHistory(sn=auth_account.uin)
        result = response["results"]
        for friendly in filter(lambda x: x["sn"] == chat, result["persons"]):
            assert friendly == auth_account.uin, f"{auth_account.uin} no in friendly field"

    with allure.step(f"Проверям, что установился атрибут для приятеля под инстансом {second_auth_account}"):
        time.sleep(30)
        RETRIES = 5

        friendly_second = False
        for _ in range(RETRIES):
            fetch_until_empty_answer(second_auth_account)
            for event in event_filter(second_auth_account.events, "diff"):
                for data in event["eventData"]:
                    for entry in data["data"]:
                        for buddy in filter(
                            lambda y: chat == y["aimId"],
                            entry["buddies"],
                        ):
                            if buddy["friendly"] == second_auth_account.uin:
                                friendly_second = True
                                break
                        if friendly_second:
                            break
                    if friendly_second:
                        break
                if friendly_second:
                    break
            if friendly_second:
                break
            else:
                time.sleep(1)

        assert friendly_second, f"{second_auth_account.uin} no in friendly field"


@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.id("218310")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Контакты")
@allure.feature("Изменение контакта")
@allure.title("Добавление приятеля в список друзей")
@pytest.mark.parametrize("chat_type", ["group", "favorite", "channel", "private"])
def test_buddylist_add_buddy(
    fetch_until_empty_answer,
    event_filter,
    chat_type,
    prepare_test_chats,
    second_auth_account,
):
    event_filter.start_point()

    auth_account, opponent_account, group, channel = prepare_test_chats
    auth_account.fetch(timeout=300)

    if chat_type == "private":
        chat = opponent_account.uin
    elif chat_type == "favorite":
        chat = auth_account.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Пробуем добавить приятеля в список друзей."):
        response = auth_account.wim_buddyList_addBuddy(
            buddy=chat,
            group=f"Test name group {uuid.uuid4().hex}",
            nick=f"Test nick {uuid.uuid4().hex}",
        )
        results = response["response"]["data"]["results"]
        assert response["response"]["statusCode"] == 200, "Status code not 200"
        assert response["response"]["statusText"] == "Ok", 'Status text not "OK"'
        assert chat == results[0]["buddy"], f"{chat} not matches"

    with allure.step(f"Проверям, что пришло события добавления приятеля под инстансом {second_auth_account}"):
        time.sleep(30)
        RETRIES = 5
        added_event_second = False
        for i in range(RETRIES):
            fetch_until_empty_answer(second_auth_account)
            for event in event_filter(second_auth_account.events, "diff"):
                for data in event["eventData"]:
                    for entry in data["data"]:
                        if "added" in entry:
                            added_event_second = True
                            break
                    if added_event_second:
                        break
                if added_event_second:
                    break
            if added_event_second:
                break
            else:
                time.sleep(i)

        assert added_event_second, "Added fiend not found"


@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.id("218309")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Контакты")
@allure.feature("Изменение контакта")
@allure.title("Скрытие чата")
@pytest.mark.parametrize("chat_type", ["group", "favorite", "channel"])
def test_buddylist_hideChat(
    fetch_until_empty_answer,
    event_filter,
    chat_type,
    prepare_test_chats,
    second_auth_account,
):
    event_filter.start_point()

    auth_account, opponent_account, group, channel = prepare_test_chats
    auth_account.fetch(timeout=300)

    if chat_type == "private":
        chat = opponent_account.uin
    elif chat_type == "favorite":
        chat = auth_account.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Пробуем скрыть чат"):
        response = auth_account.wim_buddyList_hideChat(buddy=chat)
        assert response["response"]["statusCode"] == 200, "Status code not 200"
        assert response["response"]["statusText"] == "Ok", 'Status text not "OK"'


@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.id("218331")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Контакты")
@allure.feature("Изменение контакта")
@allure.title("Удаление контакта/чата")
@pytest.mark.parametrize("chat_type", ["group", "favorite", "channel", "private"])
def test_buddylist_removeBuddy(
    fetch_until_empty_answer,
    event_filter,
    chat_type,
    prepare_test_chats,
    second_auth_account,
):
    event_filter.start_point()

    auth_account, opponent_account, group, channel = prepare_test_chats

    auth_account.fetch(timeout=300)

    # In boss (sapi backend service) we have flow:
    # 1) updateUser
    # 2) [only for groups and channels] updateUserFromMchat
    # 3) updateUserFromMchat
    # 4) [only if BOSS_HIST_DELIVER_SELF_LEAVE true] cleanBuddyMchatSelfLeave
    # 5) generate hiddenEvent
    # Therefore, only for mchat entities (like channels and groups) ending with @chat.agent we will receive hiddenEvent.
    is_hidden_event_required: bool = chat_type in ["group", "channel"]

    if chat_type == "private":
        chat = opponent_account.uin
    elif chat_type == "favorite":
        chat = auth_account.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Пробуем добавить приятеля в список друзей."):
        auth_account.wim_buddyList_addBuddy(
            buddy=chat,
            group="Test name group",
            nick="Test nick",
        )

    fetch_until_empty_answer(second_auth_account)  # we need to get initial buddylist to see diff later

    with allure.step("Пробуем удалить чат"):
        response = auth_account.wim_buddyList_removeBuddy(buddy=chat)
        assert response["response"]["statusCode"] == 200, "Status code not 200"
        assert response["response"]["statusText"] == "Ok", 'Status text not "OK"'

    with allure.step(f"Проверям, что пришли события под инстансом {second_auth_account}"):
        time.sleep(30)
        RETRIES = 5
        deleted_event_second = False
        hidden_chat_event_second = False

        for i in range(RETRIES):
            fetch_until_empty_answer(second_auth_account)
            for event in event_filter(second_auth_account.events[::-1], "hiddenChat", "diff"):
                if event["type"] == "diff":
                    for data in event["eventData"]:
                        if data["type"] == "deleted":
                            deleted_event_second = True
                            break
                    if deleted_event_second:
                        break
                else:
                    hidden_chat_event_second = True

                if deleted_event_second and not is_hidden_event_required:
                    break
                if deleted_event_second and hidden_chat_event_second:
                    break

            if deleted_event_second and not is_hidden_event_required:
                break
            if deleted_event_second and hidden_chat_event_second:
                break
            else:
                time.sleep(i)

        assert deleted_event_second, "Deleted event type not found"
        if is_hidden_event_required:
            assert hidden_chat_event_second, "HiddenChat event type not found"
