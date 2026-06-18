from typing import Optional

from pyvkteamsclient.client import DesktopClient
import allure


def cleanup_chat(*, acc: DesktopClient, chat_sn: str, uncleanable_messages: Optional[list[str]] = None):
    if acc.uin == chat_sn:
        return
    if uncleanable_messages is None:
        uncleanable_messages = []
    history = acc.rapi_getHistory(sn=chat_sn, count=-200)
    msgIds = [
        int(msg["msgId"])
        for msg in history["results"]["messages"]
        if (msg.get("outgoing") and int(msg["msgId"]) not in uncleanable_messages)
    ]
    if msgIds:
        for msgId in msgIds:
            response = acc.session.post(
                url=acc.api_url + "/rapi/delMsg",
                json={
                    "aimsid": acc.aimsid,
                    "reqId": acc.getReqId(),
                    "params": {"sn": chat_sn, "shared": True, "msgId": msgId},
                },
            )
            assert response.status_code == 200


def restore_prepared_chats(
    *,
    sender: DesktopClient,
    recipient: DesktopClient,
    group_sn,
    channel_sn,
    uncleanable_messages: Optional[list[str]] = None,
):
    with allure.step("Очищаем группу и чат от старых сообщений"):
        for actor in [sender, recipient]:
            for chat in [sender.uin, recipient.uin, group_sn, channel_sn]:
                cleanup_chat(acc=actor, chat_sn=chat, uncleanable_messages=uncleanable_messages)
    with allure.step("Принудительно проставляем роли участникам чата/группы"):
        response = sender.rapi_modChatMember(
            memberSn=recipient.uin,
            sn=group_sn,
            role="member",
        )
        assert response["status"]["code"] in [20000, 20100], "Wrong status code"
        response = sender.rapi_modChatMember(
            memberSn=recipient.uin,
            sn=channel_sn,
            role="readonly",
        )
        assert response["status"]["code"] in [20000, 20100], "Wrong status code"


def subscribe_thread_if_not_subscribed(*, acc: DesktopClient, thread_id: str):
    with allure.step("Проверяем подписан пи пользователь на трэд"):
        response = acc.rapi_thread_get(
            threadId=thread_id,
        )
    if not response["results"]["you"]["subscriber"]:
        with allure.step("Пользователь не подписан на трэд, подписываем"):
            acc.rapi_thread_subscribe(threadId=thread_id)
