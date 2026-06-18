import logging
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

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


@allure.id("912655")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Файлы")
@allure.title("Загрузка файла c запрещенным расширением. Отправка файла в личку/группу/канал/избранное.")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@DLP
@pytest.mark.parametrize("file_name", ["banned_file.jpeg", "png_file_111kB.png", "png_file_670kB.png", "file_1MB.bmp"])
@pytest.mark.parametrize("send_func", [send_message_rapi, send_message_wim])
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "favorites", "thread"])
def test_file_attributes_ban(
    get_limit_for_current_file,
    file_name,
    chat_type,
    fetch_until_empty_answer_with_filter,
    send_func,
    chat_entities,
    main_acc_second_instance,
    check_event_send_message_event_exist,
):
    main_acc, opponent_acc, chats = chat_entities
    chat = chats[chat_type]
    if chat_type == "thread":
        opponent_acc.rapi_group_subscribe(
            chatId=chat,
        )
    file = pathlib.Path("support").joinpath("files").joinpath("dlp").joinpath(file_name)
    with allure.step("Считываем лимиты на файлы данного типа из конфига"):
        file_size_limit = get_limit_for_current_file(file)

    if file_size_limit < 0:
        pytest.skip("Unchecked file extension")

    with allure.step("Проверяем размер тестового файла"):
        actual_file_size = file.stat().st_size

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
            if actual_file_size <= file_size_limit:
                check_file_availability(acc, file_id)
            else:
                check_file_unavailability(acc, file_id)
