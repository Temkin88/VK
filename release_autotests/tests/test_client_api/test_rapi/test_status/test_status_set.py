import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("26924")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite("Статусы")
@allure.feature("Установка статуса")
@allure.title("Установка статуса")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "smile",
    [
        "👀",
        "🖖️",
        "🤐",
        "🤡",
        "😼",
        "🥳",
        # "🤝", "👹️", "🥸", "🤒", "🤠", "👻",
        # "👍", "❤️", "🤣", "😳", "😢", "😡"
    ],
)
@pytest.mark.parametrize(
    "status_text",
    [
        "Working!!!",
        "Roar",
    ],
)
@pytest.mark.parametrize(
    "duration",
    [
        60,
        # 3600,
        # 10800,
        32400,
    ],
)
@pytest.mark.parametrize("is_reply", [True, False], ids=["reply", "not_reply"])
def test_set_and_remove_status(
    smile,
    status_text,
    duration,
    is_reply,
    auth_account,
    opponent_account,
):
    """
    Установка и удаление статуса
    """
    with allure.step("Пытаемся установить статус"):
        if is_reply:
            auth_account.rapi_status_set(
                _type="emoji",
                media=smile,
                text=status_text,
                duration=duration,
                reply_sn=opponent_account.uin,
                reply_type="emoji",
                reply_media=smile,
                reply_text=status_text,
            )
        else:
            auth_account.rapi_status_set(
                _type="emoji",
                media=smile,
                text=status_text,
                duration=duration,
            )

    with allure.step("Пытаемся удалить статус"):
        auth_account.rapi_status_set(
            _type="empty",
        )
