import allure
import pytest

from support.cases.formatted_msgs import formatted_msgs
from support.markers import SAAS, ISOLATION


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Создание треда")
@allure.title("Создание треда в чате")
@ISOLATION
@SAAS
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.parametrize("msg_parts", formatted_msgs)
def test_create_thread_isolation(
    chat_type,
    msg_parts,
    prepare_test_chats_msg_isolation,
):
    """
    Проверяем создание тредов
    """
    auth_account, opponent, group, channel = prepare_test_chats_msg_isolation

    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем тестовое сообщение"):
        response = auth_account.wim_im_sendIM(
            t=chat,
            parts=msg_parts,
        )
        msg_id = response["response"]["data"]["histMsgId"]

    with allure.step(f"Пытаемся создать тред от сообщения ID {msg_id}"):
        response = auth_account.rapi_thread_add(
            chatId=chat,
            messageId=msg_id,
        )
        thread_id = response["results"]["threadId"]
        assert response["status"]["code"] == 20000, f"Failed to create thread from msgId {msg_id} in chat {chat}"

    with allure.step(
        f"Пытаемся отправить сообщение в тред ID {thread_id}",
    ):
        response = auth_account.send_basic_message(
            sn=response["results"]["threadId"],
            text="Test msg to thread",
        )
        assert response, f"Failed to send msgId {msg_id} in thread {thread_id}"

    with allure.step(f"Пытаемся создать тред оппонентом от сообщения ID {msg_id}"):
        response = opponent.rapi_thread_add(
            chatId=chat,
            messageId=msg_id,
        )

        assert response["status"]["code"] == 20000, f"Failed to create thread from msgId {msg_id} in chat {chat}"

    with allure.step(
        f"Пытаемся отправить сообщение в тред оппонентом ID {response['results']['threadId']}",
    ):
        assert opponent.send_basic_message(
            sn=response["results"]["threadId"],
            text="Test msg to thread",
        )


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Тред задачи")
@allure.title("Доступ к треду задачи участника чата с разными ролями")
@ISOLATION
@SAAS
@pytest.mark.parametrize(
    ("chat_type", "chat_role"),
    [
        ("group", "admin"),
        ("group", "member"),
        ("channel", "admin"),
        ("channel", "member"),
        ("channel", "readonly"),
    ],
)
def test_check_task_thread_access_by_chat_role_isolation(
    first_auth_account_in_tenant,
    second_auth_account_in_tenant,
    chat_type,
    chat_role,
    ENV_PLATFORM,
):
    with allure.step("Создаем чат"):
        chat_id = first_auth_account_in_tenant.create_chat(
            members=[second_auth_account_in_tenant],
            defaultRole="member" if chat_type == "group" else "readonly",
        )

    with allure.step("Меняем роль участника"):
        first_auth_account_in_tenant.rapi_modChatMember(
            memberSn=second_auth_account_in_tenant.uin,
            sn=chat_id,
            role=chat_role,
        )

    with allure.step("Создаем задачу и ее тред"):
        msg_id, task_id = first_auth_account_in_tenant.task_add_by_sendIM(
            chat_id=chat_id,
        )

        thread_id = second_auth_account_in_tenant.add_thread(
            chat_id=chat_id,
            msg_id=msg_id,
        )
    with allure.step(f"Пишем ее тред под другим пользователем домена {second_auth_account_in_tenant}"):
        second_auth_account_in_tenant.send_basic_message(
            sn=thread_id,
            text=f"Test {second_auth_account_in_tenant}",
        )

    with allure.step(
        f"Проверяем что второй пользователь с ролью {chat_role} может подписаться и читать тред",
    ):
        opponent_thread_id = second_auth_account_in_tenant.add_thread(
            chat_id=chat_id,
            msg_id=msg_id,
        )

        assert opponent_thread_id == thread_id, f"Thread id not equal to opponent thread_id {thread_id}"

        second_auth_account_in_tenant.rapi_getHistory(
            sn=thread_id,
            fromMsgId="-1",
            count=20,
            patchVersion="init",
        )

        second_auth_account_in_tenant.send_basic_message(
            sn=thread_id,
            text="Test",
        )
