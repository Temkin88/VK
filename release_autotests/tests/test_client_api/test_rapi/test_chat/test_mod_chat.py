import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("28155")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Создание и редактирование чата")
@allure.title("Редактирование чата")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    ("with_avatar", "with_description", "with_rules", "is_public", "is_join_moderation"),
    [
        (False, False, False, False, True),
        (True, True, True, False, True),
        (True, False, False, False, True),
    ],
)
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_edit_chat(
    request,
    with_avatar,
    with_rules,
    with_description,
    is_public,
    is_join_moderation,
    chat_type,
    auth_account,
    prepare_test_chats,
):
    """
    Проверяем создание и редактирование чата
    """

    _, _, group, channel = prepare_test_chats

    if chat_type == "group":
        chat_id = group
        default_role = "member"
    else:
        chat_id = channel
        default_role = "readonly"

    with allure.step("Пробуем редактировать тестовый чат"):
        name = f"Modded {chat_type} - {request.node.name}"
        about = "Modded description"
        rules = "Modded rules"
        public = not is_public
        join_moderation = not is_join_moderation

        assert auth_account.mod_chat(
            sn=chat_id,
            name=name,
            about=about,
            rules=rules,
            public=public,
            joinModeration=join_moderation,
        )["status"]["code"]

        chat_info = auth_account.rapi_getChatInfo(sn=chat_id)["results"]

        assert chat_info["creator"] == auth_account.uin, f"Creator is'nt {auth_account.uin}"

        assert chat_info["defaultRole"] == default_role

        assert chat_info["members"]

        assert chat_info.get("about", "") == about

        assert chat_info.get("rules", "") == rules
