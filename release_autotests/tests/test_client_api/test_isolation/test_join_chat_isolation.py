import allure
import pytest

from support.markers import SAAS, ISOLATION


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Вступить в группу или подписаться на канал")
@allure.title("Вступление в группу")
@ISOLATION
@SAAS
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_join_chat_isolation(
    request,
    chat_type,
    prepare_test_chats_msg_isolation,
):
    """
    Проверяем вступить в группу или подписаться на канал
    """
    main_acc, opponent, group, channel = prepare_test_chats_msg_isolation

    with allure.step("Создаем чат"):
        name = f"Test {chat_type} - {request.node.name}"
        default_role = "member" if chat_type == "group" else "readonly"

        chat_id = main_acc.create_chat(
            name=name,
            joinModeration=False,
            defaultRole=default_role,
        )

        chat_info_before_join = main_acc.rapi_getChatInfo(sn=chat_id, memberLimit=10)
        chat_stamp = chat_info_before_join["results"]["stamp"]

    with allure.step("Проверяем что в чате только один участник"):
        sn_count_before_join = len(chat_info_before_join["results"]["members"])
        assert sn_count_before_join == 1, "Count members not equal 1"

    with allure.step("Проверяем что в списке участников есть создатель чата"):
        name_sn_list_before_join = [sn["sn"] for sn in chat_info_before_join["results"]["members"]]
        assert main_acc.uin in name_sn_list_before_join, f"Creator not listed as chat member:creator-{main_acc.uin}"

    with allure.step("Пробуем присоединиться к чату через rapi/joinChat"):
        response = opponent.rapi_joinChat(stamp=chat_stamp)

        assert response["status"]["code"] == 20000, "Response code error"

    with allure.step("Проверяем что появился новый участник в списке участников чата"):
        chat_info_after_join = main_acc.rapi_getChatInfo(sn=chat_id, memberLimit=10)

        sn_count_after_join = len(chat_info_after_join["results"]["members"])

        assert sn_count_after_join > sn_count_before_join, "Count members equal 1"

        name_sn_list_after_join = [sn["sn"] for sn in chat_info_after_join["results"]["members"]]
        assert opponent.uin in name_sn_list_after_join, f"New member not listed as chat members:member-{opponent.uin}"
