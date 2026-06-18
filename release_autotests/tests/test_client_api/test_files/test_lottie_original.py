import allure

from support.markers import SAAS, VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("76637")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("Стикер")
@allure.title("Получаем стикер")
@SAAS
@PRE_SAAS
@VKTI
@PRE_VKTI
@TARM
@PRE_TARM
@SANDBOX
def test_lottie_original(
    auth_account,
    get_lottie_id,
):
    with allure.step("Пробуем получить стикер"):
        auth_account.files_lottie_original(file_id=get_lottie_id)
