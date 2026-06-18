import bisect
import random
from typing import Optional, List

import allure
from keyring.backends import null

multipin_personal_limit = 10
multipin_chat_limit = 10
multipin_channel_limit = 10

correct_message = "обычное сообщение"
failed_message = "Сообщение невалидно! НЕ ДОЛЖНО ПОЯИВТЬСЯ В ПЕРЕПИСКЕ!"
msg_too_long_len = 64000 + 1

formally_ok_but_invalid_user_sn = "123@invalid.com"
obviously_invalid_user_sn = "111e"


@allure.step("Проверяем правильности массива pinned сообщений")
def check_multipins(
    account,
    chat,
    expected_msgs,
    prev_patch_version: Optional[str] = None,
    check_patch_update=False,
):
    """
    Запиненные сообщения должны быть отсортированны по msgId от самого нового сообщения к самому старому
    """
    expected_msgs.sort(reverse=True)
    response = account.rapi_getHistory(sn=chat, count=-1)
    results = response["results"]
    if len(expected_msgs) == 0 and ("patch" in results):
        pinned_patches = set()
        unpinned_patches = set()
        patches = results["patch"]
        for item in patches:
            if "type" in item:
                if item["type"] == "pinned":
                    pinned_patches.add(int(item["msgId"]))
                elif item["type"] == "unpinned":
                    unpinned_patches.add(int(item["msgId"]))
        assert pinned_patches == unpinned_patches, (
            f"There is some unpinned messages in history {response}! Expected: 0 msgs, patch {patches}"
        )

    if "pinned" not in results:
        assert len(expected_msgs) == 0, f"No pinned messages in history {response}! Expected: {expected_msgs}"
    else:
        pinned_msgs_info = results["pinned"]
        assert len(pinned_msgs_info) == len(expected_msgs), (
            f"Number of pinned messages in history not equal to expected! "
            f"Expected: {expected_msgs}, in fact: {pinned_msgs_info}"
        )

        really_pinned_msgs = []
        for msg_info in pinned_msgs_info:
            assert "msgId" in msg_info, f"No pinned msgId in pinned array {pinned_msgs_info}!"
            really_pinned_msgs.append(int(msg_info["msgId"]))
        assert really_pinned_msgs == expected_msgs, (
            f"Multipins error! Expected pinned: {expected_msgs}, in fact: {really_pinned_msgs}"
        )

        assert "patchVersion" in results, f"No patchVersion in history: {results}"

        new_patch_version = results["patchVersion"]
        assert not check_patch_update or (prev_patch_version is not None and prev_patch_version != new_patch_version)

        return new_patch_version


@allure.step("Отчищаем массив запиненных в диалоге")
def unpin_all_in_dialog(two_accounts, pinned_msgs: Optional[List[int]] = null):
    """
    При уделении сообщения на клиентах автоматичнски дергается метод pinMessage с параметром unpin = true,
        те бек сам при удалении сообщений не чистит пины
    Поэтому в личках нужно чистить пины перед началом теста

    Если в конце теста есть список запиненых, чистим явно его
    """
    first_acc, second_acc = two_accounts
    if pinned_msgs != null:
        for to_unpin_msg in pinned_msgs:
            first_acc.rapi_pinMessage(sn=second_acc.uin, msgId=to_unpin_msg, unpin=True)
    else:
        response = first_acc.rapi_getHistory(sn=second_acc.uin, count=-1)
        already_unpinned = set()

        if "patch" in response["results"]:
            pinned_patches = set()
            unpinned_patches = set()
            for item in response["results"]["patch"]:
                if "type" in item:
                    if item["type"] == "pinned":
                        pinned_patches.add(int(item["msgId"]))
                    elif item["type"] == "unpinned":
                        unpinned_patches.add(int(item["msgId"]))

            msgs_to_unpin = pinned_patches.difference(unpinned_patches)
            for to_unpin_msg in msgs_to_unpin:
                first_acc.rapi_pinMessage(sn=second_acc.uin, msgId=to_unpin_msg, unpin=True)
                already_unpinned.add(to_unpin_msg)

        if "pinned" in response["results"]:
            pinned_msgs_info = response["results"]["pinned"]
            for item in pinned_msgs_info:
                if "msgId" not in already_unpinned:
                    first_acc.rapi_pinMessage(sn=second_acc.uin, msgId=item["msgId"], unpin=True)


