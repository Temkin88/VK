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
def write_to_chat(ipros_client):
    def fn(chat_id, plain: str, **kwargs):
        with allure.step("Отправка сообщения в чат"):
            response = ipros_client.gbld_mchat_store(
                chat_id=chat_id,
                plain=plain,
                **kwargs)
            assert response.status() == 200, "Ошибка отправки сообщения в чат"
            return response

    return fn

@pytest.fixture(scope="session")
def select(ipros_client):
    def fn(chat_id, select_params, slip, message_id, **kwargs):
        with allure.step("Получаем историю чата"):
            response = ipros_client.gbld_mchat_select(
                chat_id=chat_id,
                message_id=message_id,
                select_params=select_params,
                slip=slip,
                **kwargs)
            assert response.status() == 200, "Ошибка получения истории чата"
            return response

    return fn

@pytest.fixture(scope="session")
def select_batch(ipros_client):
    def fn(chat_id, select_batch_params, **kwargs):
        with allure.step("Получаем историю чата батчевым запросом"):
            response = ipros_client.gbld_mchat_select_batch(
                chat_id=chat_id,
                select_batch_params=select_batch_params,
                **kwargs)
            assert response.status() == 200, "Ошибка получения истории чата батчевым запросом"
            return response

    return fn

@pytest.fixture(scope="session")
def add_thread(ipros_client):
    def fn(chat_id, sender_sn, message_id, default_role, **kwargs):
        with allure.step("Добавляем тред в чат"):
            response = ipros_client.gbld_mchat_add_thread(
                chat_id=chat_id,
                sender_sn=sender_sn,
                message_id=message_id,
                default_role=default_role,
                **kwargs)
            assert response.status() == 200, "Ошибка добавления треда в чат"
            return response

    return fn

@pytest.fixture(scope="session")
def get_all_threads(ipros_client):
    def fn(chat_id, **kwargs):
        with allure.step("Получаем все треды чата"):
            response = ipros_client.gbld_mchat_get_all_threads(
                chat_id=chat_id,
                **kwargs)
            assert response.status() == 200, "Ошибка получения всех тредов чата"
            return response

    return fn

@pytest.fixture(scope="session")
def set_dlg_state(ipros_client):
    def fn(chat_id, delivered_message_id, read_message_id, **kwargs):
        with allure.step("Выставляем state чата"):
            response = ipros_client.gbld_mchat_set_dlg_state(
                chat_id=chat_id,
                delivered_message_id=delivered_message_id,
                read_message_id=read_message_id,
                **kwargs)
            assert response.status() == 200, "Ошибка выставления state чата"

    return fn

@pytest.fixture(scope="session")
def set_dlg_state_wim(ipros_client):
    def fn(chat_id, delivered_message_id, read_message_id, **kwargs):
        with allure.step("Выставляем state чата wim (плюс два параметра - непонятного назначения)"):
            response = ipros_client.gbld_mchat_set_dlg_state_wim(
                chat_id=chat_id,
                delivered_message_id = delivered_message_id,
                read_message_id = read_message_id,
                **kwargs)
            assert response.status() == 200, "Ошибка выставления state чата wim version"

    return fn

@pytest.fixture(scope="session")
def get_state_chat(ipros_client):
    def fn(thread_id, sender_sn, **kwargs):
        with allure.step("Получаем state чата (только для тредов)"):
            response = ipros_client.gbld_mchat_get_dlg_state(
                chat_id=thread_id,
                sender_sn=sender_sn,
                **kwargs)
            assert response.status() == 200, "Ошибка получения state чата (только для тредов)"
            return response

    return fn

@pytest.fixture(scope="session")
def set_reaction_id(ipros_client):
    def fn(chat_id, message_id, reaction_id, **kwargs):
        with allure.step("Устанавливаем реакцию на сообщение в чате"):
            response = ipros_client.gbld_mchat_set_reaction_id(
                chat_id=chat_id,
                message_id=message_id,
                reaction_id=reaction_id,
                **kwargs)
            assert response.status() == 200, "Ошибка установки реакции на сообщение в чате"

    return fn

@pytest.fixture(scope="session")
def go_suggest_mailing(ipros_client):
    def fn(chat_id, suggest_params, **kwargs):
        with allure.step("Получаем саджест в чате"):
            response = ipros_client.gbld_mchat_go_suggest_mailing(
                chat_id=chat_id,
                suggest_params=suggest_params,
                **kwargs)
            assert response.status() == 200, "Ошибка получения саджеста в чате"
            return response

    return fn

@pytest.fixture(scope="session")
def del_msg(ipros_client):
    def fn(chat_id, additional_msgs, **kwargs):
        with allure.step("Удаляем cообщение в чате"):
            response = ipros_client.gbld_mchat_del_msg(
                chat_id=chat_id,
                additional_msgs=additional_msgs,
                **kwargs
            )
            assert response.status() == 200, "Ошибка удаления сообщения"
            return response

    return fn

@pytest.fixture(scope="session")
def del_up_to(ipros_client):
    def fn(chat_id, up_to_msg_id, **kwargs):
        with allure.step("Удаляем все сообщения до указанного в чате"):
            response = ipros_client.gbld_mchat_del_up_to(
                chat_id=chat_id,
                message_id=up_to_msg_id,
                **kwargs
            )
            assert response.status() == 200, "Ошибка удаления сообщения до указанного"
            return response

    return fn

@pytest.fixture(scope="session")
def del_msg_glob(ipros_client):
    def fn(chat_id, additional_msgs, **kwargs):
        with allure.step("Глобально удаляем два сообщения в чате"):
            response = ipros_client.gbld_mchat_del_msg_glob(
                chat_id=chat_id,
                additional_msgs=additional_msgs,
                **kwargs
            )
            assert response.status() == 200, "Ошибка глобального удаления сообщения"
            return response

    return fn

@pytest.fixture(scope="session")
def susbcribe_to_chat(ipros_client):
    def fn(chat_id, aimsid_pref, sender_sn, is_bot=False, **kwargs):
        with allure.step("Подписываемся на группу"):
            response = ipros_client.gbld_mchat_subscribe_to_group(
                chat_id=chat_id,
                aimsid_pref= aimsid_pref,
                is_bot=is_bot,
                sender_sn=sender_sn,
                **kwargs
            )
            assert response.status() == 200, "Ошибка при подписке на группу"

    return fn

@pytest.fixture(scope="session")
def gallery_notify(ipros_client):
    def fn(chat_id, json_data, **kwargs):
        with allure.step("Gallery Notify"):
            response = ipros_client.gbld_mchat_gallery_notify(
                chat_id=chat_id,
                json_data=json_data
            )
            assert response.status() == 200, "Ошибка при Gallery Notify"

    return fn
