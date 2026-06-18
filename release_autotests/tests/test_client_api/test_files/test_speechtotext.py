import allure

from support.markers import VKTI, PRE_VKTI, SAAS


@allure.id("28160")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Файлы")
@allure.feature("S2T-T2S")
@allure.title("Распознование текста в голосовом сообщении")
@VKTI
@PRE_VKTI
@SAAS
def test_file_speechtotext(
    auth_account,
    uploaded_speechtottext_file_id,
):
    with allure.step("Запрашиваем расшифровку"):
        response = auth_account.files_speechtotext(
            file_id=uploaded_speechtottext_file_id,
        )

        assert response["status"] == 200, "Failed request"
        assert response["text"], f"Wrong text value: {response['text']}"


@allure.id("30227")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Файлы")
@allure.feature("S2T-T2S")
@allure.title("Закрепления текста за аудиозаписью")
@VKTI
@PRE_VKTI
def test_files_textforspeech(
    auth_account,
    uploaded_speechtottext_file_id,
):
    with allure.step("Закрепляем текст за аудиозаписью"):
        auth_account.files_textforspeech(
            file_id=uploaded_speechtottext_file_id,
            text="Текст для теста",
        )

    with allure.step("Запрашиваем расшифровку"):
        response = auth_account.files_speechtotext(
            file_id=uploaded_speechtottext_file_id,
        )

        assert response["status"] == 200, "Failed request"
        assert response["text"], f"Wrong text value: {response['text']}"
