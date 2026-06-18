import allure
import pytest

from support.markers import SAAS, ISOLATION, PRE_SAAS


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Реакции")
@allure.feature("Реакции в чате")
@allure.title("Получение списка реакций к сообщению в чате")
@ISOLATION
@PRE_SAAS
@SAAS
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_reactions_isolation(
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
        opponent_chat = main_acc.uin
    elif chat_type == "group":
        chat = group
        opponent_chat = group
    else:
        chat = channel
        opponent_chat = channel

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

        response = opponent.rapi_reaction_add(
            msgId=msg_id,
            chatId=opponent_chat,
            reactions=reactions_fixt,
            reaction=reaction,
        )

        assert response["status"]["code"] == 20000, f'Failed to add reaction "{reaction}" to msg ID {msg_id}'

    with allure.step(
        f"Проверяем наличие {reaction} к сообщению ID {msg_id}",
    ):
        response = main_acc.rapi_reaction_list(
            chatId=chat,
            msgId=msg_id,
            reaction=reaction,
            olderThan="0",
        )
        reaction_response = response["results"]

        users_in_reaction_list = [x["user"] for x in reaction_response["reactions"]]

        assert main_acc.uin in users_in_reaction_list, "Failed to found user reaction in list"

        assert opponent.uin in users_in_reaction_list, "Failed to found user reaction in list"
