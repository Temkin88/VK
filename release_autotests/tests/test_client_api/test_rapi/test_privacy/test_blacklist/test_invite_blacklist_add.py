import allure
import pytest

from pyvkteamsclient.client import UserMustJoinByLinkException
from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("79709")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Настройки приватности")
@allure.feature("Черный список")
@allure.title("Добавление в черный список")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_add_invite_blacklist(
    prepare_test_chats,
    add_invite_blacklist,
):
    """
    Добавление в черный список
    """

    main_acc, opponent, _, _ = prepare_test_chats

    uins_list = [
        "1000000001",
        "1000000002",
        opponent.uin,
    ]

    with allure.step("Добавляем uin в черный список"):
        add_invite_blacklist(account=main_acc, users_list=uins_list)

    with allure.step("Проверяем что uin появились в черном списке"):
        response = main_acc.rapi_privacy_groups_inviteBlacklist_get(10)
        assert all(uin in response["results"]["blacklist"] for uin in uins_list), "Uin not in blacklist"


@allure.id("79753")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Настройки приватности")
@allure.feature("Черный список")
@allure.title("Проверяем что нельзя добавить позователя который в черном списке в группу")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_cannot_add_in_group_users_is_invite_blacklist(
    prepare_test_chats,
    add_invite_blacklist,
):
    """
    Добавление в черный список и проверяем что аккаунт который добавлен в black list не может добавить в группу
    """

    main_acc, opponent, _, _ = prepare_test_chats

    uins_list = [
        opponent.uin,
    ]

    with allure.step("Создаем тестовый чат"):
        chat_id = opponent.create_chat(
            name="Test group for adding member",
            defaultRole="member",
        )

    with allure.step("Проверяем что только создатель присутствует в группе"):
        after_black_list = opponent.rapi_getChatInfo(sn=chat_id)
        assert len(after_black_list["results"]["members"]) == 1, "Count uin in group not equal 1"
        assert opponent.uin in [uin["sn"] for uin in after_black_list["results"]["members"]], "opponent in group"

    with allure.step("Добавляем uin в черный список"):
        add_invite_blacklist(account=main_acc, users_list=uins_list)

    with allure.step("Проверяем что uin появились в черном списке"):
        response = main_acc.rapi_privacy_groups_inviteBlacklist_get(10)
        assert all(uin in response["results"]["blacklist"] for uin in uins_list), "Uin not in blacklist"

    with (
        allure.step("Пробуем добавить пользователя который в black list в группу"),
        pytest.raises(UserMustJoinByLinkException),
    ):
        opponent.rapi_group_members_add(
            sn=chat_id,
            members=[main_acc.uin],
        )

    with allure.step("Проверяем что uin не добавился в группу"):
        before_black_list = opponent.rapi_getChatInfo(sn=chat_id)
        assert main_acc.uin not in [uin["sn"] for uin in before_black_list["results"]["members"]], "main_acc in group"
