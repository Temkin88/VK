import allure
import pytest

from pyvkteamsclient.stentor.exceptions import RequestException
from support.markers import SANDBOX
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CALENDAR)]


@allure.id("28435")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Calendar")
@allure.title("Метод /api/v1/calendar/createConference")
@SANDBOX
def test_create_conference(
    stentor,
    auth_account,
):
    with allure.step("Пытаемся создать конференцию"):
        response = stentor.calendar_createConference(
            email=auth_account.uin,
            name="Conference name",
        )

    with allure.step("Проверяем ответ"):
        assert "url" in response["results"], "No conference URL in response"
        assert response["results"]["url"] is not None, "Wrong conference URL"


@allure.id("28533")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Stentor")
@allure.feature("Calendar")
@allure.title("Метод /api/v1/calendar/createConference - ошибки")
@SANDBOX
@pytest.mark.parametrize("invalid_param", ["", 1234, [], {}, None])
def test_create_conference_error(
    stentor,
    invalid_param,
):
    with allure.step("Пытаемся создать конференцию"), pytest.raises(RequestException):
        stentor.calendar_createConference(
            email=invalid_param,
        )
