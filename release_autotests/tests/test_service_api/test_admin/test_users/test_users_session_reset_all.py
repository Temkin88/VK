import allure

from support.markers import SANDBOX


@allure.id("79686")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Пользователи")
@allure.title(
    "Сброс всех сессий пользователя",
)
@SANDBOX
def test_users_reset_all_sessions(
    admin_account,
    auth_account,
    user_id,
):
    """
    Проверяем сброс всех сессий пользователя
    :param admin_account: Аккаунт с правами администратора
    :param auth_account: Основной аккаунт
    :param user_id: Фикстура для получения user_id аккаунта
    """
    with allure.step("Пробуем получить списка пользователя"):
        response = admin_account.api_users_user_id_sessions(
            user_id=user_id,
        )

        assert len(response["result"].get("sessions", []) or []), f"{auth_account.env}:Wrong sessions count"

    with allure.step("Пробуем сбросить сессии"):
        admin_account.api_users_user_id_reset_all_sessions(
            user_id=user_id,
        )
