import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("28438")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Реакции")
@allure.feature("Реакции в чате")
@allure.title("Добавление реакции к сообщению в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private", "group", "channel"])
def test_reactions_add(
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

    with allure.step(f"Проверяем реакции к сообщению ID {msg_id}"):
        for reaction in reactions_fixt:
            with allure.step(
                f"Пробуем добавить реакцию {reaction} к сообщению ID {msg_id}",
            ):
                response = main_acc.rapi_reaction_add(
                    msgId=msg_id,
                    chatId=chat,
                    reactions=reactions_fixt,
                    reaction=reaction,
                )

                assert response["status"]["code"], f'Failed to add reaction "{reaction}" to msg ID {msg_id}'
