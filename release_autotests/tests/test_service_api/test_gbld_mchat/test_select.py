import allure

from support.markers import SANDBOX

from pyvkteamsclient.client.base.ipros.mchat_st.base_types import Anketa

from pyvkteamsclient.client.base.ipros.common.rid import Rid

@allure.id("2316301")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-mchat")
@allure.title("Положительные сценарии по работе с select в чатах")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_select(
    auth_account,
    opponent_account,
    create_chat,
    write_to_chat,
    select
    ):
    chat_name = "test chat"
    chat_id = Rid(2, create_chat([auth_account.uin], Anketa(name=chat_name)).chatId)

    store_response = write_to_chat(
        chat_id=chat_id,
        plain="Корова в бомболюке")

    write_to_chat(chat_id=chat_id, plain="Корова в бомболюке 2")

    select_response = select(
        chat_id=chat_id,
        slip = 10,
        message_id=store_response.messageId,
        select_params = {
            "after": store_response.messageId,
            "slip": 10
            })
    assert len(select_response.plain_messages) == 1, (
        "Ошибка при получении написанного сообщения в чате с помощью select")

@allure.id("2316319")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-mchat")
@allure.title("Положительные сценарии по работе с select в чатах batch")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_select_batch(
    auth_account,
    opponent_account,
    create_chat,
    write_to_chat,
    select_batch
    ):
    chat_name = "test chat"
    chat_id = Rid(2, create_chat([auth_account.uin], Anketa(name=chat_name)).chatId)

    message_id_first = write_to_chat(
        chat_id=chat_id,
        plain="Корова в бомболюке").messageId

    write_to_chat(
        chat_id=chat_id,
        plain="Корова в бомболюке 1")

    message_id_third = write_to_chat(
        chat_id=chat_id,
        plain="Корова в бомболюке 2").messageId

    select_batch_response = select_batch(
        chat_id=chat_id,
        select_batch_params = {
            "show_heads": True,
            "sub_req_params": [{"after": message_id_first, "slip": 10},{"until":message_id_third, "slip": 12}]
            })
    assert len(select_batch_response.result["sub_req"]) > 0, (
        "Ошибка при получении написанного сообщения в чате с помощью select batch")
