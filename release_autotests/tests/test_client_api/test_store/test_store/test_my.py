import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("30149")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Стикеры")
@allure.feature("Информация о стикерах")
@allure.title("Получение списка добавленных стикеров")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_store_my(
    auth_account,
):
    with allure.step("Получаем список стикер паков"):
        response = auth_account.store_my()

        assert "sticker_packs" in response["result"]
