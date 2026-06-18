import random

import allure
import pytest
from pyvkteamsclient.client.exceptions import MultipinLimitException

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SANDBOX, SAAS, PRE_SAAS
from tests.test_client_api.test_rapi.test_multipins.common import (
    multipin_channel_limit,
    multipin_chat_limit,
    multipin_personal_limit,
    random_pin_in_dialog,
    random_pin_in_chat,
    check_multipins,
)


@allure.id("881215")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Мультипины")
@allure.title("Проверка ограничения на число запиненных в личке")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["private"])
def test_basic_multipin_pin_limit_private(
    chat_type,
    prepare_personal_dialog,
):
    """
    Проверка ограничения на число запиненных в личке
    """

    accounts, msgs_to_pin = prepare_personal_dialog()

    pinned_msgs = []

    with allure.step(
        f"Случайным образом закрепляем максимальное ({multipin_personal_limit}) число сообщений в {chat_type}"
    ):
        for _ in range(multipin_personal_limit):
            random_pin_in_dialog(accounts, msgs_to_pin, pinned_msgs)

    with (
        allure.step(f"Попытка запинить сообщение выше лимита в {chat_type}"),
        pytest.raises(MultipinLimitException),
    ):
        random_pin_in_dialog(accounts, msgs_to_pin, pinned_msgs)

    with allure.step(f"Открепляем одно сообщение в {chat_type}"):
        to_unpin_msg = pinned_msgs.pop(random.randint(0, len(pinned_msgs) - 1))
        user_to_unpin_idx = random.randint(0, 1)
        accounts[user_to_unpin_idx].rapi_pinMessage(
            sn=accounts[1 - user_to_unpin_idx].uin, msgId=to_unpin_msg, unpin=True
        )
        msgs_to_pin.append(to_unpin_msg)

    with allure.step(f"Пиним сообщение в {chat_type} после анпина и не получаем ошибку"):
        random_pin_in_dialog(accounts, msgs_to_pin, pinned_msgs)
        check_multipins(
            accounts[1],
            accounts[0].uin,
            pinned_msgs,
        )


@allure.id("881214")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Сообщения")
@allure.feature("Мультипины")
@allure.title("Проверка ограничения на число запиненных в чатах / каналах")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_basic_multipin_limit_pin_chat(
    chat_type,
    prepare_chat,
):
    """
    Проверка ограничения на число запиненных в чатах / каналах
    """

    is_channel, chat, accounts, msgs_to_pin = prepare_chat(chat_type)
    cur_limit = multipin_channel_limit if is_channel else multipin_chat_limit
    pinned_msgs = []
    with allure.step(f"Случайным образом закрепляем максимальное {cur_limit} число сообщений в {chat_type}"):
        for _ in range(cur_limit):
            random_pin_in_chat(accounts, chat, chat_type, msgs_to_pin, pinned_msgs)

    with (
        allure.step(f"Попытка запинить сообщение выше лимита в {chat_type}"),
        pytest.raises(MultipinLimitException),
    ):
        random_pin_in_chat(accounts, chat, chat_type, msgs_to_pin, pinned_msgs)

    with allure.step(f"Открепляем одно сообщение в {chat_type}"):
        to_unpin_msg = pinned_msgs.pop(random.randint(0, len(pinned_msgs) - 1))
        user_to_unpin_idx = 0 if is_channel else random.randint(0, 2)
        accounts[user_to_unpin_idx].rapi_pinMessage(sn=chat, msgId=to_unpin_msg, unpin=True)
        msgs_to_pin.append(to_unpin_msg)

    with allure.step(f"Пиним сообщение в {chat_type} после анпина и не получаем ошибку"):
        random_pin_in_chat(accounts, chat, chat_type, msgs_to_pin, pinned_msgs)

        user_to_check_idx = random.randint(0, 2)
        check_multipins(
            accounts[user_to_check_idx],
            chat,
            pinned_msgs,
        )
