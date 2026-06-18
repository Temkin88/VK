import allure
import pytest

from pyvkteamsclient.client import UserMustJoinByLinkException
from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS
from support.markers import PRODUCT_FUNCTIONALITY
from support.product_functionality import ProductFunctionality


pytestmark = [PRODUCT_FUNCTIONALITY(ProductFunctionality.CONTACTS)]


@allure.id("79654")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Чаты")
@allure.feature("Участники чата")
@allure.title("Отмена приглашения на вступление в чат")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_cancel_user_invitations(
    auth_account,
    opponent_account,
    third_account,
    chat_type,
):
    with allure.step("Создаем группу"):
        chat_id = auth_account.create_chat(
            name=f"[{auth_account.getReqId()}] Test group",
            members=[opponent_account],
            defaultRole="member" if chat_type == "group" else "readonly",
        )

        auth_account.rapi_modChatMember(
            sn=chat_id,
            memberSn=opponent_account.uin,
            role="member",
        )

    with allure.step("Пробуем добавиться в чат"), pytest.raises(UserMustJoinByLinkException):
        opponent_account.rapi_group_members_add(
            sn=chat_id,
            members=[third_account.uin],
        )

    with allure.step("Проверяем что сотрудник попал в список премодерации и не добавился в чат"):
        response = auth_account.rapi_getChatInfo(sn=chat_id)
        assert third_account.uin not in [x["sn"] for x in response["results"]["members"]], (
            f'{auth_account.env}:User added by "rapi/joinChat" without premoderation'
        )

        response = auth_account.rapi_getChatMembers(
            _id=chat_id,
            filter_role="pending",
        )
        assert third_account.uin in [x["sn"] for x in response["results"]["members"]], (
            f"{auth_account.env}:User not mentioned as pending"
        )

    with allure.step("Отменяем запрос на добавление сотрудника в чат"):
        opponent_account.rapi_group_invitations_cancel(sn=third_account.uin, chatId=chat_id)

    with allure.step("Проверяем что сотрудник добавился в чат"):
        response = auth_account.rapi_getChatInfo(sn=chat_id)
        assert third_account.uin not in [x["sn"] for x in response["results"]["members"]], (
            f"{auth_account.env}:User not added by resolving premoderation"
        )

        response = auth_account.rapi_getChatMembers(
            _id=chat_id,
            filter_role="pending",
        )
        assert third_account.uin not in [x["sn"] for x in response["results"]["members"]], (
            f"{auth_account.env}:User mentioned as pending"
        )
