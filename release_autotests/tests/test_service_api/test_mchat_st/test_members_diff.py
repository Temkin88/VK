import allure

from support.markers import SANDBOX

@allure.id("2310463")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с чатами с помощью mchat-st")
@allure.title("Положительные сценарии по работе со списком участников в чате")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_chat_members_diff(
    auth_account,
    opponent_account,
    create_chat,
    get_diff_member_list,
    delete_member,
):
    chat_id = create_chat([auth_account.uin, opponent_account.uin]).chatId
    version = get_diff_member_list(chat_id).version
    delete_member(chat_id, [opponent_account.uin])
    get_diff_member_list(chat_id, version=version)
