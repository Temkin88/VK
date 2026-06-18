import allure


@allure.id("91554")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Авторизация")
@allure.feature("Отправить проверочный код")
@allure.title(" Отправка проверочного кода")
def test_auth_send_code(
    auth_account,
):
    """
    Проверяем выполнение метода проверочного кода

    Используемые параметры:
    :param auth_account: аккаунт ICQ
    """
    with allure.step("Пробуем отправить запрос"):
        response = auth_account.rapi_auth_send_сode()

        assert response["status"]["code"] == 20000, "Response code error"
        assert isinstance(response["results"]["sessionId"], str), "Attribute type not string"
        assert response["results"]["sessionId"], "ICQ object has no attribute sessionId"
