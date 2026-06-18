import allure
import pytest

from support.markers import SAAS, ISOLATION, PRE_SAAS


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Реакции")
@allure.feature("Реакции в чате")
@allure.title("Удаление реакции к сообщению в чате")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_reactions_remove_isolation(
    chat_type,
    reactions_fixt,
    prepare_test_chats_msg_isolation,
):
    """
    Проверяем добавление, наличие и удаление реакции к сообщению
    """

    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Отправляем тестовое сообщение"):
        msg_id = main_acc.send_basic_message(
            sn=chat,
            text="Test msg for reactions",
        )

    reaction = reactions_fixt[0]

    with allure.step(
        f"Пробуем добавить реакцию {reaction} к сообщению ID {msg_id}",
    ):
        response = main_acc.rapi_reaction_add(
            msgId=msg_id,
            chatId=chat,
            reactions=reactions_fixt,
            reaction=reaction,
        )

        assert response["status"]["code"] == 20000, f'Failed to add reaction "{reaction}" to msg ID {msg_id}'

    with allure.step(f"Удаляем {reaction} к сообщению ID {msg_id}"):
        response = main_acc.rapi_reaction_remove(
            chatId=chat,
            msgId=msg_id,
        )

        assert response["status"]["code"] == 20000, f'Failed to add reaction "{reaction}" to msg ID {msg_id}'
