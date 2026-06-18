import allure
import pytest


@allure.id("26894")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.suite("Авторизация")
@allure.feature("Авторизация по логину и паролю")
@allure.title("Проверка сложности пароля")
@pytest.mark.parametrize(
    ("pwd", "status_code"),
    [
        ("Aa568217", 20000),
        ("pa55word", 20003),
        ("\n\t", 20006),
        ("qwerty", 20008),
        ("qwerty" * 25, 20009),
    ],
)
def test_is_strong_password(
    pwd: str,
    status_code: int,
    auth_account,
):
    """
    Проверяем надежность пароля

    Используемые параметры:
    :param auth_account: аккаунт ICQ
    :param pwd: пароль
    :param status_code: код для пароля
    """
    result = auth_account.rapi_auth_is_strong_password(
        password=pwd,
    )

    assert 20000 <= result["status"]["code"] < 30000, "Failed request"
