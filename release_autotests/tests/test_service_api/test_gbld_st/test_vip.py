import allure

from support.markers import SANDBOX

@allure.id("2316307")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с vip статусом диалога")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_vip(
    auth_account,
    opponent_account,
    write_to_dlg,
    can_disturb_vip
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

    response = can_disturb_vip(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        vip_sn=opponent_account.uin)
    assert response.result["verdict"] == 1, "Ошибка при получении can_disturb vip диалога"
