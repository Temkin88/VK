import uuid

import allure
import pytest

from support.markers import PRE_TARM, VKTI, PRE_VKTI, SAAS, TARM, SANDBOX, PRE_SAAS


@allure.id("538387")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Получение аватара пользователя или чата")
@allure.title("Получение аватара пользователя или чата")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
def test_avatar_get(chat_type, auth_account, photo_id, survey_miniapp):
    """
    Получение аватара чата
    """

    with allure.step("Пробуем создать тестовый чат"):
        default_role = "member" if chat_type == "group" else "readonly"

        chat_id = auth_account.create_chat(
            name=f"Test chat {uuid.uuid4().hex}",
            avatarId=photo_id,
            members=[],
            about="Test description",
            rules="Test rules",
            public=False,
            joinModeration=False,
            defaultRole=default_role,
        )

        assert chat_id, "Failed to create chat"

    with allure.step("Пробуем получить аватар чата"):
        response = survey_miniapp.internal_avatar_get(size="64", target_sn=chat_id)

        assert response.status_code == 200, "Response error code"
        assert response.content, "Content null"
        assert "PNG" in response.text, "PNG not in text"
