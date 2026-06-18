import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.AUTHENTICATION)]


@allure.id("67286")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Авторизация")
@allure.feature("Сессии")
@allure.title("Изменить параметры пользовательской сессии")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_session_param_set(
    auth_account,
    event_filter,
    fetch_until_empty_answer_with_filter,
):
    type_my_info = False

    with allure.step('Проверяем что в стартовой сессии присутствуют все "capabilities"'):
        for event in fetch_until_empty_answer_with_filter(auth_account, "myInfo"):
            if event["type"] == "myInfo":
                assert all(
                    event_capabilities in auth_account.assert_caps
                    for event_capabilities in event["eventData"]["capabilities"]
                ), "Some of assertedCaps not found"
                assert all(
                    event_capabilities in event["eventData"]["capabilities"]
                    for event_capabilities in auth_account.assert_caps
                ), "Some of assertedCaps not found"
                type_my_info = True
            assert type_my_info, "Type myInfo not found"

    with allure.step("Пробуем изменить параметры сессии"):
        response = auth_account.wim_aim_setSessionParam(sessionTimeout=123445, language="ru-RU")["response"]
        assert response["statusCode"] == 200, "Response code error"
