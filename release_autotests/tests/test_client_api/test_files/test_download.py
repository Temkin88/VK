import pathlib
import urllib.parse

import allure
import pytest
import requests

from support.markers import TARM, PRE_TARM, VKTI, PRE_VKTI, SAAS, PRE_SAAS, SANDBOX


@allure.id("38605")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("Скачивание файлов")
@allure.title("Скачивание файла по прямой ссылке")
@allure.label("jira", "IMSERVER-14748")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "filepath",
    pathlib.Path("support/files/common").glob("file_example_name_*.txt"),
    ids=lambda x: x.name,
)
def test_file_download(
    auth_account,
    filepath: pathlib.Path,
):
    with allure.step("Загружаем файл"):
        file_id, _ = auth_account.upload_file(filepath)

    with allure.step("Получаем ссылку на скачивание"):
        file_info = auth_account.get_file_info(file_id)
        download_link = file_info["info"]["dlink"]

    with allure.step("Скачиваем файл по полученной ссылке"):
        response = requests.get(download_link)
        assert response.status_code == 200

    with allure.step("Проверяем заголовок Content-Disposition"):
        content_disposition = response.headers["Content-Disposition"]
        escaped_filename = urllib.parse.quote(filepath.name)

        # IMSERVER-14748. Этот вариант кодировки не в полной мере соответствует
        # стандарту, но для сохранения обратной совместимости (Android-клиент)
        # сервер кодирует именно так. Подробности см. в задаче.
        expected = "attachment; filename*=UTF-8''{}; filename=\"{}\"".format(
            escaped_filename,
            filepath.name,
        )
        expected = expected
        expected = expected.encode("UTF-8").decode("ISO-8859-1")

        assert content_disposition == expected, "Значение заголовка Content-Disposition не соответствует ожиданию"

    with allure.step("Проверяем содержимое файла"):
        file_data = filepath.read_bytes()

        assert response.content == file_data, "Содержимое загруженного и скаченного файлов различно"
