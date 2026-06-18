import allure

from pyvkteamsclient.client import DesktopClient
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.MINIAPPS)]


@allure.id("38604")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Миниаппы")
@allure.feature("Список миниаппов")
@allure.title("Получение информация о мини-аппе")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_miniapp_get(
    auth_account: DesktopClient,
    miniapp_id: str,
):
    with allure.step("Пробуем получить информацию о миниаппе"):
        response = auth_account.rapi_miniapp_get(miniapp_id)

        assert response["status"]["code"] == 20000, "Response code error"

    with allure.step("Проверяем наличие полей в ответе сервера"):
        miniapp_info = response["results"]

        for key in [
            "url",
            "name",
            "description",
        ]:
            assert key in miniapp_info, f"Key {key} not presented in miniapp info: {miniapp_info}"
