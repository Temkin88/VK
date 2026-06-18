import pathlib

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26941")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Чаты")
@allure.feature("Добавление аватара в чат")
@allure.title("Добавление аватара в чат")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_set_avatar_to_existing_chat(
    chat_type,
    prepare_test_chats,
):
    """
    Проверяем добавление аватара в чат без аватара
    """

    main_acc, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    with allure.step(f"Загружаем аватар сразу с указанием ID чата {chat}"):
        png_path = pathlib.Path("support").joinpath("files").joinpath("common").joinpath("download.png")

        with png_path.open(mode="rb") as f:
            response = main_acc.files_avatar_set(
                target=chat,
                file=f,
            )

            response.raise_for_status()
