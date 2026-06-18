import pathlib
import allure
import pytest
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import send_message_rapi, send_message_wim, check_file_availability


@allure.id("900262")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("DLP")
@allure.feature("Файлы")
@allure.title(
    "Логин пользователя добавлен в исключение в adapter_manager. Отправка файлов в личку/группу/канал/избранное"
)
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@DLP
@pytest.mark.parametrize(
    "file_to_send", ["fake_file_without_sensitive_information.json", "fake_file_with_sensitive_information.json"]
)
@pytest.mark.parametrize("send_func", [send_message_rapi, send_message_wim])
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "favorites", "thread"])
def test_send_file_by_excluded_user_in_adapter_manager(
    chat_type,
    fetch_until_empty_answer_with_filter,
    send_func,
    chat_entities_with_excluded_user,
    check_event_send_message_event_exist,
    file_to_send,
):
    main_acc, opponent_acc, chats = chat_entities_with_excluded_user
    chat = chats[chat_type]
    if chat_type == "thread":
        opponent_acc.rapi_group_subscribe(
            chatId=chat,
        )
    file = pathlib.Path("support").joinpath("files").joinpath("dlp").joinpath(file_to_send)

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
        "Пользователь, добавленный в исключения,": main_acc,
    }
    if chat_type != "favorites":
        accounts["Получатель"] = opponent_acc
    for friendly_name, acc in accounts.items():
        with allure.step(f"{friendly_name} пытается получить доступ к файлу"):
            assert check_file_availability(acc, file_id)
