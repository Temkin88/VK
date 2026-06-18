import allure

from support.markers import SANDBOX

import uuid

@allure.id("2316687")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с реакциями на сообщения в диалоге")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_reaction(
    auth_account,
    opponent_account,
    write_to_dlg,
    set_reaction_id
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

    set_reaction_id(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        message_id=store_response_forward.messageId,
        reaction_id=str(uuid.uuid4())
        )

    set_reaction_id(
        sender_sn=opponent_account.uin,
        opponent_sn=auth_account.uin,
        message_id=store_response_backward.messageId,
        reaction_id=str(uuid.uuid4())
        )
