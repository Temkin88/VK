import allure

from support.markers import SANDBOX


@allure.id("79687")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Пользователи")
@allure.title(
    "Получение списка сессий пользователя",
)
@SANDBOX
def test_users_get_sessions(
    admin_account,
    auth_account,
    user_id,
):
    """
    Проверяем получение списка сессий пользователея
    :param admin_account: Аккаунт с правами администратора
    :param auth_account: Основной аккаунт
    :param user_id: Фикстура для получения user_id аккаунта
    """
    with allure.step("Пробуем получить списка пользователя"):
        response = admin_account.api_users_user_id_sessions(
            user_id=user_id,
        )

        assert len(response["result"]["sessions"]), "Wrong sessions count"
