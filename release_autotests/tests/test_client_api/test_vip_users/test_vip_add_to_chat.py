import allure
import pytest

from pyvkteamsclient.client import UserMustJoinByLinkException
from support.markers import TARM, PRE_TARM


@allure.id("33215")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("VIP")
@allure.feature("Действия со стороны обычного пользователя")
@allure.title(
    "Добавление VIP пользователей в группы",
)
@TARM
@PRE_TARM
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_add_to_chat_vip(
    chat_type,
    prepare_test_chats,
    vip_one,
    vip_two,
):
    user, opponent, group, channel = prepare_test_chats

    chat = group if chat_type == "group" else channel

    with allure.step("Пытаемся добавить VIP1 в чат"), pytest.raises(UserMustJoinByLinkException):
        user.rapi_group_members_add(
            sn=chat,
            members=[opponent.uin, vip_one.uin, vip_two.uin],
        )
