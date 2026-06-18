import allure

from pyvkteamsclient.client.base.ipros.mchat_st.base_types import ParentTopic
from support.markers import SANDBOX

@allure.id("2310464")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с чатами с помощью mchat-st")
@allure.title("Прочие положительные сценарии")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_chat_happy_cases(
    auth_account,
    opponent_account,
    create_chat,
    get_chat_info,
    get_chat_id_info,
    send_message,
    pin_message,
    delete_message,
    create_thread,
    trigger_avatar_changed,
    get_permissions,
    get_permissions_extended,
    get_recent_writers,
    modify_member,
):
    chat_id = create_chat([auth_account.uin, opponent_account.uin]).chatId

    get_chat_info(chat_id)
    get_chat_id_info(chat_id)

    msg_id = send_message(chat_id, "test message").messageId
    create_thread(chat_id, ParentTopic.MessageTopic(chat_id, msg_id))

    pin_message(chat_id, msg_id)
    delete_message(chat_id, [msg_id])

    trigger_avatar_changed(chat_id)

    get_permissions(chat_id)
    get_permissions_extended(chat_id)
    get_recent_writers(chat_id)

    modify_member(chat_id, opponent_account.uin, isAdmin=True)
