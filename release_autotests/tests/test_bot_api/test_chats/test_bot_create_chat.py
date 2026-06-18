import allure
import pytest

from support.markers import SANDBOX


@allure.id("508461")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Боты")
@allure.feature("Кастомные боты")
@allure.title("Создание чата через Bot API")
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_bot_create_chat(
    bot_class,
    auth_account,
    opponent_account,
    chat_type,
):
    with allure.step("Создаем группу"):
        chat_id = bot_class.create_chat(
            name=f"[{bot_class.uin}] Test group",
            members=[auth_account.uin],
            default_role="member" if chat_type == "group" else "readonly",
        ).json()["sn"]

    with allure.step("Проверяем что сотрудник добавился"):
        response = auth_account.rapi_getChatInfo(sn=chat_id)
        result = response["results"]

        member_list = [x["sn"] for x in result["members"]]

        assert chat_id == result["sn"], f"{chat_id} dont matched"
        assert auth_account.uin in member_list, f"{auth_account.env}:Failed to add user to group with Bot API"
        assert bot_class.uin in member_list, f"{auth_account.env}:Failed to add user to group with Bot API"
