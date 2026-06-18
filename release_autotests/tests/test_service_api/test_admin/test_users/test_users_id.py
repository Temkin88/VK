import allure

from support.markers import SANDBOX


@allure.id("79684")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Пользователи")
@allure.title(
    "Получение информации о пользователе",
)
@SANDBOX
def test_users_get_by_id(
    admin_account,
    auth_account,
    user_id,
):
    """
    Проверяем получение информации о пользователе
    :param admin_account: Аккаунт с правами администратора
    :param auth_account: Основной аккаунт
    :param user_id: Фикстура для получения user_id аккаунта
    """
    with allure.step("Пробуем получить список пользователей"):
        response = admin_account.api_users_user_id(
            user_id=user_id,
        )

        assert auth_account.uin == response["result"]["email"], "Wrong user email"
