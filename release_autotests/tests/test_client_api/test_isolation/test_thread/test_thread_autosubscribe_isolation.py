import allure

from support.markers import SAAS, ISOLATION


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Треды")
@allure.feature("Подписка на тред")
@allure.title("Автоподписка на все треды чата")
@ISOLATION
@SAAS
def test_thread_autosubscribe_isolation(
    prepare_test_chats_msg_isolation,
):
    """
    Проверяем создание тредов
    """

    auth_account, opponent, group, _ = prepare_test_chats_msg_isolation
    chat = group

    with allure.step("Включаем автоподписку на треды"):
        auth_account.rapi_thread_autosubscribe(
            chatId=chat,
        )

    with allure.step("Проверяем что автоподписка включена"):
        response = auth_account.rapi_getChatInfo(sn=chat)
        auto_subscribe = response["results"]["threadsAutoSubscribeWithExisting"]

        assert auto_subscribe, "Autosubscribe to thread is disable"

    with allure.step("Отправляем тестовое сообщение"):
        msg_id = opponent.send_basic_message(
            sn=chat,
            text="Test msg for thread autosubscribe",
        )

    with allure.step("Создаем тред от этого сообщения"):
        thread_id = opponent.add_thread(
            chat_id=chat,
            msg_id=msg_id,
        )

    with allure.step("Проверяем что аккаунт добавился в подписчики"):
        response = auth_account.rapi_thread_get(thread_id)
        assert response["results"]["you"]["subscriber"], "{auth_account.uin} not subscriber"

    with allure.step("Отправляем тестовое сообщение в тред"):
        opponent.send_basic_message(
            sn=thread_id,
            text="Test msg for thread",
        )

    with allure.step("Проверяем список подписчиков треда"):
        response = opponent.rapi_thread_subscribers_get(thread_id)

        subsribers_list = [x["sn"] for x in response["results"]["subscribers"]]

        assert auth_account.uin in subsribers_list, "Autosubscribe to thread is not working"
