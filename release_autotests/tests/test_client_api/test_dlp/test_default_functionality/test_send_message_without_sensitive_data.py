import allure
import pytest

from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import send_message_rapi, send_message_wim


@allure.id("557298")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Сообщения")
@allure.title("Отправка сообщения без чувствительных данных")
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
def test_send_message_without_sensitive_data(
    send_func, chat_type, check_event_send_message_event_exist, chat_entities, dlp_noblock_text
):
    """
    Проверка отправки текстового сообщения
    """

    main_acc, opponent_acc, chats = chat_entities
    chat = chats[chat_type]

    if chat_type == "thread":
        opponent_acc.rapi_group_subscribe(
            chatId=chat,
        )

    text = dlp_noblock_text

    with allure.step("Отправляем сообщение получателю"):
        status_code, msg_id = send_func(main_acc, chat, text)

    with allure.step("Проверяем что ID сообщения не вернулось и получен статус код блокировки"):
        assert msg_id is not None, "Идентификатор сообщения присутствует"
        assert status_code == 20000, "Сообщение не заблокировано"
    reader_acc = opponent_acc
    if chat_type == "favorites":
        reader_acc = main_acc

    with allure.step("Проверяем что событие с текстом сообшения к оппоненту пришло"):
        assert check_event_send_message_event_exist(reader_acc, msg_text=text, msg_id=msg_id), (
            "Событие о новом сообщении не найдено"
        )

    accounts = {
        "Отправитель": main_acc,
    }
    if chat_type != "favorites":
        accounts["Получатель"] = opponent_acc

    for friendly_name, acc in accounts.items():
        msg_finded_key = False
        with allure.step(f"{friendly_name} пытается прочитать текст сообщения"):
            if chat_type == "private" and acc == opponent_acc:
                chat = main_acc.uin
            history = acc.rapi_getHistory(sn=chat)
            for msg in history["results"]["messages"]:
                msg_id_from_history = msg["msgId"]
                msg_texts_from_history = [part["text"] for part in msg["parts"] if "text" in part]
                if msg_id_from_history == str(msg_id) and text in msg_texts_from_history:
                    msg_finded_key = True
                    break

            assert msg_finded_key, "Текст сообщения не доступен"
