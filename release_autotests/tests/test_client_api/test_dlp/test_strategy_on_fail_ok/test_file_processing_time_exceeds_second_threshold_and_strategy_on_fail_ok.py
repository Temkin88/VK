import pathlib

import allure
import pytest
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import send_message_rapi, send_message_wim, check_file_availability


@allure.id("870335")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Файлы")
@allure.title(
    "В состоянии ожидания ответа от DLP, при превышении 2-го порога недоступности"
    " и в конфиге настроен strategy_on_fail: ok, система (Вахтёр) должна разрешить"
    " отправку файла в личку/группу/канал/избранное."
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
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "favorites", "thread"])
def test_file_processing_time_exceeds_second_threshold_and_strategy_on_fail_ok(
    chat_type,
    fetch_until_empty_answer_with_filter,
    send_func,
    check_event_send_message_event_exist,
    chat_entities,
    main_acc_second_instance,
):
    main_acc, opponent_acc, chats = chat_entities

    chat = chats[chat_type]
    if chat_type == "thread":
        opponent_acc.rapi_group_subscribe(
            chatId=chat,
        )
    file = pathlib.Path("support").joinpath("files").joinpath("dlp").joinpath("fake_file_disconect_action.json")

    with allure.step("Пытаемся загрузить файл"):
        file = main_acc.upload_file(file.absolute())

    file_id, file_url = file

    assert file_id is not None, "Идентификатор файла отстуствует"
    assert file_url is not None, "Ссылка на файл отстуствует"

    with allure.step("Отправляем файл получателю"):
        status_code, msg_id = send_func(main_acc, chat, None, file_url)

    assert msg_id is not None, "Идентификатор сообщения отстуствует"

    reader_acc = opponent_acc
    if chat_type == "favorites":
        reader_acc = main_acc

    assert check_event_send_message_event_exist(reader_acc, msg_id=msg_id), "Событие о новом сообщении не найдено"

    accounts = {
        "Cессия отправителя": main_acc,
        "Вторая сессия отправителя": main_acc_second_instance,
    }
    if chat_type != "favorites":
        accounts["Сессия получателя"] = opponent_acc

    for friendly_name, acc in accounts.items():
        with allure.step(f"{friendly_name} пытается получить доступ к файлу"):
            assert check_file_availability(acc, file_id)
