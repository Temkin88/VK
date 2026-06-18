import allure

from support.markers import SANDBOX

@allure.id("2316314")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с проверкой пустоты диалога")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_is_dlg_empty(
    auth_account,
    opponent_account,
    write_to_dlg,
    is_dlg_empty
    ):
    write_to_dlg(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        store_params={},
        message_body={  "plain": "Корова в бомболюке" })
    write_to_dlg(
        sender_sn=opponent_account.uin,
        opponent_sn=auth_account.uin,
        store_params={},
        message_body={  "plain": "Корова в бомболюке 2" })

    response = is_dlg_empty(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin
        )
    assert response.result["is_empty"] == 0, "Ошибка при получении статуса пустоты диалога"
