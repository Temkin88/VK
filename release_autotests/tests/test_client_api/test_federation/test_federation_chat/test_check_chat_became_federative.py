import allure
import pytest

from support.markers import SANDBOX
from tests.test_client_api.test_federation.common import generate_uniq_chat_name, find_chat_by_some_criterion


@allure.id("1434610")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Группы")
@allure.feature("Поиск федеративных групповых чатов")
@allure.title("Наличие признака федеративности у группового чата")
@SANDBOX
@pytest.mark.parametrize(
    "defaultRole",
    [
        "member",
        "readonly",
    ],
)
@pytest.mark.parametrize(
    ("chat_creator", "chat_member", "chat_additional_member"),
    [
        ("fed_acc_on_host1_host2", "fed_acc_on_host2_host1", "none"),
        ("fed_acc_on_host1_host2", "none", "fed_acc_on_host2_host1"),
    ],
)
def test_check_chat_became_federative(
    request, defaultRole, chat_creator, chat_member, chat_additional_member, fetch_until_empty_answer_with_filter
):
    chat_creator = request.getfixturevalue(chat_creator)
    members_uins = [chat_creator.uin]
    friendly_name = "Test_chat"
    chat_name = generate_uniq_chat_name(friendly_name)
    if chat_member != "none":
        chat_member = request.getfixturevalue(chat_member)
        members_uins.append(chat_member.uin)
    with allure.step(f"Создаем чат {friendly_name}"):
        response = chat_creator.post(
            "rapi/createChat",
            headers={"Content-Type": "application/json"},
            json={
                "aimsid": chat_creator.aimsid,
                "reqId": chat_creator.getReqId(),
                "params": {
                    "name": chat_name,
                    "members": [{"sn": member} for member in members_uins],
                    "joinModeration": False,
                    "defaultRole": defaultRole,
                },
            },
        )

        local_chat_sn = response["results"]["sn"]
        assert response["status"]["code"] == 20000, "Не удалось создать чат"
        chat_creator.rapi_modChat(sn=local_chat_sn, public=True)
        if chat_member == "none":
            with allure.step("Проверяем что созданный чат не является федеративным"):
                assert find_chat_by_some_criterion(chat_creator, chat_name, {"isFederation": False}) is not None
    additional_members_uins = []
    if chat_additional_member != "none":
        chat_additional_member = request.getfixturevalue(chat_additional_member)
        additional_members_uins.append(chat_additional_member.uin)
        with allure.step(f"Добавляем в чат {friendly_name} федеративных пользователей {additional_members_uins}"):
            response = chat_creator.rapi_group_members_add(sn=local_chat_sn, members=additional_members_uins)
            assert response["status"]["code"] == 20000, "Не удалось добавить в чат пользователей"
    with allure.step("Проверяем что чат является федеративным в поиске"):
        assert find_chat_by_some_criterion(chat_creator, chat_name, {"isFederation": True}) is not None
