import pathlib
from time import sleep
from typing import Union
from pyvkteamsclient.client import DesktopClient
import allure


def send_message_rapi(account: DesktopClient, chat_id, text=None, url=None) -> tuple[int, int]:
    if text is not None and url is not None:
        response = account.rapi_message_send(
            target=chat_id,
            parts={"mainPart": {"captionedContent": {"caption": {"plain": text}, "url": url}}},
        )
    elif text is None:
        response = account.rapi_message_send(
            target=chat_id,
            parts={"mainPart": {"text": {"plain": url}}},
        )
    elif url is None:
        response = account.rapi_message_send(
            target=chat_id,
            parts={"mainPart": {"text": {"plain": text}}},
        )
    try:
        msg_id = response["results"]["msgId"]
    except KeyError:
        msg_id = None
    response_status_code = response["status"]["code"]
    return response_status_code, msg_id


def send_message_wim(account: DesktopClient, chat_id, text=None, url=None) -> tuple[int, int]:
    response_codes = {
        603: 40607,
        200: 20000,
    }
    if text is not None and url is not None:
        response = account.wim_im_sendIM(
            t=chat_id,
            parts=[
                {"mediaType": "text", "text": "Медиа с подписью", "captionedContent": {"caption": text, "url": url}}
            ],
        )
    elif text is None:
        response = account.wim_im_sendIM(
            t=chat_id,
            parts=[{"mediaType": "text", "text": url}],
        )
    elif url is None:
        response = account.wim_im_sendIM(
            t=chat_id,
            parts=[{"mediaType": "text", "text": text}],
        )
    try:
        msg_id = response["response"]["data"]["histMsgId"]
    except KeyError:
        msg_id = None
    response_status_code = response["response"]["statusCode"]
    response_status_code = response_codes.get(response_status_code, response_status_code)
    return response_status_code, msg_id


def create_chats(
    main_acc,
    opponent_acc: Union[DesktopClient, list[DesktopClient]],
):
    result = {}
    if not isinstance(opponent_acc, list):
        result["private"] = opponent_acc.uin
        opponent_acc = [opponent_acc]
    result["favorites"] = main_acc.uin
    result["group"] = main_acc.create_chat(
        "Test group",
        members=opponent_acc,
    )
    result["channel"] = main_acc.create_chat(
        "Test channel",
        defaultRole="readonly",
        members=opponent_acc,
    )

    response = main_acc.rapi_message_send(
        target=result["group"],
        parts={"mainPart": {"text": {"plain": "Message_with_thread"}}},
    )
    response = main_acc.rapi_thread_add(
        chatId=result["group"],
        messageId=response["results"]["msgId"],
    )
    result["thread"] = response["results"]["threadId"]

    return result


def check_file_unavailability(acc: DesktopClient, file_id: str, is_final=True) -> bool:
    previews = ["iphone_retina", "xlarge"]
    try_limit = 6 if is_final else 2
    try_counter = 0
    while try_counter < try_limit:
        response = acc.files_info(
            file_id=file_id,
            previews=previews,
        )
        if type(response) is not dict:
            status_code = response.json()["status"]["code"]
            assert status_code == 40401, "Неверный код ответа"
            return True
        response = acc.session.get(response["result"]["info"]["dlink"])
        status_code = response.status_code
        if status_code == 404:
            return True
        assert status_code == 425, "Неверный код ответа"
        sleep(try_counter**2 + 1)
        try_counter += 1
    if is_final:
        raise Exception("Превышен лимит попыток проверки доступности файла")
    else:
        return True


def check_file_availability(acc: DesktopClient, file_id: str, is_final=True):
    previews = ["iphone_retina", "xlarge"]
    try_limit = 6 if is_final else 2
    try_counter = 0
    while try_counter < try_limit:
        response = acc.files_info(
            file_id=file_id,
            previews=previews,
        )
        if type(response) is not dict:
            raise Exception(f"Неверная схема ожидаемого ответа {response.json()}")

        status_code = response["status"]["code"]
        assert status_code == 20000, "Неверный код ответа"
        response = acc.session.get(response["result"]["info"]["dlink"])
        status_code = response.status_code
        if status_code == 200:
            return True
        assert status_code == 425, "Неверный код ответа"
        sleep(try_counter**2 + 1)
        try_counter += 1
    if is_final:
        raise Exception("Превышен лимит попыток проверки доступности файла")
    else:
        return True


def dehumanize_file_size(filesize: str) -> int:
    dimensions = {"kib": 1, "mib": 2, "gib": 3, "tib": 4, "pib": 5, "eib": 6}
    size = filesize
    size = size.replace(" ", "").lower()
    multiplier = 1
    for key in dimensions:
        if key == "b":
            break
        elif key in size:
            size = size.replace(key, "")
            multiplier = 1024 ** dimensions[key]
            break
        elif key.replace("i", "") in size:
            size = size.replace(key.replace("i", ""), "")
            multiplier = 1024 ** dimensions[key]
            break
    return int(size) * multiplier


def upload_file_with_sensitive_data_to_block_by_fake_dlp(
    chat_type,
    send_func,
    chat_entities,
    check_event_send_message_event_exist,
    main_acc_second_instance=None,
):
    main_acc, opponent_acc, chats = chat_entities

    chat = chats[chat_type]
    if chat_type == "thread":
        opponent_acc.rapi_group_subscribe(
            chatId=chat,
        )
    file = (
        pathlib.Path("support").joinpath("files").joinpath("dlp").joinpath("fake_file_with_sensitive_information.json")
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
    accounts = {
        "Первая сессия отправителя": main_acc,
        "Вторая сессия отправителя": main_acc_second_instance,
        "Сессия получателя": opponent_acc,
    }
    for friendly_name, acc in accounts.items():
        if acc is None:
            continue
        with allure.step(f"{friendly_name} пытается получить доступ к файлу"):
            assert check_file_unavailability(acc, file_id)
