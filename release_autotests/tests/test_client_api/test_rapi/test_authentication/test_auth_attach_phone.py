import allure
import pytest


@allure.id("91552")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Авторизация")
@allure.feature("Начать OpenID Connect авторизацию")
@allure.title("OIDC авторизация через IDP, зарегистрированный на сервере")
@pytest.mark.skip("Уточняется у разработчика правильность реализации запроса")
def test_auth_attach_phone(
    auth_account,
    session_id,
):
    """
    Проверяем привязку номера телефона

    Используемые параметры:
    :param auth_account: аккаунт ICQ
    :param session_id: Ид сессии
    """
    with allure.step("Пробуем отправить запрос"):
        response = auth_account.rapi_auth_attach_phone(
            session_id=session_id,
        )
        assert response["results"]["sn"]
