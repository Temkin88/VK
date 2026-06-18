import allure

from support.markers import SANDBOX

@allure.id("2316316")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с удалением сообщений в диалоге")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_del_msg(
    auth_account,
    opponent_account,
    write_to_dlg,
    del_msg
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
    msg_id_forward = store_response_forward.messageId
    msg_id_backward = store_response_backward.messageId

    delete_response = del_msg(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        additional_msgs=[msg_id_forward, msg_id_forward + 2000])
    assert len(delete_response.failed_msgs) == 1, "Ошибка при удалении сообщений в диалоге"

    delete_response = del_msg(
        sender_sn=opponent_account.uin,
        opponent_sn=auth_account.uin,
        additional_msgs=[msg_id_backward, msg_id_backward + 2000])
    assert len(delete_response.failed_msgs) == 1, "Ошибка при удалении сообщений в диалоге"


@allure.id("2316306")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с глобальным удалением сообщений в диалоге")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_del_msg_glob(
    auth_account,
    opponent_account,
    write_to_dlg,
    del_msg_glob
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
    msg_id_forward = store_response_forward.messageId
    msg_id_backward = store_response_backward.messageId
    delete_response = del_msg_glob(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        additional_msgs=[msg_id_forward, msg_id_forward + 2000])
    assert len(delete_response.failed_msgs) == 1, "Ошибка при глобальном удалении сообщений в диалоге"
    delete_response = del_msg_glob(
        sender_sn=opponent_account.uin,
        opponent_sn=auth_account.uin,
        additional_msgs=[msg_id_backward, msg_id_backward + 2000])
    assert len(delete_response.failed_msgs) == 1, "Ошибка при глобальном удалении сообщений в диалоге"

@allure.id("2316308")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с удалением сообщений в диалоге до определенного сообщения")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_del_msg_up_to(
    auth_account,
    opponent_account,
    write_to_dlg,
    del_msg_up_to
    ):
    store_response_forward = write_to_dlg(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        store_params={},
        message_body={  "plain": "Корова в бомболюке" })
    msg_id_forward = store_response_forward.messageId
    del_msg_up_to(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        message_id=msg_id_forward)
