import allure
import pytest

from support.cases.drafts import draft_parts
from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26909")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Черновик")
@allure.feature("Черновик в чате")
@allure.title("Сохранение черновика в чате")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "chat_type",
    ["private", "group", "channel"],
)
@pytest.mark.parametrize(
    "draft_part",
    draft_parts,
    ids=[
        "text",
        "text_with_quote",
        "formatted_text",
        "formatted_text_with_quote",
    ],
)
def test_save_disabled_draft_in_chat(
    chat_type, draft_part, prepare_test_chats, fetch_until_empty_answer_with_filter, is_draft_enabled
):
    """
    Проверяем успешность выполнения запроса при октлюченном функциоале
    """

    if is_draft_enabled:
        pytest.skip("Drafts are enabled  in myteam-config")

    main_acc, opponent, group, channel = prepare_test_chats

    if chat_type == "private":
        chat = opponent.uin
    elif chat_type == "group":
        chat = group
    else:
        chat = channel

    with allure.step("Сохраняем черновик в чате"):
        assert (
            main_acc.rapi_draft_set(
                sn=chat,
                parts=draft_part,
            )["status"]["code"]
            == 20000
        )

    with allure.step("Ждем и проверяем отсутствие эвента"):
        even_found = False

        for _ in fetch_until_empty_answer_with_filter(main_acc, "draft"):
            even_found = True

        assert not even_found, "пришел эвент при отключенном черновике"
