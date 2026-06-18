import allure
import pytest
from pytest_check import raises
from pyvkteamsclient.client import ServerException

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("906793")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Поиск")
@allure.feature("Поиск по тредам")
@allure.title("Поиск сообщений в приватных чатах и каналах недопущенными к ним пользователями")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_search_on_threads_by_user_not_access_to_chat(chat_type, prepare_test_chats, third_account):
    """
    Проверяем что сообщения в приватных каналах и группах недоступны пользователям, не состоящим в них.
    """
    main_acc, opponent, group, channel = prepare_test_chats
    text_to_send = "Private text to thread"
    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем тестовое сообщение"):
        response = main_acc.wim_im_sendIM(
            t=chat,
            parts=[
                {
                    "mediaType": "text",
                    "text": "some text",
                },
            ],
        )
        msg_id = response["response"]["data"]["histMsgId"]

    with allure.step(f"Пытаемся создать тред от сообщения ID {msg_id}"):
        response = main_acc.rapi_thread_add(
            chatId=chat,
            messageId=msg_id,
        )

        assert response["status"]["code"] == 20000, f"Failed to create thread from msgId {msg_id} in chat {chat}"
        thread_id = response["results"]["threadId"]

    with allure.step(
        f"Пытаемся отправить сообщение в тред ID {thread_id}",
    ):
        assert main_acc.send_basic_message(
            sn=thread_id,
            text=text_to_send,
        )
    with (
        allure.step(
            "Пытаемся сторонним пользователем искать приватный текст в трэде",
        ),
        raises(ServerException),
    ):
        third_account.post(
            "rapi/searchChatThreads",
            headers={"Content-Type": "application/json"},
            json={
                "reqId": third_account.getReqId(),
                "aimsid": third_account.aimsid,
                "params": {
                    "pagesize": 50,
                    "filter": {
                        "keyword": text_to_send[0:3],
                        "data": {},
                    },
                    "sn": chat,
                },
            },
        )
