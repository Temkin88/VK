import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("37515")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Треды")
@allure.feature("Информация о треде")
@allure.title("Поиск по списку подписчиков треда")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_thread_subscribers_get(
    chat_type,
    prepare_test_chats,
    ENV_PLATFORM,
):
    """
    Проверяем создание тредов
    """
    if ENV_PLATFORM == "TARM":
        pytest.skip("Отключается до устранения проблем по баге https://jira.vk.team/browse/IMSERVER-19077")

    main_acc, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем тестовое сообщение"):
        msg_id = main_acc.send_basic_message(
            sn=chat,
            text="Test msg for thread autosubscribe",
        )

    with allure.step("Создаем тред от этого сообщения"):
        thread_id = main_acc.add_thread(
            chat_id=chat,
            msg_id=msg_id,
        )

    with allure.step("Проверяем список подписчиков треда"):
        response = main_acc.rapi_thread_subscribers_search(thread_id, main_acc.uin)

        subsribers_list = [x["sn"] for x in response["results"]["subscribers"]]

        assert main_acc.uin in subsribers_list, "Failed to search self in subs list"
