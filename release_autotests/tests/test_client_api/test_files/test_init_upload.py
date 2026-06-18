import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("28161")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("Загрузка файлов")
@allure.title("Загрузка файлов разных типов")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_file_upload(
    auth_account,
    common_file,
):
    with allure.step("Пытаемся загрузить файл"):
        file_id, _ = auth_account.upload_file(
            file_path=common_file,
        )

    with allure.step("Проверяем ответ"):
        assert file_id, "File ID is not presented in response"
