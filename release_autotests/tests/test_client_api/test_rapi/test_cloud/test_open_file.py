import time

import allure

from support.markers import TARM, PRE_TARM, SANDBOX, VKTI, PRE_VKTI, SAAS, PRE_SAAS


@allure.id("31440")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("jira", "IMQA-974")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Файлы")
@allure.feature("Загрузка файлов")
@allure.title("Открытие файла в облаке")
def test_open_file(
    opponent_account,
    photo_id,
):
    with allure.step("Запускаем сохранение файла в облаке"):
        opponent_account.rapi_cloud_initFileSave(
            file_id=photo_id,
            source="",
            folder="/",
        )

        time.sleep(5)

    with allure.step("Пытаемся открыть файл в облаке"):
        response = opponent_account.rapi_cloud_openFile(
            file_id=photo_id,
            source="",
        )

        assert "link" in response["results"], "Link to cloud not found"
