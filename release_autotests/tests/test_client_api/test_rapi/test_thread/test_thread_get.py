import allure
import pytest

from support.cases.formatted_msgs import formatted_msgs
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26931")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Треды")
@allure.feature("Информация о треде")
@allure.title("Информация о треде в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.parametrize("msg_parts", formatted_msgs)
def test_thread_get(
    chat_type,
    msg_parts,
    prepare_test_chats,
):
    """
    Проверяем создание тредов
    """
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

    with allure.step("Пытаемся получить информацию о треде"):
        threadId = response["results"]["threadId"]

        response = main_acc.rapi_thread_get(
            threadId=threadId,
        )

        assert response["status"]["code"] == 20000, f"Failed to get thread info from msgId {msg_id} in chat {chat}"

        assert response["results"]["threadId"] == threadId, "Wrong threadId in thread info"

        assert response["results"]["parentTopic"]["chatId"] == chat, "Wrong parent topic in thread info"

        assert response["results"]["parentTopic"]["messageId"] == msg_id, "Wrong parent msgId in thread info"
