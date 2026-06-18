import pathlib
from hashlib import md5

import allure

from support.markers import VKTI, SAAS, TARM, SANDBOX, PRE_SAAS, PRE_VKTI, PRE_TARM


@allure.id("37356")
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
# @pytest.mark.skip("IMQA-1094: Needs some infrastructure work")
def test_crash_download(
    auth_account,
):
    initial_file = pathlib.Path("support/files/common").joinpath("crashdump.zip")

    initial_file_md5 = md5(initial_file.read_bytes()).hexdigest()

    with allure.step("Загружаем крэшдамп"), initial_file.open(mode="rb") as f:
        auth_account.files_crash_upload(
            file=f,
        )

    with allure.step("Получаем список крэшей"):
        response = auth_account.files_crash_list("desktop")

        crashes_list = list(filter(lambda x: auth_account.uin in x, response["result"]))

    with allure.step("Пытаемся скачать крэшдамп"):
        response = auth_account.files_crash_download(
            file_name=crashes_list[-1],
        )

    with allure.step("Сравниваем md5 суммы первичного и скачанного файла"):
        assert md5(response.content).hexdigest() == initial_file_md5, "MD5 check failed"
