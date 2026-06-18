import allure

from support.markers import VKTI, SAAS, PRE_SAAS, PRE_VKTI, TARM, PRE_TARM


@allure.id("37506")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Misc")
@allure.feature("Misc")
@allure.title("Получение файла по прямому URL")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
def test_preview_get_url_content(
    auth_account,
):
    with allure.step("Пробуем сделать запрос"):
        auth_account.misc_preview_getUrlContent(
            url="https://filesamples.com/samples/document/doc/sample2.doc",
        )
