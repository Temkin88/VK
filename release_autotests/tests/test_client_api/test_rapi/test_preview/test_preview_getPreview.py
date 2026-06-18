import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.MESSAGING)]


@allure.id("79711")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Сообщения")
@allure.feature("Сниппет")
@allure.title("Получение сниппета")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@pytest.mark.parametrize(
    "url",
    [
        "mail",
        "rambler",
    ],
)
def test_get_snippet_success(auth_account, url):
    with allure.step("Получаем сниппет"):
        response = auth_account.misc_preview_getPreview(
            url=f"https://{url}.ru",
        )

    with allure.step("Проверяем ответ"):
        assert response["status"] == "OK", "Status is not OK"
        assert response["status_code"] == "0", "Status code is not 0"
        assert response["http_code"] == "200", "HTTP code is not 200"
        assert "doc" in response, "Doc not found"


@allure.id("30206")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Сообщения")
@allure.feature("Сниппет")
@allure.title("Ошибка получения сниппета")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@pytest.mark.parametrize(
    "url",
    [
        # "ya",
        "vkorobov.v3.im-sandbox.devmail",
    ],
)
def test_get_snippet_fail(auth_account, url):
    with allure.step("Получаем сниппет"):
        response = auth_account.misc_preview_getPreview(
            url=f"https://{url}.ru",
        )

    with allure.step("Проверяем ответ"), pytest.raises(AssertionError):
        assert response["status"] == "OK", "Status is not OK"
        assert response["status_code"] == "0", "Status code is not 0"
        assert response["http_code"] == "200", "HTTP code is not 200"
        assert "doc" in response, "Doc not found"
