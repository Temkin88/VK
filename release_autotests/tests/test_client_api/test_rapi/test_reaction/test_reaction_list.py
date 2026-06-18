import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("28145")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Реакции")
@allure.feature("Реакции в чате")
@allure.title("Получение списка реакций к сообщению в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_reactions(
    chat_type,
    reactions_fixt,
    prepare_test_chats,
):
    """
    Проверяем добавление, наличие и удаление реакции к сообщению
    """

    main_acc, opponent, group, channel = prepare_test_chats

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
        assert main_acc.rapi_reaction_add(
            msgId=msg_id,
            chatId=chat,
            reactions=reactions_fixt,
            reaction=reaction,
        )["status"]["code"], f'Failed to add reaction "{reaction}" to msg ID {msg_id}'

        assert opponent.rapi_reaction_add(
            msgId=msg_id,
            chatId=opponent_chat,
            reactions=reactions_fixt,
            reaction=reaction,
        )["status"]["code"], f'Failed to add reaction "{reaction}" to msg ID {msg_id}'

    with allure.step(
        f"Проверяем наличие {reaction} к сообщению ID {msg_id}",
    ):
        response = main_acc.rapi_reaction_list(
            chatId=chat,
            msgId=msg_id,
            reaction=reaction,
            olderThan="0",
        )["results"]

        users_in_reaction_list = [x["user"] for x in response["reactions"]]

        assert main_acc.uin in users_in_reaction_list, "Failed to found user reaction in list"

        assert opponent.uin in users_in_reaction_list, "Failed to found user reaction in list"
