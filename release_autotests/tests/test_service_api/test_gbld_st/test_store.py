import allure

from support.markers import SANDBOX

@allure.id("2316686")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Ядро отправки сообщений")
@allure.feature("Базовые сценарии работы с диалогами с помощью gbld-st")
@allure.title("Положительные сценарии по работе c store в диалоге")
#@PRE_SAAS
#@PRE_TARM
#@PRE_VKTI
@SANDBOX
def test_store(
    auth_account,
    opponent_account,
    write_to_dlg
    ):
    write_to_dlg(
        sender_sn=auth_account.uin,
        opponent_sn=opponent_account.uin,
        store_params={
                "read_all": True,
                "from_sn": auth_account.uin,
                "extstate": {
                    "last_message_heads": {
                        "heads": [{"sn": auth_account.uin}]
                        }
                }
            },
        message_body={
            "plain": "Корова в бомболюке",
            "parts_json": '{"mediaType" : "text", "text" : "Корова в бомболюке"}',
            "parts": {
                "text": {
                    "text":"В другом отсеке",
                    "sn": auth_account.uin
                    }
            },
            "typing": True,
            "hide_edit": True,
            "origin": {
                "client_id": 123123,
                "req_id": "777",
                "ip": "0.0.0.0",
                "ua": "Windows"
            },
            "message_class": 0,
        })
    write_to_dlg(
        sender_sn=opponent_account.uin,
        opponent_sn=auth_account.uin,
        store_params={
                "read_all": True,
                "from_sn": opponent_account.uin,
                "extstate": {
                    "last_message_heads": {
                        "heads": [{"sn": opponent_account.uin}]
                        }
                }
            },
        message_body={
            "plain": "Корова в бомболюке",
            "parts_json": '{"mediaType" : "text", "text" : "Корова в бомболюке"}',
            "parts": {
                "text": {
                    "text":"В другом отсеке",
                    "sn": opponent_account.uin
                    }
            },
            "typing": True,
            "hide_edit": True,
            "origin": {
                "client_id": 123123,
                "req_id": "777",
                "ip": "0.0.0.0",
                "ua": "Windows"
            },
            "message_class": 0,
        })
