import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("842938")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Автоматическая подписка бота на треды в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_bot_auto_autosubscribe_to_threads(
    bot_class,
    auth_account,
):
    """
    Тест проверяет автоматическую подписку бота на треды в чате (без ручного вызова autosubscribe)
    По сути тестируем, что работает этот флаг mchat.enable_bots_to_auto_subscribe_to_chat_threads = true
    Также для работы теста он должен быть включенным в конфиге
    """
    chat = None
    with allure.step("1. Создаем тестовый чат"):
        chat = auth_account.create_chat(
            name="Test group for adding member",
        )

    with allure.step("2. Пробуем добавить пользователя в чат"):
        assert auth_account.rapi_group_members_add(
            sn=chat,
            members=[bot_class.uin],
            confirmUnblock=True,
        )

    with allure.step("3. Пользователь отправляет сообщение в чат"):
        msg_id = auth_account.send_basic_message(
            sn=chat,
            text="Test message for bot auto-subscription to thread",
        )
        assert msg_id, "Failed to send message to chat"

    with allure.step("4. Пользователь создает тред на сообщении"):
        thread_id = auth_account.add_thread(
            chat_id=chat,
            msg_id=msg_id,
        )
        assert thread_id, "Failed to create thread from message"

    with allure.step("5. Проверяем, что бот автоматически подписался на тред"):
        response = auth_account.rapi_thread_subscribers_get(thread_id)
        subscribers_list = [x["sn"] for x in response["results"]["subscribers"]]

        assert bot_class.uin in subscribers_list, (
            f"Bot {bot_class.uin} is not subscribed to thread {thread_id}, inside chat {chat}"
        )
