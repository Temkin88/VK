import allure

from support.markers import SANDBOX

@allure.id("2310462")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с чатами с помощью mchat-st")
@allure.title("Положительные сценарии по работе с заблокированными участниками чата")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_chat_user_block(
    auth_account,
    opponent_account,
    create_chat,
    get_blocked_list,
    block_members,
):
    chat_id = create_chat([auth_account.uin, opponent_account.uin]).chatId

    assert len(get_blocked_list(chat_id)) == 0, "Заблокированных нет"

    block_members(chat_id, [opponent_account.uin])

    members = get_blocked_list(chat_id)
    assert len(members) == 1, "Найден заблокированный пользователь"
    assert members[0].sn == opponent_account.uin, "Заблокирован нужный юзер"
