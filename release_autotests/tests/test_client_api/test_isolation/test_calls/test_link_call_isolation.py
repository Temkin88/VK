import allure
import pytest

from support.markers import SAAS, ISOLATION


@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Конференция")
@allure.title("[DESKTOP] Звонок по ссылке")
@ISOLATION
@SAAS
@pytest.mark.parametrize("participants_count", [2])
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "favorite"])
def test_link_call_isolation(get_voip_bots, participants_count, prepare_test_chats_msg_isolation, chat_type):
    """
    Подключение к звонку по ссылке
    """
    auth_account, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "favorite":
        chat = auth_account.uin
    else:
        chat = channel

    with allure.step("Получение VoIP-ботов"):
        bots = get_voip_bots(participants_count)

        first_bot, *other_bots = bots

    with allure.step("Сгенерировать ссылку на звонок с любого из клиентов"):
        call_link = first_bot.create_conference().conferenceUrl

    with allure.step("Отправляем ссылку на фото"):
        msg_id = auth_account.send_basic_message_by_message_send(
            target=chat,
            plain=call_link,
        )
        assert msg_id, f"Failed to send msg to edit it to chat ID {chat}"


@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Звонки")
@allure.feature("Конференция")
@allure.title("[DESKTOP] Звонок по ссылке")
@ISOLATION
@SAAS
@pytest.mark.parametrize("participants_count", [2])
@pytest.mark.parametrize("chat_type", ["private", "group", "channel", "favorite"])
def test_link_call_isolation_not_in_tenant(
    get_voip_bots,
    participants_count,
    prepare_test_chats_msg_isolation,
    chat_type,
    auth_account_with_domain_lalalalalalal,
):
    """
    Подключение к звонку по ссылке
    """
    auth_account, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    elif chat_type == "favorite":
        chat = auth_account.uin
    else:
        chat = channel

    with allure.step("Получение VoIP-ботов"):
        bots = get_voip_bots(participants_count)

        first_bot, *other_bots = bots

    with allure.step("Сгенерировать ссылку на звонок с любого из клиентов пользователем не из тенанта"):
        call_link = first_bot.create_conference().conferenceUrl

    with allure.step("Отправляем ссылку на фото"), pytest.raises(Exception):
        auth_account_with_domain_lalalalalalal.send_basic_message_by_message_send(
            target=chat,
            plain=call_link,
        )
