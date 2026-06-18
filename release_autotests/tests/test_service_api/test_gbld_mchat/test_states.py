import allure

from support.markers import SANDBOX

from pyvkteamsclient.client.base.ipros.mchat_st.base_types import Anketa

from pyvkteamsclient.client.base.ipros.common.rid import Rid

@allure.id("2316304")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-mchat")
@allure.title("Положительные сценарии по работе с состояниями в чатах")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_states(
    auth_account,
    opponent_account,
    create_chat,
    write_to_chat,
    add_thread,
    set_dlg_state,
    set_dlg_state_wim,
    get_state_chat
    ):
    chat_name = "test chat"
    chat_id = Rid(2, create_chat([auth_account.uin], Anketa(name=chat_name)).chatId)

    message_id_first = write_to_chat(
        chat_id=chat_id,
        plain="Корова в бомболюке").messageId

    message_id_second = write_to_chat(
        chat_id=chat_id,
        plain="Корова в бомболюке 1").messageId

    first_thread_id = add_thread(
        chat_id=chat_id,
        message_id=message_id_first,
        sender_sn=auth_account.uin,
        default_role=0xffffffff).threadId

    set_dlg_state(
        chat_id=chat_id,
        delivered_message_id=message_id_first,
        read_message_id=message_id_first)

    set_dlg_state_wim(
        chat_id=chat_id,
        delivered_message_id=message_id_second,
        read_message_id=message_id_second)

    get_state_chat(thread_id=first_thread_id, sender_sn=auth_account.uin)
