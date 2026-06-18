import pathlib
from time import sleep
import allure
import pytest
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import send_message_rapi, send_message_wim


@allure.id("863155")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("DLP")
@allure.feature("Файлы")
@allure.title(
    "Если ответ по файлу от DLP ещё не получен и нет превышения 2-го порога. Система (Вахтёр) должна не"
    + " давать доступ к файлу (чтение/скачивание) отправителю/получателю."
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
def test_upload_file_with_disconnect_timeout(
    chat_type,
    fetch_until_empty_answer_with_filter,
    dlp_block_text,
    send_func,
    check_file_disconnect_timeout,
    chat_entities,
    check_event_send_message_event_exist,
):
    main_acc, opponent_acc, chats = chat_entities

    chat = chats[chat_type]
    if chat_type == "thread":
        opponent_acc.rapi_group_subscribe(
            chatId=chat,
        )
    file = (
        pathlib.Path("support")
        .joinpath("files")
        .joinpath("dlp")
        .joinpath("fake_file_with_check_file_disconnect_timeout.json")
    )

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

    previews = ("iphone_retina", "xlarge")

    with allure.step("Получатель пытается получить доступ к информации о файле в начальный момент ожидания"):
        response = opponent_acc.files_info(
            file_id=file_id,
            previews=previews,
        )
        files_info_response = response["result"]
    url_of_file = files_info_response["info"]["dlink"]

    with allure.step("Получатель пытается скачать файл в начальный момент ожидания"):
        response = opponent_acc.session.get(url_of_file).json()
        assert response["status"]["code"] == 425, "Неверный статус проверки"

    sleep(check_file_disconnect_timeout)

    with allure.step("Получатель пытается получить доступ к информации о файле в конечный момент ожидания"):
        response = opponent_acc.files_info(
            file_id=file_id,
            previews=previews,
        )
        files_info_response = response["result"]
    url_of_file = files_info_response["info"]["dlink"]

    with allure.step("Получатель пытается скачать файл в конечный момент ожидания"):
        response = opponent_acc.session.get(url_of_file).json()
        assert response["status"]["code"] == 425, "Неверный статус проверки"
