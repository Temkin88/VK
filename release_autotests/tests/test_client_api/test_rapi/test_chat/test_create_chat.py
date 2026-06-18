import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("28157")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Создание и редактирование чата")
@allure.title("Создание чата")
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
def test_create_chat(
    request,
    with_avatar,
    with_rules,
    with_description,
    is_public,
    is_join_moderation,
    chat_type,
    auth_account,
    photo_id,
):
    """
    Проверяем создание и редактирование чата
    """

    if with_avatar:
        with allure.step("Предзагружаем аватар"):
            avatar_id = photo_id

    else:
        with allure.step("Ставим пустой ID аватара"):
            avatar_id = ""

    with allure.step("Пробуем создать тестовый чат"):
        name = f"Test {chat_type} - {request.node.name}"
        about = "Test description" if with_description else ""
        rules = "Test rules" if with_rules else ""
        public = is_public
        join_moderation = is_join_moderation
        default_role = "member" if chat_type == "group" else "readonly"

        chat_id = auth_account.create_chat(
            name=name,
            avatarId=avatar_id,
            members=[],
            about=about,
            rules=rules,
            public=public,
            joinModeration=join_moderation,
            defaultRole=default_role,
        )

        assert chat_id, "Failed to create chat"
