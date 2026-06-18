import allure

from support.markers import SANDBOX

@allure.id("2316688")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с получением истории диалога с помощью select")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_select(
    auth_account,
    opponent_account,
    write_to_dlg,
    select
    ):
    store_response_forward = write_to_dlg(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        store_params={},
        message_body={  "plain": "Корова в бомболюке" })
    write_to_dlg(
        sender_sn=opponent_account.uin,
        opponent_sn=auth_account.uin,
        store_params={},
        message_body={  "plain": "Корова в бомболюке 2" })

    response = select(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        select_params={
                "slip": 10,
                "wstate": True,
                "evlist_ver": None,
                "after": store_response_forward.messageId
            }
        )
    assert len(response.result["messages"]) == 1, (
        "Ошибка при получении истории диалога с помощью select")

@allure.id("2316685")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с получением истории диалога с помощью select batch")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_select_batch(
    auth_account,
    opponent_account,
    write_to_dlg,
    select_batch
    ):
    store_response_forward = write_to_dlg(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        store_params={},
        message_body={  "plain": "Корова в бомболюке" })
    store_response_backward = write_to_dlg(
        sender_sn=opponent_account.uin,
        opponent_sn=auth_account.uin,
        store_params={},
        message_body={  "plain": "Корова в бомболюке" })

    response = select_batch(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        select_batch_params = {
                "no_evlist": True,
                "evlist_ver": "none",
                "sub_req_params": [
                    {"after": store_response_forward.messageId, "slip": 10},
                    {"until": store_response_backward.messageId, "slip": 12}]
            }
            )
    assert len(response.result["sub_req"][0]["messages"]) == 1, (
        "Ошибка при получении истории диалога с помощью select batch")
