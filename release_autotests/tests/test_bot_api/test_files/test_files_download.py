import allure

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("32493")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Скачивание файлов по ссылке из files/info")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_bot_files_download(
    start_bot,
    auth_account,
    session,
    bot_class,
    common_file,
    uploaded_common_file_url,
):
    for i in range(1, 11):
        with allure.step(f"Попытка #{i} скачивания файлов"):
            with allure.step("Пробуем получить ссылку на скачивание файла"):
                response = bot_class.get_file_info(
                    file_id=uploaded_common_file_url.split("/")[-1],
                )

                auth_account.allure_attach(response)

                download_url = response.json()["url"]

            with allure.step("Пытаемся скачать файл по полученной ссылке"):
                response = session.get(download_url)

                auth_account.allure_attach(response)

                response.raise_for_status()
