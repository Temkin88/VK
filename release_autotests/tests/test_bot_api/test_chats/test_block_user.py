import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("37485")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Блокировка/разблокировка пользователя в чате через BotAPI")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group"])
def test_bot_block_user(
    bot_class,
    prepare_bot_test_chats,
    chat_type,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Пробуем заблокировать пользователя в чате"):
        response = bot_class.chat_block_user(
            chat_id=chat,
            user_id=opponent.uin,
        )

        user.allure_attach(response)

        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")

    with allure.step("Получаем список заблокированных пользователей в чате"):
        response = bot_class.get_chat_blocked_users(
            chat_id=chat,
        )

        user.allure_attach(response)

        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")
        assert opponent.uin in [x["userId"] for x in response_info["users"]], f"{opponent.uin} is not blocked"

    with allure.step("Пробуем заблокировать пользователя в чате"):
        response = bot_class.chat_unblock_user(
            chat_id=chat,
            user_id=opponent.uin,
        )

        user.allure_attach(response)

        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")
