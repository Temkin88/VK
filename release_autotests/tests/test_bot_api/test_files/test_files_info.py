import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("27481")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Получение info о файлах через BotAPI")
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
def test_bot_files_info(
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
    with allure.step("Пробуем получить информацию о файле"):
        response = bot_class.get_file_info(
            file_id=eval(file_type),
        )

        auth_account.allure_attach(response)

        response_json = response.json()

        assert response_json["type"] == type_from_info, response.text
