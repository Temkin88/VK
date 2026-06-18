import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_multipins.common import (
    multipin_channel_limit,
    multipin_chat_limit,
    multipin_personal_limit,
    random_pin_in_dialog,
    random_check_multipin_in_dialog,
    random_pin_in_chat,
    random_check_multipin_in_chat,
)


@allure.id("881211")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Мультипины")
@allure.title("Проверка возможности пинить больше 1 сообщения в личках")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private"])
def test_basic_multipin_pin_private(
    chat_type,
    prepare_personal_dialog,
):
    """
    Проверка возможности пинить больше 1 сообщения в личках
    Также проверяем, что все запиненные сообщения отсортированы по msgId (что совпадает с сортировкой по времени)
    """

    accounts, msgs_to_pin = prepare_personal_dialog()

    pinned_msgs = []
    patch_version = "init"
    with allure.step(f"Случайным образом закрепляем {multipin_personal_limit} сообщений в {chat_type}"):
        for _ in range(multipin_personal_limit):
            random_pin_in_dialog(accounts, msgs_to_pin, pinned_msgs)
            patch_version = random_check_multipin_in_dialog(
                accounts, pinned_msgs, patch_version, check_patch_update=True
            )


@allure.id("881212")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Мультипины")
@allure.title("Проверка возможности пинить больше 1 сообщения в чатах / каналах")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_basic_multipin_pin_chat(
    chat_type,
    prepare_chat,
):
    """
    Проверка возможности пинить больше 1 сообщения в каналах / чатах
    Также проверяем, что все запиненные сообщения отсортированы по msgId (что совпадает с сортировкой по времени)
    """

    is_channel, chat, accounts, msgs_to_pin = prepare_chat(chat_type)
    cur_limit = multipin_channel_limit if is_channel else multipin_chat_limit
    pinned_msgs = []
    patch_version = "init"
    with allure.step(f"Случайным образом закрепляем {cur_limit} сообщений в {chat_type}"):
        for _ in range(cur_limit):
            random_pin_in_chat(accounts, chat, chat_type, msgs_to_pin, pinned_msgs)
            patch_version = random_check_multipin_in_chat(
                accounts, chat, chat_type, pinned_msgs, patch_version, check_patch_update=True
            )
