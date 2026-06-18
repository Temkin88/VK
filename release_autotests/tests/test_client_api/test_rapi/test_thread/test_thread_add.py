import allure
import pytest

from support.cases.formatted_msgs import formatted_msgs
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26938")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Создание треда")
@allure.title("Создание треда в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.parametrize("msg_parts", formatted_msgs)
def test_create_thread(
    chat_type,
    msg_parts,
    prepare_test_chats,
):
    """
    Проверяем создание тредов
    """
    main_acc, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем тестовое сообщение"):
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

    with allure.step(
        f"Пытаемся отправить сообщение в тред ID {response['results']['threadId']}",
    ):
        assert main_acc.send_basic_message(
            sn=response["results"]["threadId"],
            text="Test msg to thread",
        )


@allure.id("21728")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Тред задачи")
@allure.title("Доступ к треду задачи участника чата с разными ролями")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
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
def test_check_task_thread_access_by_chat_role(
    auth_account,
    opponent_account,
    chat_type,
    chat_role,
    ENV_PLATFORM,
):
    if ENV_PLATFORM == "TARM":
        pytest.skip("Отключается до устранения проблем по баге https://jira.vk.team/browse/IMSERVER-19077")

    with allure.step("Создаем чат"):
        chat_id = auth_account.create_chat(
            members=[opponent_account],
            defaultRole="member" if chat_type == "group" else "readonly",
        )

    with allure.step("Меняем роль участника"):
        auth_account.rapi_modChatMember(
            memberSn=opponent_account.uin,
            sn=chat_id,
            role=chat_role,
        )

    with allure.step("Создаем задачу и ее тред"):
        msg_id, task_id = auth_account.task_add_by_sendIM(
            chat_id=chat_id,
        )

        thread_id = auth_account.add_thread(
            chat_id=chat_id,
            msg_id=msg_id,
        )

    with allure.step(
        f"Проверяем что второй пользователь с ролью {chat_role} может подписаться и читать тред",
    ):
        opponent_thread_id = opponent_account.add_thread(
            chat_id=chat_id,
            msg_id=msg_id,
        )

        assert opponent_thread_id == thread_id

        opponent_account.rapi_getHistory(
            sn=thread_id,
            fromMsgId="-1",
            count=20,
            patchVersion="init",
        )

        opponent_account.send_basic_message(
            sn=thread_id,
            text="Test",
        )
