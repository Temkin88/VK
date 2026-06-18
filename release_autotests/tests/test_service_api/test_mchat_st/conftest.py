import allure
import pytest

from pyvkteamsclient.client.base.ipros.mchat_st.base_types import Anketa

@pytest.fixture
def create_chat(ipros_client):
    def fn(members, anketa=None, **kwargs):
        if anketa is None:
            anketa = Anketa(name="test chat")

        with allure.step("Создаем чат"):
            response = ipros_client.mchatst_createChat(anketa, members, **kwargs)
            assert response.status() == 200, "Ошибка создания чата"

            return response

    return fn


@pytest.fixture(scope="session")
def add_members(ipros_client):
    def fn(chat_id, accounts, **kwargs):
        with allure.step("Добавляем участников"):
            response = ipros_client.mchatst_addMembers(chat_id, accounts, **kwargs)
            assert response.status() == 200, "Ошибка добавления участника в чат"

    return fn


@pytest.fixture(scope="session")
def get_rid(ipros_client):
    def fn(uin):
        with allure.step("Получаем рид пользователя"):
            return ipros_client.snst_resolveRid(uin).rid

    return fn


@pytest.fixture(scope="session")
def get_pending_members(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Получаем ожидающих вступления"):
            response = ipros_client.mchatst_getPendingList(chat_id, **kwargs)
            assert response.status() == 200, "Ошибка получения списка ожидающих вступления"

            return response.members

    return fn


@pytest.fixture(scope="session")
def cancel_invitation(ipros_client):
    def fn(chat_id, inviteOwnerId, invitedUserSn, **kwargs):
        with allure.step("Отменяем заявку на вступление"):
            response = ipros_client.mchatst_invitationCancel(chat_id, inviteOwnerId, invitedUserSn, **kwargs)
            assert response.status() == 200, "Ошибка отзыва заявки"

    return fn


@pytest.fixture(scope="session")
def resolve_pending(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Разрешаем заявку на вступление"):
            response = ipros_client.mchatst_resolvePending(chat_id, **kwargs)
            assert response.status() == 200, "Ошибка разрешения заявки на вступление"

    return fn


@pytest.fixture(scope="session")
def join_alpha(ipros_client):
    def fn(chat_id, *args, **kwargs):
        with allure.step("Вступаем в чат по ссылке"):
            response = ipros_client.mchatst_joinAlpha(chat_id, *args, **kwargs)

            return response.status()

    return fn


@pytest.fixture(scope="session")
def get_diff_member_list(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Получаем список участников"):
            response = ipros_client.mchatst_getDiffMemberList(chat_id, **kwargs)
            assert response.status() == 200, "Ошибка получения мемберов чата"

            return response

    return fn


@pytest.fixture(scope="session")
def delete_member(ipros_client):
    def fn(chat_id, members, **kwargs):
        with allure.step("Удаляем участников"):
            response = ipros_client.mchatst_delMembersTagged(chat_id, members, **kwargs)
            assert response.status() == 200, "Ошибка удаления участника из чата"

    return fn


@pytest.fixture(scope="session")
def get_chat_info(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Получаем информацию о чате"):
            response = ipros_client.mchatst_getInfo(chat_id, **kwargs)
            assert response.status() == 200, "Ошибка получения информации о чате"

            return response

    return fn


@pytest.fixture(scope="session")
def get_chat_id_info(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Получаем информацию о чате урезанным методом"):
            response = ipros_client.mchatst_getIdInfo(chat_id, **kwargs)
            assert response.status() == 200, "Ошибка получения информации о чате"

            return response

    return fn


@pytest.fixture(scope="session")
def send_message(ipros_client):
    def fn(chat_id, message, **kwargs):
        with allure.step("Отправляем сообщение в чат"):
            response = ipros_client.mchatst_sendMessage(chat_id, message, **kwargs)
            assert response.status() == 200, "Ошибка отправки сообщения"

            return response

    return fn


@pytest.fixture(scope="session")
def pin_message(ipros_client):
    def fn(chat_id, message_id, **kwargs):
        with allure.step("Пиним сообщение"):
            response = ipros_client.mchatst_pinMessage(chat_id, message_id, **kwargs)
            assert response.status() == 200, "Ошибка пиннинга"

    return fn


@pytest.fixture(scope="session")
def create_thread(ipros_client):
    def fn(chat_id, parent_topic, **kwargs):
        with allure.step("Создаем тред"):
            response = ipros_client.mchatst_createThread(chat_id, parent_topic, **kwargs)
            assert response.status() == 200, "Ошибка создания треда"

            return response

    return fn


@pytest.fixture(scope="session")
def delete_message(ipros_client):
    def fn(chat_id, messages, **kwargs):
        with allure.step("Удаляем сообщение"):
            response = ipros_client.mchatst_delMsgGlob(chat_id, messages, **kwargs)
            assert response.status() == 200, "Ошибка удаления"

    return fn


@pytest.fixture(scope="session")
def trigger_avatar_changed(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Триггерим смену аватарки в чате"):
            response = ipros_client.mchatst_avatarChanged(chat_id)
            assert response.status() == 200, "Ошибка смены аватара"

    return fn


@pytest.fixture(scope="session")
def get_permissions(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Получаем права на чат"):
            response = ipros_client.mchatst_getPermissions(chat_id, **kwargs)
            assert response.status() == 200, "Ошибка получения прав"

            return response

    return fn


@pytest.fixture(scope="session")
def get_permissions_extended(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Получаем права на чат, полноценный метод"):
            response = ipros_client.mchatst_getPermissionsExtended(chat_id, **kwargs)
            assert response.status() == 200, "Ошибка получения прав"

            return response

    return fn


@pytest.fixture(scope="session")
def get_recent_writers(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Получаем последних активных пользователей"):
            response = ipros_client.mchatst_getRecentWriters(chat_id, **kwargs)
            assert response.status() == 200, "Ошибка получения последних активных пользователей"

            return response

    return fn


@pytest.fixture(scope="session")
def modify_member(ipros_client):
    def fn(chat_id, user_uin, **kwargs):
        with allure.step("Обновляем роль участника чата"):
            response = ipros_client.mchatst_modMember(chat_id, user_uin, **kwargs)
            assert response.status() == 200, "Ошибка обновления роли пользователя"

    return fn


@pytest.fixture(scope="session")
def get_members(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Получаем список участников"):
            response = ipros_client.mchatst_getMembers(chat_id, **kwargs)
            assert response.status() == 200, "Ошибка получения участников чата"

            return response.members

    return fn


@pytest.fixture(scope="session")
def get_blocked_list(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Получаем список заблокированных"):
            response = ipros_client.mchatst_getBlockedList(chat_id, **kwargs)
            assert response.status() == 200, "Ошибка получения списка заблокированных"

            return response.blockList

    return fn


@pytest.fixture(scope="session")
def block_members(ipros_client):
    def fn(chat_id, members, **kwargs):
        with allure.step("Блокируем пользователя"):
            response = ipros_client.mchatst_setBlocked(chat_id, members, **kwargs)
            assert response.status() == 200, "Ошибка выставления блокировки"

    return fn


@pytest.fixture(scope="session")
def get_anketa_field(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Получаем анкету чата"):
            response = ipros_client.mchatst_getAnketaField(chat_id, **kwargs)
            assert response.status() == 200, "Ошибка получения анкеты чата"

            return response

    return fn


@pytest.fixture(scope="session")
def modify_anketa(ipros_client):
    def fn(chat_id, anketa, **kwargs):
        with allure.step("Изменяем анкету чата"):
            response = ipros_client.mchatst_modAnketa(chat_id, anketa, **kwargs)
            assert response.status() == 200, "Ошибка обновления анкеты"

    return fn
