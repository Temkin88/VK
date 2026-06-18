import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("37473")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Получение списка админов в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_get_chat_admins(
    bot_class,
    prepare_bot_test_chats,
    chat_type,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Пробуем закрепить сообщение в чате"):
        response = bot_class.get_chat_admins(
            chat_id=chat,
        )

    with allure.step("Проверяем ответ"):
        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")

        members_map = [x["userId"] for x in response_info["admins"]]

        for member_uin in (bot_class.uin, user.uin):
            assert member_uin in members_map, f"{member_uin} not in members list: {members_map}"
