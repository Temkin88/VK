import allure

from support.markers import SANDBOX


@allure.id("79685")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Пользователи")
@allure.title(
    "Сброс сессии пользователя",
)
@SANDBOX
def test_users_session_hash_reset(
    admin_account,
    auth_account,
    user_id,
):
    """
    Проверяем сброс сессии пользователя
    :param admin_account: Аккаунт с правами администратора
    :param auth_account: Основной аккаунт
    :param user_id: Фикстура для получения user_id аккаунта
    """
    with allure.step("Пробуем получить списка пользователя"):
        response = admin_account.api_users_user_id_sessions(
            user_id=user_id,
        )

        assert len(response["result"]["sessions"]), "Wrong sessions count"

    with allure.step("Пробуем сбросить сессии"):
        for session in response["result"]["sessions"]:
            admin_account.api_users_user_id_sessions_hash_reset(
                user_id=user_id,
                session_id=session["id"],
            )
