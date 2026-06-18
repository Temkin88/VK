import uuid

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


def get_cursor(acc, curs=None):
    if curs is None:
        response = acc.rapi_thread_feed_get()
        cursor = response["results"].get("cursor")
    else:
        response = acc.rapi_thread_feed_get(cursor=curs)
        cursor = response["results"].get("cursor")

    return cursor


@allure.id("493555")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Треды")
@allure.feature("Скрол тредов")
@allure.title("Скрол тредов")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.first
def test_thread_scroll(
    chat_type,
    prepare_test_chats,
):
    """
    Проверяем скрола тредов
    """
    msg_ids = []
    threads_ids = []
    main_acc, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    for iterator in range(31):
        with allure.step("Отправляем тестовое сообщение"):
            msg_id = main_acc.send_basic_message(
                sn=chat,
                text=f"Test text-{uuid.uuid4().hex}",
            )

            msg_ids.append(msg_id)

        with allure.step(f"Пытаемся создать тред от сообщения ID {msg_id}"):
            response = main_acc.rapi_thread_add(
                chatId=chat,
                messageId=msg_id,
            )
            threads_ids.append(response["results"]["threadId"])

        with allure.step(
            f"Пытаемся отправить сообщение в тред ID {response['results']['threadId']}",
        ):
            main_acc.send_basic_message(
                sn=response["results"]["threadId"],
                text="Test msg to thread",
            )

        with allure.step("Проверка курсора"):
            if iterator == 0 or iterator == 8:
                response = main_acc.rapi_thread_feed_get()

                assert response["status"]["code"] == 20000, "Response error code"
                assert "cursor" not in response["results"], "Field 'cursor' in response"

            elif iterator == 10:
                response = main_acc.rapi_thread_feed_get()
                threads = threads_ids[1:]

                assert len(threads) == len(response["results"]["threads"]), "Count not match"
                assert all(thread["threadId"] in threads for thread in response["results"]["threads"]), (
                    f"Tread not list {threads}"
                )

                assert response["status"]["code"] == 20000, "Response error code"
                assert "cursor" in response["results"], "Field 'cursor' in response"

            elif iterator == 20:
                cursor = get_cursor(acc=main_acc)
                response = main_acc.rapi_thread_feed_get(cursor=cursor)
                threads = threads_ids[1:11]
                assert len(threads) == len(response["results"]["threads"]), "Count not match"
                assert all(thread["threadId"] in threads for thread in response["results"]["threads"]), (
                    f"Tread not list {threads}"
                )

                assert response["status"]["code"] == 20000, "Response error code"

            elif iterator == 30:
                cursor_1 = get_cursor(acc=main_acc)
                cursor_2 = get_cursor(acc=main_acc, curs=cursor_1)

                response = main_acc.rapi_thread_feed_get(cursor=cursor_2)
                threads = threads_ids[1:11]

                assert len(threads) == len(response["results"]["threads"]), "Count not match"
                assert all(thread["threadId"] in threads for thread in response["results"]["threads"]), (
                    f"Tread not list {threads}"
                )

                assert response["status"]["code"] == 20000, "Response error code"
                assert "cursor" in response["results"], "Field 'cursor' in response"
                assert cursor_1 != cursor_2 != response["results"]["cursor"], "Cursor matched"

    with allure.step("Пытаемся удалить первые 10 сообщений с тредами"):
        response = main_acc.rapi_delMsgBatch(
            sn=chat,
            msgIds=msg_ids[:10],
            shared=True,
            silent=False,
        )
        assert response["status"]["code"] == 20000, "Response error code"

    with allure.step("Пытаемся проверяем что курсор остался при оставшихся тредах"):
        cursor = get_cursor(acc=main_acc)
        response = main_acc.rapi_thread_feed_get(cursor=cursor)

        assert response["status"]["code"] == 20000, "Response error code"
        assert "cursor" in response["results"], "Field 'cursor' in response"
