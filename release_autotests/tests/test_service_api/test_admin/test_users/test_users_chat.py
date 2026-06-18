import allure

from support.markers import SANDBOX


@allure.id("79683")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Myteam-admin")
@allure.feature("Пользователи")
@allure.title(
    "Получение списка чатов пользователя",
)
@SANDBOX
def test_users_get_chats(
    admin_account,
    auth_account,
    user_id,
):
    """
    Проверяем получение списка чатов пользователея
    :param admin_account: Аккаунт с правами администратора
    :param auth_account: Основной аккаунт
    :param user_id: Фикстура для получения user_id аккаунта
    """
    with allure.step("Создаем чат"):
        chat_title = f"[{auth_account.getReqId()}]"
        chat_id = auth_account.create_chat(name=chat_title)

    with allure.step("Ищем чат в списке чатов пользователя"):
        response = admin_account.api_users_user_id_chats(
            user_id=user_id,
            filter_name=chat_title,
            filter_group=True,
            filter_channel=True,
        )

        assert chat_id in [x["id"] for x in response["result"]["chats"]], "Chat not found"
