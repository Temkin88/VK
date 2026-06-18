import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("67051")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Получить список пользователей в чате с пагинацией.")
@allure.title("Получение списка участников чата")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.parametrize("filter_role", ["admins", "members"])
def test_chat_members(
    request,
    chat_type,
    filter_role,
    prepare_test_chats,
):
    """
    Получить список пользователей в чате с пагинацией.
    """
    main_acc, opponent, group, channel = prepare_test_chats

    with allure.step("Создаем чат"):
        name = f"Test {chat_type} - {request.node.name}"
        default_role = "member" if chat_type == "group" else "readonly"

        chat_id = main_acc.create_chat(
            name=name,
            joinModeration=False,
            defaultRole=default_role,
        )

    with allure.step("Присоеденяемся к чату"):
        chat_info_before_join = main_acc.rapi_getChatInfo(sn=chat_id, memberLimit=10)
        chat_stamp = chat_info_before_join["results"]["stamp"]
        opponent.rapi_joinChat(stamp=chat_stamp)

    with allure.step("Пробуем получить участников чата"):
        response = main_acc.rapi_getChatMembers(
            _id=chat_id,
            filter_role=filter_role,
        )

        assert response["status"]["code"] == 20000, "Response code error"
        assert response["results"]["sn"] == chat_id

    with allure.step("Проверяем фильтрацию участников чата"):
        if filter_role == "admins":
            event_admins = response["results"]["members"]
            assert all(event["role"] == "admin" for event in event_admins), "Role admin not listed as members"
            assert all(event["sn"] == main_acc.uin for event in event_admins), "Dont match account uin"
        else:
            event_members = [event for event in response["results"]["members"] if event["role"] != "admin"]
            assert all(event["role"] == default_role for event in event_members), (
                f"Role {default_role} not listed as members"
            )
            assert all(event["sn"] == opponent.uin for event in event_members), "Dont match account uin"
