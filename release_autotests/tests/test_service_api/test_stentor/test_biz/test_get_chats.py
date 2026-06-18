import json

import allure
import pytest

import time

from support.markers import SANDBOX


@allure.id("513333")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Biz")
@allure.title("Проверка получения списка чатов /api/v1/biz/chats")
@SANDBOX
def test_get_chats(auth_account, stentor, stentor_groups_info):
    with allure.step("Получаем текущий список групп"):
        stentor.biz_getChats()

    with allure.step(f"Создаем группу {stentor_groups_info['name']}"):
        response = auth_account.create_chat(**stentor_groups_info)
        chat_id = response.split("@")[0]

    time.sleep(3)

    with allure.step("Получаем текущий список групп"):
        response = stentor.biz_getChats(id_in=json.dumps([chat_id]))

    with allure.step(f"Проверяем наличие созданной группы {stentor_groups_info['name']} в списке"):
        for chat in response["results"]["chats"]:
            group_name = chat["name"]
            creator_email = chat["creator_sn"]
            public = chat["public"]
            chat_type = chat["type"]
            member_cnt = chat["members_count"]
            if (
                creator_email == auth_account.uin
                and group_name == stentor_groups_info["name"]
                and public == stentor_groups_info["public"]
                and chat_type == "group"
                and member_cnt == len(stentor_groups_info["members"]) + 1
            ):
                break
        else:
            pytest.fail(f"Created chat {stentor_groups_info['name']} not found")
