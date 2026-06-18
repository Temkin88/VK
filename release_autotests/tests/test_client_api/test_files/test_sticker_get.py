import allure

from support.markers import SAAS, SANDBOX, VKTI, PRE_VKTI, TARM, PRE_TARM, PRE_SAAS


@allure.id("75346")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Файлы")
@allure.feature("Стикер")
@allure.title("Скачивание стикера по file_id")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_sticker_get(
    auth_account,
    get_sticker_id,
):
    with allure.step("Пробуем получить стикер"):
        response = auth_account.files_sticker_get(get_sticker_id)
        assert response.status_code == 200, "Response code error"