@allure.step("Отчищаем массив запиненных в чате / канале")
def unpin_all_in_chat(three_accounts, chat, chat_type, pinned_msgs, is_channel=False):
    """
    В чатах можно пинить только админам, поэтому анпить тоже можно произвольно
    В канале может анпинить создатель канала
    """
    for to_unpin_msg in pinned_msgs:
        user_to_unpin_idx = 0 if is_channel else random.randint(0, 2)
        response = three_accounts[user_to_unpin_idx].rapi_pinMessage(sn=chat, msgId=to_unpin_msg, unpin=True)
        assert response["status"]["code"] == 20000, (
            f"Message {user_to_unpin_idx} unpin failed in {chat_type}! Already pinned {len(pinned_msgs)} msgs"
        )


@allure.step("Закрепление сообщения случайным юзером в личке")
def random_pin_in_dialog(two_accounts, msgs_to_pin, pinned_msgs):
    chat_type = "private"
    to_pin_msg = msgs_to_pin.pop(random.randint(0, len(msgs_to_pin) - 1))
    user_to_pin_idx = random.randint(0, 1)
    response = two_accounts[user_to_pin_idx].rapi_pinMessage(
        sn=two_accounts[1 - user_to_pin_idx].uin,
        msgId=to_pin_msg,
    )
    assert response["status"]["code"] == 20000, (
        f"Message {to_pin_msg} pin failed in {chat_type}! Already pinned {len(pinned_msgs)} msgs"
    )
    bisect.insort(pinned_msgs, to_pin_msg)


@allure.step("Проверка закрепления сообщений случайным юзером в личке")
def random_check_multipin_in_dialog(
    two_accounts, expected_msgs, prev_patch_version: Optional[str] = None, check_patch_update=False
):
    user_to_check_idx = random.randint(0, 1)
    with allure.step("Проверяем, что в getHistory обновленный отсортированный массив запиненных сообщений"):
        return check_multipins(
            two_accounts[user_to_check_idx],
            two_accounts[1 - user_to_check_idx].uin,
            expected_msgs,
            prev_patch_version,
            check_patch_update,
        )


@allure.step("Закрепление сообщения случайным юзером в чате / канале")
def random_pin_in_chat(accounts, chat, chat_type, msgs_to_pin, pinned_msgs):
    is_channel = chat_type == "channel"
    to_pin_msg = msgs_to_pin.pop(random.randint(0, len(msgs_to_pin) - 1))
    user_to_pin_idx = 0 if is_channel else random.randint(0, 2)
    response = accounts[user_to_pin_idx].rapi_pinMessage(
        sn=chat,
        msgId=to_pin_msg,
    )
    assert response["status"]["code"] == 20000, (
        f"Message {to_pin_msg} pin failed in {chat_type}! Already pinned {len(pinned_msgs)} msgs"
    )
    bisect.insort(pinned_msgs, to_pin_msg)


@allure.step("Проверка закрепления сообщений случайным юзером в чате / канале")
def random_check_multipin_in_chat(
    accounts, chat, chat_type, pinned_msgs, prev_patch_version: Optional[str] = None, check_patch_update=False
):
    is_channel = chat_type == "channel"
    user_to_check_idx = random.randint(1 if is_channel else 0, 2)
    with allure.step("Проверяем, что в getHistory отсортированный массив запиненных сообщений после"):
        return check_multipins(accounts[user_to_check_idx], chat, pinned_msgs, prev_patch_version, check_patch_update)
