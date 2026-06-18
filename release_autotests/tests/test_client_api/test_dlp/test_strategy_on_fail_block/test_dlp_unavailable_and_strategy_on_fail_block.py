import allure
import pytest
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import send_message_rapi, send_message_wim


@allure.id("870473")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("DLP")
@allure.feature("Файлы")
@allure.title(
    "Если DLP система не доступна и в конфиге настроен strategy_on_fail: block, "
    + "система (Вахтёр) должна запретить отправку сообщения в личку/группу/канал/избранное."
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
def test_dlp_unavailable_and_strategy_on_fail_block(
    chat_type,
    fetch_until_empty_answer_with_filter,
    send_func,
    chat_entities,
    check_event_send_message_event_exist,
):
    text = "server_error_word"
    main_acc, opponent_acc, chats = chat_entities
    chat = chats[chat_type]

    with allure.step("Отправляем cообщение получателю"):
        status_code, msg_id = send_func(main_acc, chat, text=text)

    assert msg_id is None, "Идентификатор сообщения присутствует"

    reader_acc = opponent_acc
    if chat_type == "favorites":
        reader_acc = main_acc
    assert not check_event_send_message_event_exist(reader_acc, msg_text=text), "Событие о новом сообщении найдено"
