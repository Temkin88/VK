import allure

from support.markers import SANDBOX

@allure.id("2316318")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с выставлением состояния диалога")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_set_dlg_state(
    auth_account,
    opponent_account,
    write_to_dlg,
    set_dlg_state
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
        message_body={  "plain": "Корова в бомболюке" })
    msg_id_forward = store_response_forward.messageId

    set_dlg_state(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        set_dlg_state_params = {
                "delivered_message_id": msg_id_forward,
                "read_message_id": msg_id_forward,
                "to_sn": auth_account.uin,
                "from_sn": opponent_account.uin,
                "drop_stranger": True,
                "exclude_calls": True,
            }
        )

@allure.id("2316313")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с выставлением состояния диалога WIM")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_set_dlg_state_wim(
    auth_account,
    opponent_account,
    write_to_dlg,
    set_dlg_state_wim
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
        message_body={  "plain": "Корова в бомболюке" })
    msg_id_forward = store_response_forward.messageId

    set_dlg_state_wim(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        set_dlg_state_params = {
            "w_delivered_message_id": "test_msg",
            "w_read_message_id": "test_msg_2",
            "delivered_message_id": msg_id_forward,
            "read_message_id": msg_id_forward,
            "to_sn": auth_account.uin,
            "from_sn": opponent_account.uin,
            "drop_stranger": True,
            "exclude_calls": True,
            }
        )
