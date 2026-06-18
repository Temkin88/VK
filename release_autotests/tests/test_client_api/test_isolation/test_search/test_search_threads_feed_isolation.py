import time

import allure
import lorem
import pytest

from support.markers import SAAS, ISOLATION


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по потоку тредов")
@ISOLATION
@SAAS
def test_search_thread_feed_isolation(
    prepared_thread_isolation,
):
    auth_account, opponent_account, target, msg_id, thread_id = prepared_thread_isolation

    text = lorem.sentence().replace(" ", "_")

    with allure.step("Пишем сообщение в тред"):
        thread_msg_id = auth_account.send_basic_message(
            sn=thread_id,
            text=text,
        )

    with allure.step("Пишем сообщение в тред"):
        opponent_account.send_basic_message(
            sn=thread_id,
            text=text,
        )

    with allure.step("Ищем сообщение в потоке тредов"):
        entry_found_and_checked = False

        for i in range(6):
            result = opponent_account.rapi_searchThreadsFeed(
                keyword=text,
            )

            for dialog in result["results"]["dialogs"]:
                if dialog["sn"]:
                    for entry in dialog["entries"]:
                        message = entry["message"]
                        if message["msgId"] == thread_msg_id and message["text"] == text:
                            entry_found_and_checked = True
                            break
                    if entry_found_and_checked:
                        break
                    else:
                        time.sleep(i)
            if entry_found_and_checked:
                break

        assert entry_found_and_checked, (
            f"/api/v{auth_account.api_ver}/rapi/searchThreadsFeed:msg_not_found:{thread_msg_id}"
        )


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по потоку тредов")
@ISOLATION
@SAAS
def test_search_thread_feed_isolation_not_in_tenant(
    prepared_thread_isolation,
    first_auth_account_not_in_tenant,
):
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

    with allure.step("Ищем сообщение в потоке тредов"), pytest.raises(Exception):
        first_auth_account_not_in_tenant.rapi_searchThreadsFeed(
            keyword=text,
        )
