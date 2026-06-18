import allure
import pytest

from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM


@allure.id("557305")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Сообщения")
@allure.title("Пересылка сообщения с чувствительными данными через message/send")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@DLP
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "thread"])
def test_forward_message_with_sensitive_data(chat_type, chat_entities):
    """
    Проверка пересылки обычного текстового сообщения
    """
    main_acc, opponent, chats = chat_entities

    chat = chats[chat_type]

    with allure.step("Отправка сообщения, чтобы потом отредактировать его"):
        msg_id = main_acc.send_basic_message_by_message_send(
            target=chat,
            plain="Test msg for forward",
        )
        assert msg_id, f"Failed to send msg to forward it to chat ID {chat}"

    with allure.step("Пересылка текстового сообщения"):
        response = main_acc.rapi_message_send(
            target=chat,
            parts={
                "forwardParts": [{"text": {"plain": "block"}, "time": 0, "sn": main_acc.uin, "msgId": msg_id}],
            },
        )

        assert response["status"]["code"] == 40607, "Response code error"
