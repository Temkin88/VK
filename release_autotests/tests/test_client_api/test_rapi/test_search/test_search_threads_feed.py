import time

import allure
import lorem

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("28135")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по потоку тредов")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_search_thread_feed(
    prepared_thread,
    auth_account,
):
    target, msg_id, thread_id = prepared_thread

    text = lorem.sentence().replace(" ", "_")

    with allure.step("Пишем сообщение в тред"):
        thread_msg_id = auth_account.send_basic_message(
            sn=thread_id,
            text=text,
        )

    with allure.step("Ищем сообщение в потоке тредов"):
        entry_found_and_checked = False

        for i in range(6):
            result = auth_account.rapi_searchThreadsFeed(
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
