import allure
import pytest

from support.cases.formatted_msgs import formatted_msgs
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("41698")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Подписка на тред")
@allure.title("Подписка и отписка от треда в чате, проверка поля you")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.parametrize("msg_parts", formatted_msgs)
def test_thread_check_you_not_subscribed(
    chat_type,
    msg_parts,
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

    with allure.step("Отправляем тестовую задачу"):
        msg_id = main_acc.wim_im_sendIM(
            t=chat,
            parts=msg_parts,
        )["response"]["data"]["histMsgId"]

    with allure.step(f"Пытаемся создать тред от сообщения ID {msg_id}"):
        response = main_acc.rapi_thread_add(
            chatId=chat,
            messageId=msg_id,
        )

        assert response["status"]["code"] == 20000, f"Failed to create thread from msgId {msg_id} in chat {chat}"

        threadId = response["results"]["threadId"]

        main_acc.send_basic_message(
            sn=threadId,
            text="test",
        )

    with allure.step("Пытаемся отписаться от треда"):
        response = main_acc.rapi_thread_unsubscribe(
            threadId=threadId,
        )

        assert response["status"]["code"] == 20000, (
            f"Failed to unsubscribe from thread from msgId {msg_id} in chat {chat}"
        )

    with allure.step("Проверяем поле you"):
        response = main_acc.rapi_thread_get(
            threadId=threadId,
        )
        assert not response["results"]["you"]["subscriber"], "Falsely subscribed"
