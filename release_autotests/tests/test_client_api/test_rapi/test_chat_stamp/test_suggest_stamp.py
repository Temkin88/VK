import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("37338")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Чаты")
@allure.feature("Создание и редактирование чата")
@allure.title("Проверка саджестов stamp для чата")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize("chat_type", ["group", "channel"])
@pytest.mark.parametrize("is_public", [True, False], ids=["public", "private"])
def test_suggest_public_group_stamp(
    auth_account,
    prepare_test_chats,
    chat_type,
    is_public,
):
    _, _, group, channel = prepare_test_chats

    chat_id = group if chat_type == "group" else channel

    with allure.step(f"Пробуем получить предложение stamp для чата {chat_type}"):
        if is_public:
            response = auth_account.rapi_suggestPublicGroupStamp(
                sn=chat_id,
            )
        else:
            response = auth_account.rapi_suggestPrivateGroupStamp(
                sn=chat_id,
            )

        assert response.get("results", {}).get("stamp") or response["status"]["code"] == 20001, "No stamp suggested"
