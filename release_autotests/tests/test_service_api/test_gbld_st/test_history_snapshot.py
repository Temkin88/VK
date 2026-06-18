import allure

from support.markers import SANDBOX

@allure.id("2316317")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с получением снепшота истории диалога")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_history_snapshot(
    auth_account,
    opponent_account,
    write_to_dlg,
    get_history_snapshot
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

    snapshot_response = get_history_snapshot(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin
        )
    assert len(snapshot_response.result["dumps"]) > 0, "Ошибка при получении снепшота истории диалога"
