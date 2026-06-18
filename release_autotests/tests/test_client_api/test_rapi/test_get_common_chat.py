import time

import allure

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CONTACTS)]


@allure.id("26901")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Чаты")
@allure.feature("Общие чаты")
@allure.title("Проверка списка общих чатов")
def test_get_common_chats(
    prepare_test_chats,
    fetch_until_empty_answer,
    event_filter,
):
    """
    Проверяем список общих чатов с пользователем
    """

    main_acc, opponent, group, channel = prepare_test_chats

    with allure.step(f"Создаем тестовый чат, общий с {opponent.uin}"):
        chat = main_acc.create_chat(
            "Test common chat",
            members=[opponent],
        )

    with allure.step(f"Запрашиваем список общих чатов с {opponent.uin}"):
        response = main_acc.rapi_getCommonChats(opponent.uin)

        assert response["status"]["code"] == 20000, "rapi_getCommonChats - request failed"

        assert response["results"]["chats"], "Empty chats list"

    with allure.step("Проверяем что чат пришел в событиях"):
        fetch_until_empty_answer(opponent)

        assert list(
            filter(
                lambda x: x["eventData"]["sn"] == chat,
                event_filter(opponent.events, "histDlgState"),
            )
        ), f'Failed to found common chat ID {chat} in events "histDlgState"'

    with allure.step(f"Проверяем что тестовый чат ID {chat} есть в списке"):
        for i in range(1, 5):
            chat_getter = [general_chat for general_chat in response["results"]["chats"] if general_chat["sn"] == chat]
            if not chat_getter:
                time.sleep(i)
                response = main_acc.rapi_getCommonChats(opponent.uin)

        assert [general_chat for general_chat in response["results"]["chats"] if general_chat["sn"] == chat], (
            f"Failed to found common chat ID {chat}"
        )
