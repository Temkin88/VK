import allure

from support.markers import SANDBOX

@allure.id("2316315")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с закреплением сообщений в диалоге")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_pin(
    auth_account,
    opponent_account,
    write_to_dlg,
    pin_msg
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
        message_body={  "plain": "Корова в бомболюке 2" })

    pin_msg(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        msg_ids=[store_response_forward.messageId]
        )

    pin_msg(
        sender_sn=opponent_account.uin,
        opponent_sn=auth_account.uin,
        msg_ids=[store_response_backward.messageId]
        )
