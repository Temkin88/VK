import allure
import lorem
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


# @allure.id("26911")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по всем чатам запиненного сообщения удаленного у отправителя")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_search_deleted_after_pin_message(
    chat_type,
    prepare_test_chats,
):
    """
    Проверяем поиск по всем чатам, удаленного у пользователя сообщения, которое предварительно было запинено
    Согласно багу IMSERVER-21544 эти действия должны приводить к ошибке с циклическими падениями mini
    Баг на данный момент исправлен и тест должен проходить.
    """
    main_acc, opponent, group, channel = prepare_test_chats

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем тестовое сообщение"):
        text = lorem.sentence()
        msg_id = main_acc.send_basic_message(
            sn=chat,
            text=text,
        )
    with allure.step(f"Пытаемся закрепить сообщение ID {msg_id}"):
        main_acc.rapi_pinMessage(
            sn=chat,
            msgId=msg_id,
        )
        main_acc.rapi_delMsgBatch(sn=chat, msgIds=[msg_id], shared=False)

    with allure.step("Ищем сообщение по всем чатам"):
        response = main_acc.rapi_searchAllDialogs(text)
        assert response["status"]["code"] == 20000, "rapi_searchAllDialogs - request failed"
