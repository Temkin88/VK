import allure

from support.markers import SANDBOX

from pyvkteamsclient.client.base.ipros.mchat_st.base_types import Anketa

from pyvkteamsclient.client.base.ipros.common.rid import Rid


@allure.id("2316298")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-mchat")
@allure.title("Положительные сценарии по работе с удалением сообщений в чатах")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_del(
    auth_account,
    opponent_account,
    create_chat,
    write_to_chat,
    del_msg,
    ):
    chat_name = "test chat"
    chat_id = Rid(2, create_chat([auth_account.uin], Anketa(name=chat_name)).chatId)

    message_id_first = write_to_chat(
        chat_id=chat_id,
        plain="Корова в бомболюке").messageId

    response_del = del_msg(
        chat_id=chat_id,
        additional_msgs=[message_id_first, message_id_first + 999999])

    assert len(response_del.failed_msgs) == 1, "Ошибка при удалении сообщения в чате с помощью delete_msgs"


@allure.id("2316299")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-mchat")
@allure.title("Положительные сценарии по работе с удалением сообщений в чатах глобально")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_del_global(
    auth_account,
    opponent_account,
    create_chat,
    write_to_chat,
    del_msg_glob,
    ):
    chat_name = "test chat"
    chat_id = Rid(2, create_chat([auth_account.uin], Anketa(name=chat_name)).chatId)

    message_id_first = write_to_chat(
        chat_id=chat_id,
        plain="Корова в бомболюке").messageId

    response_del = del_msg_glob(
        chat_id=chat_id,
        additional_msgs=[message_id_first, message_id_first + 999999])

    assert len(response_del.failed_msgs) == 1, "Ошибка при удалении сообщения в чате с помощью delete_msgs_global"

@allure.id("2316312")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-mchat")
@allure.title("Положительные сценарии по работе с удалением сообщений в чатах up to")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_del_up_to(
    auth_account,
    opponent_account,
    create_chat,
    write_to_chat,
    del_up_to,
    ):
    chat_name = "test chat"
    chat_id = Rid(2, create_chat([auth_account.uin], Anketa(name=chat_name)).chatId)

    message_id_first = write_to_chat(
        chat_id=chat_id,
        plain="Корова в бомболюке").messageId

    del_up_to(
        chat_id=chat_id,
        up_to_msg_id=message_id_first)
