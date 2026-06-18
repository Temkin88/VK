import pathlib

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("37493")
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
@pytest.mark.parametrize("avatar_size", [64, 128, 256, 1024])
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_set_avatar_to_existing_chat(
    chat_type,
    avatar_size,
    prepare_test_chats,
):
    """
    Проверяем добавление аватара в чат без аватара
    """

    main_acc, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    with allure.step(f"Загружаем аватар сразу с указанием ID чата {chat}"):
        png_path = pathlib.Path("support").joinpath("files").joinpath("common").joinpath("download.png")

        with png_path.open("rb") as f:
            response = main_acc.files_avatar_set(
                target=chat,
                file=f,
            )

            response.raise_for_status()

    with allure.step("Пробуем получить аватар в чате"):
        response = main_acc.files_avatar_get_by_sn(
            sn=chat,
            size=avatar_size,
        )

        assert response.status_code == 200, "Wrong status code, 200 OK was awaited"

        last_modified_date = response.headers["Last-Modified"]

    with allure.step("Повторно пробуем получить аватар с указанием Last-Modified"):
        response = main_acc.files_avatar_get_by_sn(
            sn=chat,
            size=avatar_size,
            last_modified_data=last_modified_date,
        )

        assert response.status_code == 304, "Wrong status code, 304 Not Modified was awaited"
