import allure

from support.markers import SANDBOX

from pyvkteamsclient.client.base.ipros.mchat_st.base_types import Anketa

@allure.id("2310460")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с чатами с помощью mchat-st")
@allure.title("Положительные сценарии по работе с анкетой чата")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_anketa(
    auth_account,
    create_chat,
    get_anketa_field,
    modify_anketa,
):
    chat_name = "test chat"
    chat_id = create_chat([auth_account.uin], Anketa(name=chat_name)).chatId

    anketa = get_anketa_field(chat_id)
    assert anketa.name == chat_name, "Получили верное название чата"

    chat_name = "new chat name"
    modify_anketa(chat_id, Anketa(name=chat_name))

    anketa = get_anketa_field(chat_id)
    assert anketa.name == chat_name, "Название чата изменилось"
