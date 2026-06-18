import allure
import lorem
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("37470")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Редактирование описания группы")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_set_chat_rules(
    bot_class,
    prepare_bot_test_chats,
    chat_type,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Пробуем правила чата"):
        response = bot_class.set_chat_rules(
            chat_id=chat,
            rules=lorem.sentence(),
        )

    with allure.step("Проверяем ответ"):
        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")
