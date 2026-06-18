import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26948")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Реакции")
@allure.feature("Реакции в чате")
@allure.title("Получение реакции к сообщению в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_reactions_get(
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
        assert main_acc.rapi_reaction_add(
            msgId=msg_id,
            chatId=chat,
            reactions=reactions_fixt,
            reaction=reaction,
        )["status"]["code"], f'Failed to add reaction "{reaction}" to msg ID {msg_id}'

    with allure.step(
        f"Проверяем наличие {reaction} к сообщению ID {msg_id}",
    ):
        reaction_get_response = main_acc.rapi_reaction_get(
            chatId=chat,
            msgIds=[msg_id],
        )["results"]["reactions"][-1]

        assert reaction_get_response["msgId"] == msg_id, f"msgId is'nt ID {msg_id}"
        assert reaction_get_response["chatId"] in [
            chat,
            f"{chat};{main_acc.uin}",
            f"{main_acc.uin};{chat}",
        ], f"chatId is'nt ID {chat}"
        assert reaction_get_response["myReaction"] == reaction

        for reaction_dict in reaction_get_response["reactions"]:
            if reaction_dict["reaction"] == reaction:
                assert reaction_dict["counter"] == 1, f'Counter for reaction "{reaction}" not equal 1'
            else:
                assert reaction_dict["counter"] == 0, f'Counter for reaction "{reaction_dict["reaction"]}" not equal 0'
