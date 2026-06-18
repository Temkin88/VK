import allure

from support.markers import SAAS, PRE_SAAS


@allure.id("79710")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("Загрузка файлов")
@allure.title("Загрузка файлов разных типов")
@SAAS
@PRE_SAAS
def test_file_upload_full(
    auth_account,
    opponent_account,
    common_file,
):
    with allure.step("Пытаемся загрузить файл"):
        response = auth_account.files_direct_upload(
            chat_id=opponent_account.uin,
            file_path=common_file,
            type_format=None,
            chunk_size=common_file.stat().st_size,
        )
        assert response["status"]["code"] == 200, "Response code error"
        assert response["result"]["filename"] == common_file.name, "File not found"


@allure.id("75317")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("Загрузка файлов")
@allure.title("Загрузка чанками файлов разных типов")
@SAAS
@PRE_SAAS
def test_file_upload_chunked(
    auth_account,
    opponent_account,
    speechtottext_file,
):
    with allure.step("Пытаемся загрузить файл"):
        response = auth_account.files_direct_upload(
            chat_id=opponent_account.uin,
            file_path=speechtottext_file,
        )
        assert response["status"]["code"] == 200, "Response code error"
        assert response["result"]["filename"] == speechtottext_file.name, "File not found"
