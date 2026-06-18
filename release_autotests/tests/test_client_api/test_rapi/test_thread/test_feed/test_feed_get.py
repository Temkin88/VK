import allure
import pytest

from support.cases.formatted_msgs import formatted_msgs
from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.MESSAGING)]


@allure.id("26940")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Поток тредов")
@allure.label("layer", "api_layer")
@allure.title("Просмотр потока тредов")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_thread_feed_get(
    auth_account,
):
    """
    Проверяем запрос потока тредов
    """
    with allure.step("Делаем запрос"):
        auth_account.rapi_thread_feed_get()


@allure.id("26928")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Поток тредов")
@allure.title("Добавление нового треда в поток")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.parametrize("msg_parts", formatted_msgs)
def test_add_thread_to_feed(
    chat_type,
    msg_parts,
    prepare_test_chats,
):
    """
    Проверяем что новый тред появляется в потоке тредов
    """
    main_acc, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем тестовую задачу"):
        msg_id = main_acc.wim_im_sendIM(
            t=chat,
            parts=msg_parts,
        )["response"]["data"]["histMsgId"]

    with allure.step(f"Пытаемся создать тред от сообщения ID {msg_id}"):
        response = main_acc.rapi_thread_add(
            chatId=chat,
            messageId=msg_id,
        )

        assert response["status"]["code"] == 20000, f"Failed to create thread from msgId {msg_id} in chat {chat}"

        main_acc.send_basic_message(
            sn=response["results"]["threadId"],
            text="test",
        )

        searched_thread_id = response["results"]["threadId"]

    with allure.step("Ищем созданный тред в потоке тредов"):
        found = False

        for thread in main_acc.iter_thread_list(page_size=50):
            if thread["threadId"] == searched_thread_id:
                found = True

                assert thread["parentTopic"]["chatId"] == chat, "Thread has different parent topic"
                assert thread["parentTopic"]["messageId"] == msg_id, "Thread has different topic starter"

        assert found, f"Thread ID {searched_thread_id} not found in feed"


@allure.id("33155")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Треды")
@allure.feature("Поток тредов")
@allure.title("Треды без сообщений не отображаются в потоке")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_feed_does_not_contain_threads_without_any_message(
    chat_type,
    prepare_test_chats,
    ENV_PLATFORM,
):
    if ENV_PLATFORM == "TARM":
        pytest.skip("Отключается до устранения проблем по баге https://jira.vk.team/browse/IMSERVER-19077")

    user, opponent, group, channel = prepare_test_chats
    _ = opponent

    chat = group if chat_type == "group" else channel

    with allure.step("Отправляем сообщение в чат"):
        msg_id = user.send_basic_message(
            sn=chat,
            text="Она надежно меня спрячет, словно Кинг-Конг",
        )

    with allure.step(f"Создаем тред от сообщения ID {msg_id}"):
        response = user.rapi_thread_add(
            chatId=chat,
            messageId=msg_id,
        )

        assert response["status"]["code"] == 20000, f"Failed to create thread from msgId {msg_id} in chat {chat}"

        thread_id = response["results"]["threadId"]

    with allure.step(f"Подписываемся на тред {thread_id}"):
        resp = user.rapi_thread_subscribe(thread_id)

        assert resp["status"]["code"] == 20000, f"Failed to subscribe to thread {thread_id}"

    with allure.step("Получаем поток тредов"):
        resp = user.rapi_thread_feed_get()

    with allure.step("Проверяем, что в потоке нет пустого треда"):
        assert thread_id not in [x["threadId"] for x in resp["results"]["threads"]], (
            "Empty thread in response for rapi/thread/feed/get"
        )
