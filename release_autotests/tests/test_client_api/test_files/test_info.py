import pathlib

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, SLA, PRE_SAAS


@allure.id("28154")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("Загрузка файлов")
@allure.title("Получение информации о файле по ID")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@SLA
@pytest.mark.parametrize(
    "filename",
    pathlib.Path().joinpath("support").joinpath("files").joinpath("common").glob("*.*"),
    ids=lambda x: x.name,
)
def test_file_info(
    auth_account,
    opponent_account,
    filename: pathlib.Path,
):
    file_size = filename.stat().st_size

    previews = ("iphone_retina", "xlarge")

    with allure.step("Пытаемся загрузить файл"):
        file_id, _ = auth_account.upload_file(
            str(filename.absolute()),
        )

    with allure.step("Делаем запрос информации о файле"):
        response = opponent_account.files_info(
            file_id=file_id,
            previews=previews,
        )["result"]

    with allure.step("Проверяем ответ"):
        has_preview = (
            "image" in response["info"]["mime"]
            and "svg" not in response["info"]["mime"]
            and "tiff" not in response["info"]["mime"]
            and "x-icon" not in response["info"]["mime"]
        ) or "video" in response["info"]["mime"]

        assert response["info"]["has_previews"] == has_preview, "Wrong has_previews state"
        assert set(previews) == set(response["previews"].keys()), "Wrong 'previews' value'"
        assert response["info"]["file_size"] == file_size, "File size not equal"

    with allure.step("Проверяем ссылку на скачивание"):
        response = opponent_account.session.get(response["info"]["dlink"])

        response.raise_for_status()
