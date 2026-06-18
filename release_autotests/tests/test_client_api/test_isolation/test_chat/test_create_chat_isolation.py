import allure
import pytest

from support.markers import SAAS, ISOLATION


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Создание и редактирование чата")
@allure.title("Создание чата")
@ISOLATION
@SAAS
@pytest.mark.parametrize(
    ("with_avatar", "with_description", "with_rules", "is_public", "is_join_moderation"),
    [
        (False, False, False, False, True),
        (True, True, True, False, True),
        (True, False, False, False, True),
    ],
)
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_create_chat_isolation(
    request,
    with_avatar,
    with_rules,
    with_description,
    is_public,
    is_join_moderation,
    chat_type,
    first_auth_account_in_tenant,
    second_auth_account_in_tenant,
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

    with allure.step("Пробуем создать тестовый чат с пользователем из одного тенанта"):
        name = f"Test {chat_type} - {request.node.name}"
        about = "Test description" if with_description else ""
        rules = "Test rules" if with_rules else ""
        public = is_public
        join_moderation = is_join_moderation
        default_role = "member" if chat_type == "group" else "readonly"

        chat_id = first_auth_account_in_tenant.create_chat(
            name=name,
            avatarId=avatar_id,
            members=[second_auth_account_in_tenant],
            about=about,
            rules=rules,
            public=public,
            joinModeration=join_moderation,
            defaultRole=default_role,
        )

        assert chat_id, "Failed to create chat"


@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Создание и редактирование чата")
@allure.title("Создание чата")
@ISOLATION
@SAAS
@pytest.mark.parametrize(
    ("with_avatar", "with_description", "with_rules", "is_public", "is_join_moderation"),
    [
        (False, False, False, False, True),
        (True, True, True, False, True),
        (True, False, False, False, True),
    ],
)
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_create_chat_isolation_not_in_tenant(
    request,
    with_avatar,
    with_rules,
    with_description,
    is_public,
    is_join_moderation,
    chat_type,
    first_auth_account_not_in_tenant,
    first_auth_account_in_tenant,
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

    with allure.step("Пробуем создать тестовый чат  пользователем не из тенанта"), pytest.raises(Exception):
        name = f"Test {chat_type} - {request.node.name}"
        about = "Test description" if with_description else ""
        rules = "Test rules" if with_rules else ""
        public = is_public
        join_moderation = is_join_moderation
        default_role = "member" if chat_type == "group" else "readonly"

        first_auth_account_not_in_tenant.create_chat(
            name=name,
            avatarId=avatar_id,
            members=[first_auth_account_in_tenant],
            about=about,
            rules=rules,
            public=public,
            joinModeration=join_moderation,
            defaultRole=default_role,
        )
