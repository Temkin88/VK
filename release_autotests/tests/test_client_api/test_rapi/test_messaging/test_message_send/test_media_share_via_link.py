import allure
import pytest


from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS


@allure.id("515245")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки фото")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_photo(
    chat_type,
    prepare_test_chats_msg,
    photo,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки фото
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем ссылку на фото"):
        send_msg_id = main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=photo,
        )

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        for account in [opponent]:
            assert check_events_list_contains_event_with_msgId(account, send_msg_id), (
                f"Sended message not found in events of {account}"
            )


@allure.id("515240")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки стикера")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_sticker(
    chat_type,
    prepare_test_chats_msg,
    sticker,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки стикера
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем ссылку на стикер"):
        send_msg_id = main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=sticker,
        )

    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        for account in [opponent]:
            assert check_events_list_contains_event_with_msgId(account, send_msg_id), (
                f"Sended message not found in events of {account}"
            )


@allure.id("513340")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки голосового сообщения")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_media_via_link(
    chat_type,
    prepare_test_chats_msg,
    voice,
    check_history_contains_message_with_msgId,
    check_events_list_contains_event_with_msgId,
):
    """
    Проверка отправки голосового сообщения
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем ссылку на голосовое сообщение"):
        send_msg_id = main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=voice,
        )
    with allure.step("Проверяем наличие отправленного сообщения в истории переписки"):
        assert check_history_contains_message_with_msgId(main_acc, send_msg_id, chat), (
            "Sended message not found in history"
        )

    with allure.step("Проверяем наличие события отправленного сообщения в истории переписки"):
        assert check_events_list_contains_event_with_msgId(opponent, send_msg_id), "Sended message not found in events"
