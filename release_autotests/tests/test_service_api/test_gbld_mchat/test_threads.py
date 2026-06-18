import allure

from support.markers import SANDBOX

from pyvkteamsclient.client.base.ipros.mchat_st.base_types import Anketa

from pyvkteamsclient.client.base.ipros.common.rid import Rid

@allure.id("2316309")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-mchat")
@allure.title("Положительные сценарии по работе с созданием тредов в чатах")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_threads(
    auth_account,
    opponent_account,
    create_chat,
    write_to_chat,
    add_thread,
    get_all_threads
    ):
    chat_name = "test chat"
    chat_id = Rid(2, create_chat([auth_account.uin], Anketa(name=chat_name)).chatId)

    message_id_first = write_to_chat(
        chat_id=chat_id,
        plain="Корова в бомболюке").messageId

    message_id_second = write_to_chat(
        chat_id=chat_id,
        plain="Корова в бомболюке 1").messageId

    add_thread(
        chat_id=chat_id,
        message_id=message_id_first,
        sender_sn=auth_account.uin,
        default_role=0xffffffff)

    add_thread(
        chat_id=chat_id,
        message_id=message_id_second,
        sender_sn=auth_account.uin,
        default_role=0xffffffff)

    threads = get_all_threads(chat_id=chat_id).threads
    assert len(threads) == 2, "Ошибка при получении созданных тредов в чате"
