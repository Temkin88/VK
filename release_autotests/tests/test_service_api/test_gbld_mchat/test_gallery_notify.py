import allure

from support.markers import SANDBOX

from pyvkteamsclient.client.base.ipros.mchat_st.base_types import Anketa

from pyvkteamsclient.client.base.ipros.common.rid import Rid


@allure.id("2316297")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-mchat")
@allure.title("Положительные сценарии по работе с уведомлениями из галереи в чатах")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_gallery_notify(
    auth_account,
    opponent_account,
    create_chat,
    gallery_notify
    ):
    chat_name = "test chat"
    chat_id = Rid(2, create_chat([auth_account.uin], Anketa(name=chat_name)).chatId)

    gallery_notify(
        chat_id=chat_id,
        json_data="{}"
    )

