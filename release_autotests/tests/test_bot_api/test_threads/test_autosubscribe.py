import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("842937")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Автоподписка на треды в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.parametrize("enable", ["true", "false"])
@pytest.mark.parametrize("with_existing", ["true", "false"])
def test_bot_autosubscribe_to_threads(
    start_bot,
    auth_account,
    bot_class,
    chat_type,
    enable,
    with_existing,
    prepare_bot_test_chats,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step(f"Автоподписываемся на треды чата с enable={enable}, with_existing={with_existing}"):
        response = bot_class.threads_autosubscribe(
            chat_id=chat,
            enable=enable,
            with_existing=with_existing,
        )

        auth_account.allure_attach(response)

        response.raise_for_status()

        response_json = response.json()

        assert response_json.get("ok", False), response_json.get("description")
