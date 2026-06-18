import uuid

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("495870")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Проверка изменение порядка тредов")
@allure.title("Проверка изменение порядка тредов")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_thread_checking_order(
    chat_type,
    prepare_test_chats,
    fetch_until_empty_answer_with_filter,
    ENV_PLATFORM,
):
    """
    Проверяем изменение порядка тредов
    """
    if ENV_PLATFORM == "TARM":
        pytest.skip("Отключается до устранения проблем по баге https://jira.vk.team/browse/IMSERVER-19077")

    msg_ids = []
    main_acc, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    for _ in range(4):
        with allure.step("Отправляем тестовое сообщение"):
            msg_id = main_acc.send_basic_message(
                sn=chat,
                text=f"Test text-{uuid.uuid4().hex}",
            )
            msg_ids.append(msg_id)

        with allure.step("добавляем тред и подписываемся на него"):
            thread_id = main_acc.add_thread(chat_id=chat, msg_id=msg_id)

        with allure.step("Пишем сообщение в тред"):
            main_acc.send_basic_message(
                sn=thread_id,
                text=f"Test text-{uuid.uuid4().hex}",
            )

    with allure.step("Проверка порядка тредов"):
        response = main_acc.rapi_thread_feed_get()
        threads_list = response["results"]["threads"]
        threads_ids = [i["threadId"] for i in threads_list]

        assert response["status"]["code"] == 20000, "Response error code"

    with allure.step("Пишем сообщение в последний тред"):
        thread_msg_id = main_acc.send_basic_message(
            sn=threads_ids[-1],
            text="Test msg to thread",
        )
    with allure.step("Ишем сообщение в событии threadUpdate"):
        event_found = False
        for event in fetch_until_empty_answer_with_filter(main_acc, "threadUpdate"):
            event_data = event["eventData"]
            if event_data["yours"]["lastRead"] == thread_msg_id and event_data["threadId"] == threads_ids[-1]:
                event_found = True
                break

        assert event_found, f"Event threadUpdate with msg_id: {thread_msg_id} not found"

    with allure.step("Проверяем, что тред стал первым"):
        response = main_acc.rapi_thread_feed_get()
        threads_list = response["results"]["threads"]

        assert response["status"]["code"] == 20000, "Response error code"
        assert threads_ids[-1] == threads_list[0]["threadId"], "Thread id is dont matched"
