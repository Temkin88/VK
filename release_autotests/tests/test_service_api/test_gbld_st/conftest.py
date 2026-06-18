import allure
import pytest

@pytest.fixture
def write_to_dlg(ipros_client):
    def fn(sender_sn, opponent_sn, message_body: dict, store_params: dict, **kwargs):
        with allure.step("Отправка сообщения в диалог"):
            response = ipros_client.gbld_st_store(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                store_params=store_params,
                message_body=message_body,
                **kwargs)
            assert response.status() == 200, "Ошибка отправки сообщения в диалог"
            return response

    return fn

@pytest.fixture(scope="session")
def set_dlg_state(ipros_client):
    def fn(sender_sn, opponent_sn, set_dlg_state_params, **kwargs):
        with allure.step("Выставляем state диалога"):
            response = ipros_client.gbld_st_set_dlg_state(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                set_dlg_state_params=set_dlg_state_params,
                **kwargs)
            assert response.status() == 200, "Ошибка выставления state диалога"

    return fn

@pytest.fixture(scope="session")
def set_dlg_state_wim(ipros_client):
    def fn(sender_sn, opponent_sn, set_dlg_state_params, **kwargs):
        with allure.step("Выставляем state диалога wim (плюс два параметра - непонятного назначения)"):
            response = ipros_client.gbld_st_set_dlg_state_wim(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                set_dlg_state_params=set_dlg_state_params,
                **kwargs)
            assert response.status() == 200, "Ошибка выставления state диалога wim version"

    return fn

@pytest.fixture(scope="session")
def select(ipros_client):
    def fn(sender_sn, opponent_sn, select_params, **kwargs):
        with allure.step("Получаем историю диалога"):
            response = ipros_client.gbld_st_select(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                select_params=select_params,
                **kwargs)
            assert response.status() == 200, "Ошибка получения истории диалога"
            return response

    return fn

@pytest.fixture(scope="session")
def select_batch(ipros_client):
    def fn(sender_sn, opponent_sn, select_batch_params, **kwargs):
        with allure.step("Получаем историю диалога - batch"):
            response = ipros_client.gbld_st_select_batch(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                select_batch_params=select_batch_params,
                **kwargs)
            assert response.status() == 200, "Ошибка получения истории диалога - batch"
            return response

    return fn

@pytest.fixture(scope="session")
def pin_msg(ipros_client):
    def fn(sender_sn, opponent_sn, msg_ids, **kwargs):
        with allure.step("Закрепляем/открепляем сообщение в диалоге"):
            response = ipros_client.gbld_st_pin_msg(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                msg_ids=msg_ids,
                **kwargs)
            assert response.status() == 200, "Ошибка закрепления/открепления сообщения в диалоге"

    return fn

@pytest.fixture(scope="session")
def del_msg(ipros_client):
    def fn(sender_sn, opponent_sn, additional_msgs, **kwargs):
        with allure.step("Удаляем сообщения в диалоге"):
            response = ipros_client.gbld_st_del_msg(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                additional_msgs=additional_msgs,
                **kwargs)
            assert response.status() == 200, "Ошибка удаления сообщения"
            return response

    return fn

@pytest.fixture(scope="session")
def del_msg_glob(ipros_client):
    def fn(sender_sn, opponent_sn, additional_msgs, **kwargs):
        with allure.step("Удаляем сообщения в диалоге - глобально"):
            response = ipros_client.gbld_st_del_msg_glob(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                additional_msgs=additional_msgs,
                **kwargs)
            assert response.status() == 200, "Ошибка удаления сообщения - глобально"
            return response

    return fn

@pytest.fixture(scope="session")
def del_msg_up_to(ipros_client):
    def fn(sender_sn, opponent_sn, message_id, **kwargs):
        with allure.step("Удаляем сообщение в диалоге - up_to"):
            response = ipros_client.gbld_st_del(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                message_id=message_id,
                **kwargs)
            assert response.status() == 200, "Ошибка удаления сообщения - up_to"
            return response

    return fn

@pytest.fixture(scope="session")
def get_history_snapshot(ipros_client):
    def fn(sender_sn, opponent_sn, **kwargs):
        with allure.step("Получение снепшота истории диалога"):
            response = ipros_client.gbld_st_get_history_snapshot(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                **kwargs)
            assert response.status() == 200, "Ошибка при получении снепшота диалога"
            return response

    return fn

@pytest.fixture(scope="session")
def set_reaction_id(ipros_client):
    def fn(sender_sn, opponent_sn, message_id, reaction_id, **kwargs):
        with allure.step("Выставляем реакцию"):
            response = ipros_client.gbld_st_set_reaction_id(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                message_id=message_id,
                reaction_id=reaction_id,
                **kwargs)
            assert response.status() == 200, "Ошибка выставления реакции"

    return fn

@pytest.fixture(scope="session")
def can_disturb_vip(ipros_client):
    def fn(sender_sn, opponent_sn, vip_sn, **kwargs):
        with allure.step("Проверяем Can disturb VIP"):
            response = ipros_client.gbld_st_can_disturb_vip(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                vip_sn=vip_sn,
                **kwargs)
            assert response.status() == 200, "Ошибка при получении Can disturb VIP"
            return response

    return fn

@pytest.fixture(scope="session")
def is_dlg_empty(ipros_client):
    def fn(sender_sn, opponent_sn, **kwargs):
        with allure.step("Получаем пустой ли диалог"):
            response = ipros_client.gbld_st_is_dlg_empty(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                **kwargs)
            assert response.status() == 200, "Ошибка при получении пустой ли диалог"
            return response

    return fn

@pytest.fixture(scope="session")
def is_stranger(ipros_client):
    def fn(sender_sn, opponent_sn, **kwargs):
        with allure.step("Получаем является ли незнакомцем"):
            response = ipros_client.gbld_st_is_stranger(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                **kwargs)
            assert response.status() == 200, "Ошибка при получении является ли незнакомцем"
            return response

    return fn

@pytest.fixture(scope="session")
def get_stranger_status(ipros_client):
    def fn(sender_sn, opponent_sn, from_sn, to_sn, **kwargs):
        with allure.step("Получаем статус незнакомца"):
            response = ipros_client.gbld_st_get_stranger_status(
                side_a_sn=sender_sn,
                side_b_sn=opponent_sn,
                from_sn=from_sn,
                to_sn=to_sn,
                **kwargs)
            assert response.status() == 200, "Ошибка при получении статуса незнакомца"
            return response

    return fn
