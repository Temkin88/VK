import allure
import pytest

from support.markers import SANDBOX, DLP, VKTI, PRE_VKTI, SAAS, PRE_SAAS, TARM, PRE_TARM


@allure.id("557295")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("DLP")
@allure.feature("Сообщения")
@allure.title("Редактирование сообщения с чувствительными данными через sendIM")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@DLP
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "thread"])
def test_edit_message_with_sensitive_data_by_sendIM(chat_type, chat_entities):
    """
    Проверяем редактирование сообщений
    """
    main_acc, opponent, chats = chat_entities

    chat = chats[chat_type]

    with allure.step("Отправка тестового сообщения"):
        msg_id = main_acc.send_basic_message(
            sn=chat,
            text="Test msg for edit",
        )

    with allure.step(f"Редактируем сообщение ID {msg_id}"):
        response = main_acc.wim_im_sendIM(
            t=chat,
            updateMsgId=msg_id,
            message="block",
        )

        assert response["response"]["statusCode"] == 603, "Response code error"
