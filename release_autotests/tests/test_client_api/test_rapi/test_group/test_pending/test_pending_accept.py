import allure
import pytest

from support.markers import VKTI, PRE_VKTI, TARM, PRE_TARM, SAAS, SANDBOX, PRE_SAAS


@allure.id("79650")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Чаты")
@allure.feature("Участники чата")
@allure.title("Премодерация вступления в чат")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_get_and_resolve_pending_users(
    auth_account,
    opponent_account,
    chat_type,
):
    with allure.step("Создаем группу"):
        chat_id = auth_account.create_chat(
            name=f"[{auth_account.getReqId()}] Test group",
            members=[],
            defaultRole="member" if chat_type == "group" else "readonly",
        )
        stamp = auth_account.get_chat_stamp(chat_id)

    with allure.step("Пробуем добавиться в чат"):
        opponent_account.rapi_joinChat(stamp)

    with allure.step("Проверяем что сотрудник попал в список премодерации и не добавился в чат"):
        response = auth_account.rapi_getChatInfo(sn=chat_id)
        assert opponent_account.uin not in [x["sn"] for x in response["results"]["members"]], (
            f'{auth_account.env}:User added by "rapi/joinChat" without premoderation'
        )

        response = auth_account.rapi_getChatMembers(
            _id=chat_id,
            filter_role="pending",
        )
        result_members = response["results"]["members"]

        assert opponent_account.uin in [x["sn"] for x in result_members], (
            f"{auth_account.env}:User not mentioned as pending"
        )
        assert all(lastseen["userState"]["lastseen"] >= 0 for lastseen in result_members), "Lastseen invalid"

    with allure.step("Подтверждаем добавление сотрудника в чат"):
        auth_account.rapi_group_pending_accept(
            sn=chat_id,
            members=[opponent_account.uin],
        )

    with allure.step("Проверяем что сотрудник добавился в чат"):
        response = auth_account.rapi_getChatInfo(sn=chat_id)
        result_members = response["results"]["members"]
        assert opponent_account.uin in [x["sn"] for x in result_members], (
            f"{auth_account.env}:User not added by resolving premoderation"
        )
        assert all(lastseen["userState"]["lastseen"] >= 0 for lastseen in result_members), "Lastseen invalid"

        response = auth_account.rapi_getChatMembers(
            _id=chat_id,
            filter_role="pending",
        )
        result_members = response["results"]["members"]

        assert opponent_account.uin not in [x["sn"] for x in result_members], (
            f"{auth_account.env}:User mentioned as pending"
        )
        assert all(lastseen["userState"]["lastseen"] >= 0 for lastseen in result_members), "Lastseen invalid"
