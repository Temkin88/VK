import allure

from support.markers import SANDBOX


@allure.id("28696")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Пользователи")
@allure.title(
    "Получение списка пользователей",
)
@SANDBOX
def test_users_id(
    admin_account,
    auth_account,
):
    """
    Проверяем получение списка пользователей
    :param admin_account: Аккаунт с правами администратора
    :param auth_account: Основной аккаунт
    """
    with allure.step("Пробуем получить список пользователей"):
        response = admin_account.api_users(
            filter_name=auth_account.uin,
            filter_blocked=False,
            filter_last_activity=0,
            filter_never_went=False,
            domains=["autotest.clients"],
        )

        assert auth_account.uin in [x["email"] for x in response["result"]["users"]], "User not found"
