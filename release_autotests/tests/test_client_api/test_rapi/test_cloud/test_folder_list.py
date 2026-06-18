import allure

from support.markers import TARM, PRE_TARM, SANDBOX, SAAS, VKTI, PRE_VKTI, PRE_SAAS


@allure.id("31438")
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
@allure.title("Список файлов в папке облака")
def test_folder_list(
    opponent_account,
    photo_id,
    event_filter,
    fetch_until_empty_answer,
):
    with allure.step("Запускаем сохранение файла в облаке"):
        opponent_account.rapi_cloud_folder_list()
