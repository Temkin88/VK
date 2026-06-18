import allure
import pytest


@allure.id("91553")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Авторизация")
@allure.feature("Изменить пароль пользователя")
@allure.title("Изменение пароля пользователя")
@pytest.mark.skip("Уточняется у разработчика правильность реализации запроса")
def test_auth_reset_password(
    auth_account,
):
    """
    Проверяем изменение пароля пользователем

    Используемые параметры:
    :param auth_account: аккаунт ICQ
    """
    with allure.step("Пробуем отправить запрос"):
        auth_account.rapi_auth_reset_password(
            new_password="pa55word",
        )
