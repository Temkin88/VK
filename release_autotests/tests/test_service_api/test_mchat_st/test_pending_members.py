import allure

from support.markers import SANDBOX
from pyvkteamsclient.client.base.ipros.mchat_st.base_types import Anketa

@allure.id("2310459")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с чатами с помощью mchat-st")
@allure.title("Подтверждение заявки на вступление в чат")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_pending_members_resolve(
    auth_account,
    opponent_account,
    third_account,
    create_chat,
    add_members,
    get_pending_members,
    resolve_pending,
):
    chat_id = create_chat([auth_account.uin, opponent_account.uin],
                          Anketa(name="test chat", joinModeration=True, public=True)).chatId

    add_members(chat_id, [third_account.uin], requester=opponent_account.uin)
    pending_members = get_pending_members(chat_id)

    assert len(pending_members) == 1, "Должна добавиться одна заявка на вступление"
    assert pending_members[0].screenName == third_account.uin, "Ожидает вступления нужный юзер"

    resolve_pending(chat_id, approveMembers=[third_account.uin])

    pending_members = get_pending_members(chat_id)
    assert len(pending_members) == 0, "Заявка на вступление должна закрыться"


@allure.id("2312578")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с чатами с помощью mchat-st")
@allure.title("Отмена заявки на вступление в чат")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_pending_members_abort(
    auth_account,
    opponent_account,
    third_account,
    create_chat,
    add_members,
    get_rid,
    get_pending_members,
    cancel_invitation,
):
    opponent_id = get_rid(opponent_account.uin)
    chat_id = create_chat([auth_account.uin, opponent_account.uin],
                          Anketa(name="test chat", joinModeration=True, public=True)).chatId

    add_members(chat_id, [third_account.uin], requester=opponent_account.uin)
    pending_members = get_pending_members(chat_id)

    assert len(pending_members) == 1, "Должна добавиться одна заявка на вступление"
    assert pending_members[0].screenName == third_account.uin, "Ожидает вступления нужный юзер"

    cancel_invitation(chat_id, opponent_id, third_account.uin)
    pending_members = get_pending_members(chat_id)
    assert len(pending_members) == 0, "Заявка на вступление должна отмениться"


@allure.id("2312579")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с чатами с помощью mchat-st")
@allure.title("Вступление в чат по стемпу")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_pending_members_by_stamp(
    auth_account,
    opponent_account,
    create_chat,
    get_rid,
    get_pending_members,
    join_alpha,
    resolve_pending,
):
    opponent_id = get_rid(opponent_account.uin)
    chat_info = create_chat([auth_account.uin],
                          Anketa(name="test chat", joinModeration=True, public=True))

    assert join_alpha(chat_info.chatId, chat_info.stamp, opponent_id) == 201, "Ожидается ошибка 'waiting for approval'"

    pending_members = get_pending_members(chat_info.chatId)
    assert len(pending_members) == 1, "Должна добавиться одна заявка на вступление"
    assert pending_members[0].screenName == opponent_account.uin, "Ожидает вступления нужный юзер"

    resolve_pending(chat_info.chatId, approveMembers=[opponent_account.uin])
