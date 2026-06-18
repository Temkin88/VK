import allure

from support.markers import SANDBOX

@allure.id("2316311")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с проверкой статуса незнакомца в диалоге")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_is_stranger(
    auth_account,
    opponent_account,
    write_to_dlg,
    is_stranger
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

    response = is_stranger(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin)

    assert response.result["is_stranger"] == 0, "Ошибка при получении is_stranger диалога"


@allure.id("2316303")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе с получением статуса незнакомца в диалоге")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_get_stranger_status(
    auth_account,
    opponent_account,
    write_to_dlg,
    get_stranger_status
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

    get_stranger_status(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        from_sn=auth_account.uin,
        to_sn=opponent_account.uin)
