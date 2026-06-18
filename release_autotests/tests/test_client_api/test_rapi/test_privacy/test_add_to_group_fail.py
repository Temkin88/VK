import allure
import pytest

from pyvkteamsclient.client import UserMustJoinByLinkException
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@pytest.fixture(scope="module", autouse=True)
def wipe_privacy_settings(auth_account):
    yield

    auth_account.rapi_updatePrivacySettings("groups", "everybody")


@allure.id("30200")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Настройки приватности")
@allure.feature("Изменение настроек приватности")
@allure.title(
    "Ошибка добавления пользователя в группу из-за настроек приватности",
)
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("role", ["readonly", "member"])
def test_add_to_group_fail(
    auth_account,
    opponent_account,
    role,
    fetch_until_empty_answer,
):
    """
    Проверяем изменение настроек приватности
    """
    with allure.step("Изменяем настройки приватности"):
        auth_account.rapi_updatePrivacySettings("groups", "nobody")

    with allure.step("Проверяем что пользователя не получиться добавить в группу"):
        chat_id = opponent_account.create_chat(
            "test_add_to_group_fail",
            members=[auth_account],
            defaultRole=role,
            check_members=False,
        )

        response = opponent_account.rapi_getChatInfo(
            sn=chat_id,
        )

        assert auth_account.uin not in [x["sn"] for x in response["results"]["persons"]], (
            f"{auth_account.env}:Private account happened to be in chat members list"
        )


@allure.id("30201")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Настройки приватности")
@allure.feature("Изменение настроек приватности")
@allure.title(
    "Ошибка добавления пользователя в уже созданную группу из-за настроек приватности",
)
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("role", ["readonly", "member"])
def test_add_to_existing_group_fail(
    auth_account,
    opponent_account,
    role,
):
    """
    Проверяем изменение настроек приватности
    """
    with allure.step("Изменяем настройки приватности"):
        auth_account.rapi_updatePrivacySettings("groups", "nobody")

    with allure.step("Создаем тестовый чат"):
        chat_id = opponent_account.create_chat(
            "test_add_to_group_fail",
            members=[opponent_account],
            defaultRole=role,
            joinModeration=False,
        )

    with allure.step("Пробуем добавить пользователя в группу"), pytest.raises(UserMustJoinByLinkException):
        opponent_account.rapi_group_members_add(
            sn=chat_id,
            members=[auth_account.uin],
        )
