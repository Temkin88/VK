import allure
import pytest
from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM
from tests.test_client_api.test_dlp.common import send_message_rapi, send_message_wim


@allure.id("865492")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Сообщения")
@allure.title("Сообщение запрещено при превышении 2-го порога и strategy_on_fail=block")
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
def test_send_message_delay_and_strategy_on_fail_block(
    chat_type, send_func, chat_entities, check_event_send_message_event_exist
):
    """
    Проверяет, что если ответ DLP превысил второй порог, но strategy_on_fail=block,
    то сообщение не отправляется
    """

    text = "delay"
    main_acc, opponent_acc, chats = chat_entities
    chat = chats[chat_type]
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
