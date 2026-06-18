import allure
import pytest

from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import send_message_rapi, send_message_wim


@allure.id("2213002")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Сообщения")
@allure.title("Отправка сообщения с чувствительными данными")
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
def test_send_message_with_sensitive_data(
    send_func, chat_type, check_event_send_message_event_exist, chat_entities, dlp_block_text
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
    text = dlp_block_text

    with allure.step("Отправляем сообщение получателю"):
        status_code, msg_id = send_func(main_acc, chat, text)

    with allure.step("Проверяем что ID сообщения не вернулось"):
        assert msg_id is None, "Идентификатор сообщения присутствует"
        assert status_code == 40607, "Сообщение не заблокировано"

    reader_acc = opponent_acc
    if chat_type == "favorites":
        reader_acc = main_acc

    with allure.step("Дополнительно проверяем что событие с текстом сообшения у оппонента не пришло"):
        assert not check_event_send_message_event_exist(reader_acc, msg_text=text), "Событие о новом сообщении найдено"
