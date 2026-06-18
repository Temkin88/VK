import time

import allure
import lorem
import pytest

from support.markers import SAAS, ISOLATION, PRE_SAAS


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по сообщениям среди тредов указанного чата")
@ISOLATION
@PRE_SAAS
@SAAS
def test_search_chat_threads_isolation(
    prepared_thread_isolation,
):
    auth_account, opponent_account, target, msg_id, thread_id = prepared_thread_isolation

    text = lorem.sentence().replace(" ", "_")

    with allure.step("Пишем сообщение в тред"):
        thread_msg_id = auth_account.send_basic_message(
            sn=thread_id,
            text=text,
        )

    with allure.step("Ищем сообщение в тредах в указанном чате"):
        msg_found = False

        for i in range(6):
            result = opponent_account.rapi_searchChatThreads(
                sn=target,
                keyword=text,
                author=auth_account.uin,
            )

            for dialog in result["results"]["dialogs"]:
                if dialog["sn"] == thread_id:
                    if all(
                        entry["message"]["msgId"] == thread_msg_id and entry["message"]["text"] == text
                        for entry in dialog["entries"]
                    ):
                        msg_found = True
                        break
                else:
                    time.sleep(i)
            if msg_found:
                break

        assert msg_found, f"msg_not_found:{thread_msg_id}"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по сообщениям среди тредов указанного чата")
@ISOLATION
@PRE_SAAS
@SAAS
def test_search_chat_threads_isolation_not_in_tenant(prepared_thread_isolation, first_auth_account_not_in_tenant):
    auth_account, opponent_account, target, msg_id, thread_id = prepared_thread_isolation

    text = lorem.sentence().replace(" ", "_")

    with allure.step("Пишем сообщение в тред"):
        auth_account.send_basic_message(
            sn=thread_id,
            text=text,
        )

    with allure.step("Пишем сообщение в тред"):
        opponent_account.send_basic_message(
            sn=thread_id,
            text=text,
        )

    with allure.step("Ищем сообщение в тредах в указанном чате"), pytest.raises(Exception):
        first_auth_account_not_in_tenant.rapi_searchChatThreads(
            sn=target,
            keyword=text,
            author=auth_account.uin,
        )
