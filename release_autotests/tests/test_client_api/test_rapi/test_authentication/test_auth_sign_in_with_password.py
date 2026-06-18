import allure
import pytest


@allure.id("91555")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Авторизация")
@allure.feature("Авторизоваться по логину и паролю")
@allure.title("Авторизация по логину и паролю")
@pytest.mark.skip("Зависимость от реализации теста test_auth_reset_password")
def test_auth_sign_in_with_password(
    auth_account,
):
    """
    Проверяем авторизацию по логину и паролю

    Используемые параметры:
    :param auth_account: аккаунт ICQ
    """
    with allure.step("Пробуем отправить запрос"):
        auth_account.rapi_auth_sign_in_with_password(
            password="pa55word",
        )
