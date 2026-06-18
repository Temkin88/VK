import time

import allure
import lorem

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("67190")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Поиск")
@allure.feature("Поиск сообщений")
@allure.title("Поиск по сообщениям среди тредов указанного чата")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_search_chat_threads(
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

    with allure.step("Ищем сообщение в тредах в указанном чате"):
        msg_found = False

        for i in range(6):
            result = auth_account.rapi_searchChatThreads(
                sn=target,
                keyword=text,
                author=auth_account.uin,
            )

            for dialog in result["results"]["dialogs"]:
                if dialog["sn"] == thread_id:
                    assert all(
                        entry["message"]["msgId"] == thread_msg_id and entry["message"]["text"] == text
                        for entry in dialog["entries"]
                    ), f"msg_not_found:{thread_msg_id}"
                    msg_found = True
                    break
                else:
                    time.sleep(i)
            if msg_found:
                break

        assert msg_found, f"msg_not_found:{thread_msg_id}"
