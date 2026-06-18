import pathlib
import allure
import pytest
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import send_message_rapi, send_message_wim, check_file_availability


@allure.id("872485")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("DLP")
@allure.feature("Файлы")
@allure.title(
    "Если ответ по файлу от DLP - разрешить + КСПД сессии Internal. ,"
    " файл External. Система (Вахтёр) должна открыть доступ к файлу (чтение/скачивание)"
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
def test_internal_session_external_file(
    chat_entities_with_internal_accounts,
    first_account_with_second_internal_session,
    send_func,
    chat_type,
    check_event_send_message_event_exist,
):
    internal_main_acc, internal_opponent_acc, chats = chat_entities_with_internal_accounts
    chat = chats[chat_type]

    if chat_type == "thread":
        internal_opponent_acc.rapi_group_subscribe(
            chatId=chat,
        )
    file = (
        pathlib.Path("support")
        .joinpath("files")
        .joinpath("dlp")
        .joinpath("fake_file_without_sensitive_information.json")
    )

    with allure.step("Пытаемся загрузить файл"):
        file = internal_main_acc.upload_file(file.absolute())

    file_id, file_url = file

    assert file_id is not None, "Идентификатор файла отстуствует"
    assert file_url is not None, "Ссылка на файл отстуствует"

    with allure.step("Отправляем файл получателю"):
        status_code, msg_id = send_func(internal_main_acc, chat, None, file_url)

    assert msg_id is not None
    reader_acc = internal_opponent_acc
    if chat_type == "favorites":
        reader_acc = internal_main_acc

    assert check_event_send_message_event_exist(reader_acc, msg_id=msg_id), "Событие о новом сообщении не найдено"

    accounts = {
        "Отправитель в internal сессии": internal_main_acc,
        "Отправитель во второй internal сессии": first_account_with_second_internal_session,
    }
    if chat_type != "favorites":
        accounts["Получатель в internal сессии"] = internal_opponent_acc

    for friendly_name, acc in accounts.items():
        with allure.step(f"{friendly_name} пытается получить доступ к файлу"):
            assert check_file_availability(acc, file_id)
