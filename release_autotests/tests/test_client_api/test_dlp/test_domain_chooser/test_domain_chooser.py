import pathlib
import allure
import pytest
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import (
    send_message_rapi,
    send_message_wim,
    check_file_availability,
    check_file_unavailability,
)


@allure.id("1067353")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("DLP")
@allure.feature("Сообщения")
@allure.title(
    "Домены настроены на разные адаптеры, проверяем различия в ответах"
    "вахтера на однинаковое действие при отправке сообщений в группу/канал"
)
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@DLP
@pytest.mark.parametrize("send_func", [send_message_rapi, send_message_wim])
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_domain_chooser(chat_type, chat_entities_multidomain, send_func, check_event_send_message_event_exist):
    acc_strategy_on_fail_block_adapter, acc_strategy_on_fail_ok_adapter, acc_debug_mode_true_adapter, chats = (
        chat_entities_multidomain
    )
    """
        Данный тест проверяет работу опции adapter_chooser.
        В проверке учавствует три пользователя с доменами, соотвествующие адаптерам с опциями:
        1. strategy_on_fail: block, default_access_level: Internal
        2. strategy_on_fail: ok, default_access_level: External
        3. debug_mode_enabled: true, default_access_level: External
        Проверка на то что для выбранного домена установлен нужный адаптер производится по трем реакциям
        на отправляемые данные:
        1. Проверка на отправку блокируемого текста: "block"
        2. Проверка на отправку текста приводящего к ошибке dlp системы: "server_error_word"
        3. Проверка на доступ к файлу с уровнем доступа Internal
        Отправка сообщений происходит в группу и канал в которых состоят все три пользователя
    """

    chat = chats[chat_type]
    check_cases = {
        "block": {
            acc_strategy_on_fail_block_adapter: False,
            acc_strategy_on_fail_ok_adapter: False,
            acc_debug_mode_true_adapter: True,
        },
        "server_error_word": {
            acc_strategy_on_fail_block_adapter: False,
            acc_strategy_on_fail_ok_adapter: True,
            acc_debug_mode_true_adapter: True,
        },
    }

    for text, checks in check_cases.items():
        with allure.step(f"Проверяем реакцию на текст: {text}"):
            for acc, check_result in checks.items():
                with allure.step("Отправляем сообщение"):
                    status_code, msg_id = send_func(acc, chat, text)
                assert (msg_id is not None) == check_result, "Ошибка проверки"

    file = (
        pathlib.Path("support")
        .joinpath("files")
        .joinpath("dlp")
        .joinpath("fake_file_without_sensitive_information.json")
    )
    with allure.step("Пытаемся загрузить файл"):
        file = acc_strategy_on_fail_block_adapter.upload_file(file.absolute())

    file_id, file_url = file

    assert file_id is not None, "Идентификатор файла отстуствует"
    assert file_url is not None, "Ссылка на файл отстуствует"

    with allure.step("Отправляем файл получателю"):
        status_code, msg_id = send_func(acc_strategy_on_fail_block_adapter, chat, None, file_url)
    assert msg_id is not None

    reader_acc = acc_strategy_on_fail_ok_adapter
    assert check_event_send_message_event_exist(reader_acc, msg_id=msg_id), "Событие о новом сообщении не найдено"

    reader_acc = acc_debug_mode_true_adapter
    assert check_event_send_message_event_exist(reader_acc, msg_id=msg_id), "Событие о новом сообщении не найдено"

    checks = {
        acc_strategy_on_fail_block_adapter: True,
        acc_strategy_on_fail_ok_adapter: False,
        acc_debug_mode_true_adapter: False,
    }

    for acc, check_result in checks.items():
        if check_result:
            check_file_availability(acc, file_id, is_final=False)
        else:
            check_file_unavailability(acc, file_id, is_final=False)
