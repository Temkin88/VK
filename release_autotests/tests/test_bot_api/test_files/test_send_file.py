import pathlib

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("37474")
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
@pytest.mark.parametrize(
    ("file_type", "type_from_info"),
    [
        ("photo_id", "image"),
        ("voice_id", "audio"),
        ("sticker_id", "image"),
        ("logs_file", "application"),
    ],
    ids=[
        "photo",
        "voice",
        "sticker",
        "logs_file",
    ],
)
def test_bot_get_send_file(
    start_bot,
    auth_account,
    bot_class,
    file_type,
    type_from_info,
    photo_id,
    voice_id,
    sticker_id,
    logs_file,
):
    with allure.step("Пробуем отправить файл через fileId"):
        response = bot_class.send_file(
            chat_id=auth_account.uin,
            file_id=eval(file_type),
        )

        auth_account.allure_attach(response)

        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")


@allure.id("37472")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Отправка файла через BotAPI")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "filename",
    pathlib.Path("support").joinpath("files").joinpath("common").glob("*.*"),
    ids=lambda x: x.name,
)
def test_bot_post_send_file(
    start_bot,
    auth_account,
    bot_class,
    filename,
):
    with allure.step("Пробуем отправить файл"):
        with filename.open(mode="rb") as f:
            response = bot_class.send_file(
                chat_id=auth_account.uin,
                file=f,
            )

        auth_account.allure_attach(response)

        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")
