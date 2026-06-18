import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("37507")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Контакты")
@allure.feature("Изменение контакта")
@allure.title("Отключение уведомлений на время")
@pytest.mark.parametrize("duration", [-1, 0, 3600])
def test_contact_mute(
    setup_contact_add,
    auth_account,
    opponent_account,
    duration,
):
    with allure.step("Добавляем в контакты"):
        opponent_account.send_basic_message(auth_account.uin, "ping")
        auth_account.send_basic_message(opponent_account.uin, "pong")

    with allure.step("Пробуем сделать запрос"):
        auth_account.rapi_contacts_mute(
            sn=opponent_account.uin,
            duration=duration,
        )
