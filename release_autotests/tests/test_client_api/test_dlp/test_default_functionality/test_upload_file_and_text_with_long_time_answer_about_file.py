import pathlib
from time import sleep
import allure
import pytest
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import send_message_rapi, send_message_wim, check_file_availability


@allure.id("862870")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("DLP")
@allure.feature("Файлы")
@allure.title("Нарушение DLP нет и нет ответа по файлу. Отправка сообщений в личку/группу/канал/избранное")
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
def test_upload_file_and_text_with_long_time_answer_about_file(
    chat_type,
    fetch_until_empty_answer_with_filter,
    dlp_noblock_text,
    send_func,
    chat_entities,
    check_event_send_message_event_exist,
):
    main_acc, opponent_acc, chats = chat_entities

    chat = chats[chat_type]
    if chat_type == "thread":
        opponent_acc.rapi_group_subscribe(
            chatId=chat,
        )
    text = dlp_noblock_text

    file = (
        pathlib.Path("support")
        .joinpath("files")
        .joinpath("dlp")
        .joinpath("fake_file_without_sensitive_information_with_long_time_answer.json")
    )

    with allure.step("Пытаемся загрузить файл"):
        file = main_acc.upload_file(file.absolute())

    file_id, file_url = file

    assert file_id is not None, "Идентификатор файла отстуствует"
    assert file_url is not None, "Ссылка на файл отстуствует"

    with allure.step("Отправляем файл получателю"):
        status_code, msg_id = send_func(main_acc, chat, text, file_url)

    assert msg_id is not None, "Идентификатор сообщения отстуствует"

    reader_acc = opponent_acc
    if chat_type == "favorites":
        reader_acc = main_acc

    assert check_event_send_message_event_exist(reader_acc, msg_id=msg_id), "Событие о новом сообщении не найдено"

    previews = ("iphone_retina", "xlarge")
    accounts = {
        "Первая сессия отправителя": main_acc,
    }
    if chat_type != "favorites":
        accounts["Сессия получателя"] = opponent_acc

    for friendly_name, acc in accounts.items():
        msg_finded_key = False
        with allure.step(f"{friendly_name} пытается прочитать текст сообщения до завершения проверки"):
            if chat_type == "private" and acc == opponent_acc:
                chat = main_acc.uin
            history = acc.rapi_getHistory(sn=chat)

            for msg in history["results"]["messages"]:
                msg_id_from_history = msg["msgId"]
                msg_texts_from_history = [
                    part["captionedContent"]["caption"] for part in msg["parts"] if "captionedContent" in part
                ]

                if msg_id_from_history == str(msg_id) and text in msg_texts_from_history:
                    msg_finded_key = True
                    break

            assert msg_finded_key, "Текст сообщения не доступен"

        with allure.step(f"{friendly_name} пытается получить доступ к информации о файле"):
            response = acc.files_info(
                file_id=file_id,
                previews=previews,
            )

            files_info_response = response["result"]

        url_of_file = files_info_response["info"]["dlink"]

        with allure.step(f"{friendly_name} пытается скачать файл до прохождения проверки"):
            response = acc.session.get(url_of_file).json()
            assert response["status"]["code"] == 425, "Неверный статус проверки"

    sleep(2)  # Ждем пока проверка завершится
    for friendly_name, acc in accounts.items():
        with allure.step(f"{friendly_name} пытается получить доступ к файлу"):
            assert check_file_availability(acc, file_id)
