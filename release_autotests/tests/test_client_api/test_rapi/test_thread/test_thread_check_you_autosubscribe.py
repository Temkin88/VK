import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("41410")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Треды")
@allure.feature("Подписка на тред")
@allure.title("Автоподписка на все треды чата, проверка поля you")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group"])
def test_thread_check_you_autosubscribe(
    chat_type,
    prepare_test_chats,
    ENV_PLATFORM,
):
    """
    Проверяем создание тредов
    """
    if ENV_PLATFORM == "TARM":
        pytest.skip("Отключается до устранения проблем по баге https://jira.vk.team/browse/IMSERVER-19077")

    main_acc, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    with allure.step("Включаем автоподписку на треды"):
        main_acc.rapi_thread_autosubscribe(
            chatId=chat,
        )

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

    with allure.step("Проверяем поле you"):
        response = main_acc.rapi_thread_get(
            threadId=thread_id,
        )
        assert response["results"]["you"]["subscriber"], "Not subscribed"
