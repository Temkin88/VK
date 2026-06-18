import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26922")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Сообщения")
@allure.feature("Удаление сообщений")
@allure.title("Удаление сообщений в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("is_shared", [True, False], ids=["shared", "not_shared"])
@pytest.mark.parametrize("is_silent", [True, False], ids=["silent", "not_silent"])
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_msg_delete(
    is_shared,
    is_silent,
    chat_type,
    prepare_test_chats,
):
    """
    Проверяем удаление сообщений
    """
    main_acc, opponent, group, channel = prepare_test_chats

    if chat_type == "private":
        chat = main_acc.uin
    elif chat_type == "group":
        chat = group
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
        assert main_acc.rapi_delMsgBatch(
            sn=chat,
            msgIds=msg_ids,
            shared=is_shared,
            silent=is_silent,
        ), "Failed to delete msgs"
