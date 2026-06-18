import allure
import pytest

from support.markers import SAAS, ISOLATION, PRE_SAAS


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Сообщения")
@allure.feature("Удаление сообщений")
@allure.title("Удаление сообщений в чате")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("is_shared", [True, False], ids=["shared", "not_shared"])
@pytest.mark.parametrize("is_silent", [True, False], ids=["silent", "not_silent"])
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_msg_delete_isolation(
    is_shared,
    is_silent,
    chat_type,
    prepare_test_chats_msg_isolation,
):
    """
    Проверяем удаление сообщений
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

    msg_ids = []

    with allure.step("Отправляем пачку тестовых сообщений"):
        for i in range(5):
            msg_ids.append(
                main_acc.send_basic_message(
                    sn=chat,
                    text=f"#{i + 1} Test msg for delete [is_shared={is_shared}, is_silent={is_silent}]",
                ),
            )

    with allure.step("Пытаемся удалить пачку сообщений"):
        msg_id = main_acc.rapi_delMsgBatch(
            sn=chat,
            msgIds=msg_ids,
            shared=is_shared,
            silent=is_silent,
        )
        assert msg_id, "Failed to delete msgs"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Сообщения")
@allure.feature("Удаление сообщений")
@allure.title("Удаление сообщений в чате")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("is_shared", [True, False], ids=["shared", "not_shared"])
@pytest.mark.parametrize("is_silent", [True, False], ids=["silent", "not_silent"])
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_msg_delete_isolation_not_in_tenant(
    is_shared,
    is_silent,
    chat_type,
    prepare_test_chats_msg_isolation,
    first_auth_account_not_in_tenant,
    check_message_in_history,
):
    """
    Проверяем удаление сообщений
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

    msg_ids = []

    with allure.step("Отправляем пачку тестовых сообщений"):
        for i in range(5):
            msg_ids.append(
                main_acc.send_basic_message(
                    sn=chat,
                    text=f"#{i + 1} Test msg for delete [is_shared={is_shared}, is_silent={is_silent}]",
                ),
            )

    with allure.step("Пытаемся удалить пачку сообщений пользователем не из тенанта"), pytest.raises(Exception):
        first_auth_account_not_in_tenant.rapi_delMsgBatch(
            sn=chat,
            msgIds=msg_ids,
            shared=is_shared,
            silent=is_silent,
        )
        assert not check_message_in_history(
            acc=main_acc,
            sn=chat,
            msg_id=msg_ids,
        )
