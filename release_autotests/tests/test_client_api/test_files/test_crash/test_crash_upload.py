import pathlib

import allure

from support.markers import VKTI, SAAS, TARM, SANDBOX, PRE_SAAS, PRE_VKTI, PRE_TARM


@allure.id("37358")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Крэши")
@allure.feature("Загрузка крэш дампа")
@allure.title("Загрузка крэш дампа")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_crash_upload(auth_account):
    with allure.step("Загружаем крэшдамп"):
        crachdump_path = pathlib.Path("support").joinpath("files").joinpath("common").joinpath("crashdump.zip")

        with crachdump_path.open(mode="rb") as f:
            response = auth_account.files_crash_upload(
                file=f,
            )
            assert response["status"]["code"] == 200
