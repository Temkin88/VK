import time

import allure

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS

MIN_PIN_API_VERSION = 100


@allure.id("31908")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Контакты")
@allure.feature("Изменение контакта")
@allure.title("Изменить контакт")
def test_contact_edit(
    setup_contact_add,
    auth_account,
    opponent_account,
):
    """
    Проверяем редактирование контакта из контакт листа
    :param setup_contact_add: Фикстура в которой происходит отправка сообщения с дополнительного аккаунта на основной
    :param auth_account: Основной аккаунт
    :param opponent_account: Дополнительный аккаунт
    """
    nick = "test nick"
    with allure.step("Пробуем получить информацию"):
        auth_account.rapi_contacts_edit(
            sn=opponent_account.uin,
            friendly=nick,
        )

    with allure.step("Проверяем что присвоили ник оппоненту"):
        nick_changed = False

        for _ in range(3):
            response = auth_account.rapi_getUserInfo(
                sn=opponent_account.uin,
            )

            results = response["results"]

            if results["friendly"] == nick:
                nick_changed = True
                break
            else:
                time.sleep(1)

        assert nick_changed, 'Friendly field not equal to "test nick"'
