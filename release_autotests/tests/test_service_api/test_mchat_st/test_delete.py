import allure

from support.markers import SANDBOX

@allure.id("2310461")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с чатами с помощью mchat-st")
@allure.title("Положительные сценарии удаления участников из чата")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_chat_user_del(
    auth_account,
    opponent_account,
    create_chat,
    delete_member,
    get_members,
):
    chat_id = create_chat([ auth_account.uin, opponent_account.uin ]).chatId

    members = get_members(chat_id)
    assert len(members) == 2, "В чате 2 участника"

    delete_member(chat_id, [opponent_account.uin])

    members = get_members(chat_id)
    assert len(members) == 1, "Изменилось число участников"
    assert members[0].screenName == auth_account.uin, "Удален нужный пользователь"
