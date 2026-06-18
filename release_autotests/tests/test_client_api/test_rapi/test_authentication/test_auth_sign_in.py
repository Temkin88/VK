import allure


@allure.id("91556")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Авторизация")
@allure.feature("Авторизоваться по телефону и проверочному коду")
@allure.title("Авторизация по телефону и проверочному коду")
def test_auth_sign_in(
    auth_account,
    session_id,
):
    """
    Проверяем авторизацию по телефону и проверочному коду

    Используемые параметры:
    :param auth_account: аккаунт ICQ
    :param session_id: Ид сессии
    """
    with allure.step("Пробуем отправить запрос"):
        response = auth_account.rapi_auth_sign_in(
            session_id=session_id,
        )
        assert response["results"]["sn"]
        assert response["results"]["token"]
