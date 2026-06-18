import pathlib

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("37486")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Отпрака файла по fileId через BotAPI")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_chats_avatar_set(
    bot_class,
    prepare_bot_test_chats,
    chat_type,
):
    user, opponent, group, channel = prepare_bot_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Пробуем отправить файл через fileId"):
        file_path = pathlib.Path().joinpath("support").joinpath("files").joinpath("common").joinpath("download.png")

        with file_path.open(mode="rb") as f:
            response = bot_class.http_session.post(
                url="{}/chats/avatar/set".format(bot_class.api_base_url),
                params={
                    "token": bot_class.token,
                    "chatId": chat,
                },
                files={
                    "image": f,
                },
                timeout=bot_class.timeout_s,
            )

        user.allure_attach(response)

        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")
