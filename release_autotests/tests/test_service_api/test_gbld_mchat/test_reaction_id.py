import allure

from support.markers import SANDBOX

from pyvkteamsclient.client.base.ipros.mchat_st.base_types import Anketa

from pyvkteamsclient.client.base.ipros.common.rid import Rid

import uuid

@allure.id("2316300")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-mchat")
@allure.title("Положительные сценарии по работе с реакциями в чатах")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_reaction_id(
    auth_account,
    opponent_account,
    create_chat,
    write_to_chat,
    set_reaction_id,
    ):
    chat_name = "test chat"
    chat_id = Rid(2, create_chat([auth_account.uin], Anketa(name=chat_name)).chatId)

    message_id_first = write_to_chat(
        chat_id=chat_id,
        plain="Корова в бомболюке").messageId

    set_reaction_id(
        chat_id=chat_id,
        message_id=message_id_first,
        reaction_id=str(uuid.uuid4())
        )

