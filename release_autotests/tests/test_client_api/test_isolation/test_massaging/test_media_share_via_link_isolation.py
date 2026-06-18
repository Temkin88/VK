import allure
import pytest


from support.markers import SAAS, ISOLATION, PRE_SAAS


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки фото")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_photo_isolation(chat_type, prepare_test_chats_msg_isolation, photo):
    """
    Проверка отправки фото
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "favorite":
        chat = main_acc.uin
    else:
        chat = channel

    with allure.step("Отправляем ссылку на фото"):
        msg_id = main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=photo,
        )
        assert msg_id, f"Failed to send photo to chat ID {chat}"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки стикера")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_sticker_isolation(chat_type, prepare_test_chats_msg_isolation, sticker):
    """
    Проверка отправки стикера
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем ссылку на стикер"):
        msg_id = main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=sticker,
        )
        assert msg_id, f"Failed to send sticker to chat ID {chat}"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки голосового сообщения")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_media_via_link_isolation(chat_type, prepare_test_chats_msg_isolation, voice):
    """
    Проверка отправки голосового сообщения
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем ссылку на голосовое сообщение"):
        msg_id = main_acc.send_basic_message_by_message_send(
            target=chat,
            plain=voice,
        )
        assert msg_id, f"Failed to send voice to chat ID {chat}"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки фото")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_photo_isolation_not_in_tenant(
    chat_type, prepare_test_chats_msg_isolation, photo, first_auth_account_not_in_tenant, check_message_in_history
):
    """
    Проверка отправки фото
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "favorite":
        chat = main_acc.uin
    else:
        chat = channel

    with allure.step("Отправляем ссылку на фото пользователем не из тенанта"), pytest.raises(Exception):
        msg_id = first_auth_account_not_in_tenant.send_basic_message_by_message_send(
            target=chat,
            plain=photo,
        )
        assert check_message_in_history(
            acc=main_acc,
            sn=chat,
            msg_id=msg_id,
        )


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки стикера")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_sticker_isolation_not_in_tenant(
    chat_type, prepare_test_chats_msg_isolation, sticker, first_auth_account_not_in_tenant, check_message_in_history
):
    """
    Проверка отправки стикера
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем ссылку на стикер пользователем не из тенанта"), pytest.raises(Exception):
        msg_id = first_auth_account_not_in_tenant.send_basic_message_by_message_send(
            target=chat,
            plain=sticker,
        )
        assert check_message_in_history(
            acc=main_acc,
            sn=chat,
            msg_id=msg_id,
        )


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Отправка сообщений через message/send")
@allure.title("Проверка отправки голосового сообщения")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_share_media_via_link_isolation_not_in_tenant(
    chat_type, prepare_test_chats_msg_isolation, voice, first_auth_account_not_in_tenant, check_message_in_history
):
    """
    Проверка отправки голосового сообщения
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем ссылку на голосовое сообщение пользователем не из тенанта"), pytest.raises(Exception):
        msg_id = first_auth_account_not_in_tenant.send_basic_message_by_message_send(
            target=chat,
            plain=voice,
        )
        assert check_message_in_history(
            acc=main_acc,
            sn=chat,
            msg_id=msg_id,
        )
