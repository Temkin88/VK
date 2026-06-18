import random

import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_multipins.common import (
    check_multipins,
    unpin_all_in_dialog,
    unpin_all_in_chat,
)


@allure.id("881213")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Мультипины")
@allure.title("Проверка возможности анпинить сообщения при наличии более 1 запиненного сообщения в личках")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private"])
def test_basic_multipin_unpin_private(chat_type, prepare_private_dialog_with_pins):
    """
    Проверка возможности анпинить сообщения при наличии более 1 запиненного сообщения в личках
    """

    accounts, pinned_msgs = prepare_private_dialog_with_pins()

    patch_version = check_multipins(
        accounts[1],
        accounts[0].uin,
        pinned_msgs,
    )
    with allure.step("Теперь открепим одно из сообщений в диалоге"):
        to_unpin_msg = pinned_msgs.pop(random.randint(0, len(pinned_msgs) - 1))
        user_to_unpin_idx = random.randint(0, 1)
        response = accounts[user_to_unpin_idx].rapi_pinMessage(
            sn=accounts[1 - user_to_unpin_idx].uin, msgId=to_unpin_msg, unpin=True
        )
        assert response["status"]["code"] == 20000, (
            f"Message {to_unpin_msg} unpin failed in {chat_type}! Already pinned {len(pinned_msgs)} msgs"
        )
        user_to_check_idx = random.randint(0, 1)
        with allure.step("Проверяем, что в getHistory в массиве pinned больше нет этого анпин-сообщения"):
            check_multipins(
                accounts[user_to_check_idx],
                accounts[1 - user_to_check_idx].uin,
                pinned_msgs,
                patch_version,
                check_patch_update=True,
            )

    with allure.step("Теперь открепим оставшиеся сообщения в диалоге"):
        unpin_all_in_dialog(accounts, pinned_msgs)
        check_multipins(
            accounts[1],
            accounts[0].uin,
            [],
        )


@allure.id("881216")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Мультипины")
@allure.title("Проверка возможности анпинить сообщения при наличии более 1 запиненного сообщения в чатах / каналаъ")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_basic_multipin_unpin_chat(chat_type, prepare_chat_with_pins):
    """
    Проверка возможности анпинить сообщения при наличии более 1 запиненного сообщения в чатах / каналаъх
    """

    is_channel, chat, accounts, pinned_msgs = prepare_chat_with_pins(chat_type)

    patch_version = check_multipins(
        accounts[1],
        chat,
        pinned_msgs,
    )
    with allure.step("Теперь открепим одно из сообщений в чате"):
        to_unpin_msg = pinned_msgs.pop(random.randint(0, len(pinned_msgs) - 1))
        user_to_unpin_idx = 0 if is_channel else random.randint(0, 2)
        response = accounts[user_to_unpin_idx].rapi_pinMessage(sn=chat, msgId=to_unpin_msg, unpin=True)
        assert response["status"]["code"] == 20000, (
            f"Message {user_to_unpin_idx} unpin failed in {chat_type}! Already pinned {len(pinned_msgs)} msgs"
        )

        user_to_check_idx = random.randint(0, 2)
        with allure.step("Проверяем, что в getHistory в массиве pinned больше нет этого анпин-сообщения"):
            check_multipins(accounts[user_to_check_idx], chat, pinned_msgs, patch_version, check_patch_update=True)

    with allure.step("Теперь открепим оставшиеся сообщения в чате"):
        unpin_all_in_chat(accounts, chat, chat_type, pinned_msgs, is_channel)
        user_to_check_idx = random.randint(0, 2)
        check_multipins(
            accounts[user_to_check_idx],
            chat,
            [],
        )
