import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.AUTHENTICATION)]


@allure.id("554603")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Авторизация")
@allure.feature("Сессии")
@allure.title("Завершение пользовательской сессии")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_aim_end_session(
    auth_account,
):
    """
    Завершение пользовательской сессии

    Используемые фикстуры:
    :param auth_account: пользовательский аккаунт
    """

    with allure.step("Пишем сообшение сами себе"):
        auth_account.send_basic_message(
            sn=auth_account.uin,
            text="test messages",
        )

    with allure.step("Пробуем завершить сессию"):
        response = auth_account.wim_aim_endSession()

        assert response["response"]["statusCode"] == 200, "Response code error"
