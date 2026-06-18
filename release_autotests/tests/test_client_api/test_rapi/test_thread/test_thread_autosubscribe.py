import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("37513")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Треды")
@allure.feature("Подписка на тред")
@allure.title("Автоподписка на все треды чата")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_thread_autosubscribe(
    prepare_test_chats,
    ENV_PLATFORM,
):
    """
    Проверяем создание тредов
    """
    if ENV_PLATFORM == "TARM":
        pytest.skip("Отключается до устранения проблем по баге https://jira.vk.team/browse/IMSERVER-19077")

    main_acc, opponent, group, _ = prepare_test_chats
    chat = group

    with allure.step("Включаем автоподписку на треды"):
        main_acc.rapi_thread_autosubscribe(
            chatId=chat,
        )

    with allure.step("Проверяем что автоподписка включена"):
        response = main_acc.rapi_getChatInfo(sn=chat)
        auto_subscribe = response["results"]["threadsAutoSubscribeWithExisting"]

        assert auto_subscribe, f"{ENV_PLATFORM}: Autosubscribe to thread is disable"

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
        response = main_acc.rapi_thread_get(thread_id)
        assert response["results"]["you"]["subscriber"], f"{ENV_PLATFORM}: {main_acc.uin} not subscriber"

    with allure.step("Отправляем тестовое сообщение в тред"):
        opponent.send_basic_message(
            sn=thread_id,
            text="Test msg for thread",
        )

    with allure.step("Проверяем список подписчиков треда"):
        response = opponent.rapi_thread_subscribers_get(thread_id)

        subsribers_list = [x["sn"] for x in response["results"]["subscribers"]]

        assert main_acc.uin in subsribers_list, f"{ENV_PLATFORM}: Autosubscribe to thread is not working"
