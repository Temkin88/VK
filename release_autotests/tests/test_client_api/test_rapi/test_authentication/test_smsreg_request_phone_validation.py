import allure


@allure.id("86722")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Авторизация")
@allure.feature("Запрос смс кода для телефонного номера")
@allure.title("Запросить смс код для телефонного номера")
def test_smsreg_request_phone_validation(
    auth_account,
):
    """
    Проверяем запрос смс кода для телефонного номера

    Используемые параметры:
    :param auth_account: аккаунт ICQ
    """
    with allure.step("Пробуем запросить код для телефонного номера"):
        result = auth_account.smsreg_requestPhoneValidation()

        assert result["response"]["statusCode"] == 200, "Failed request"

        assert isinstance(result["response"]["requestId"], str), "Failed to type"

        assert result["response"]["data"]["phone_verified"], "Failed to phone verified"

        assert isinstance(result["response"]["data"]["trans_id"], str), "Failed to type"
