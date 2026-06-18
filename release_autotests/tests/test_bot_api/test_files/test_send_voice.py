import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("37483")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Отпрака голосового сообщения по fileId через BotAPI")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_bot_get_send_voice(
    start_bot,
    auth_account,
    bot_class,
    uploaded_speechtottext_file_id,
):
    with allure.step("Пробуем отправить файл через fileId"):
        response = bot_class.send_voice(
            chat_id=auth_account.uin,
            file_id=uploaded_speechtottext_file_id,
        )

        auth_account.files_info(uploaded_speechtottext_file_id)

        auth_account.allure_attach(response)

        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")


@allure.id("37490")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Отпрака голосового сообщения через BotAPI")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_bot_post_send_voice(
    start_bot,
    auth_account,
    bot_class,
    speechtottext_file,
):
    with allure.step("Пробуем отправить файл"):
        with speechtottext_file.open(mode="rb") as f:
            response = bot_class.send_voice(
                chat_id=auth_account.uin,
                file=f,
            )

        auth_account.allure_attach(response)

        response.raise_for_status()

        response_info = response.json()

        assert response_info.get("ok", False), response_info.get("description")
