import pathlib
import allure
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM


@allure.id("865552")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Файлы")
@allure.title("Получение доступа к файлу, когда нет превышения 1-го порога")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@DLP
def test_upload_file_get_info_before_response(chat_entities):
    main_acc, opponent, _ = chat_entities

    file = (
        pathlib.Path("support")
        .joinpath("files")
        .joinpath("dlp")
        .joinpath("fake_file_without_sensitive_information_with_long_time_answer.json")
    )

    with allure.step("Пытаемся загрузить файл"):
        file_id, rez = main_acc.upload_file(file.absolute())

    previews = ("iphone_retina", "xlarge")
    with allure.step("Делаем запрос информации о файле"):
        response = opponent.files_info(
            file_id=file_id,
            previews=previews,
        )
        files_info_response = response["result"]

    with allure.step("Проверяем доступность файла"):
        response = opponent.session.get(files_info_response["info"]["dlink"]).json()
        assert response["status"]["code"] == 425, "Есть доступ к файлу"
        response = main_acc.session.get(files_info_response["info"]["dlink"]).json()
        assert response["status"]["code"] == 425, "Есть доступ к файлу"
