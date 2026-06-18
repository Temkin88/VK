import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("38600")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Файлы")
@allure.feature("Превью файлов")
@allure.title("Получение превью стикера по ID")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "preview_size",
    [
        "preview_large",
        "preview_medium",
        "preview_small",
        "listicon_large",
        "listicon_medium",
        "sticker_xxlarge",
        "sticker_xlarge",
        "sticker_large",
        "sticker_medium",
        "sticker_small",
        "icon_large",
        "icon_medium",
        "icon_small",
        "stickerpicker_large",
        "stickerpicker_medium",
        "stickerpicker_small",
        "stickerpicker_xsmall",
    ],
)
def test_files_preview_sticker(
    auth_account,
    opponent_account,
    get_sticker_id,
    preview_size,
):
    with allure.step("Делаем запрос превью стикера"):
        opponent_account.files_preview_sticker(
            file_id=get_sticker_id,
            size=preview_size,
        )


@allure.id("38602")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Файлы")
@allure.feature("Превью файлов")
@allure.title("Получение превью лотти по ID")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "preview_size",
    [
        "preview_large",
        "preview_medium",
        "preview_small",
        "listicon_large",
        "listicon_medium",
        "sticker_xxlarge",
        "sticker_xlarge",
        "sticker_large",
        "sticker_medium",
        "sticker_small",
        "icon_large",
        "icon_medium",
        "icon_small",
        "stickerpicker_large",
        "stickerpicker_medium",
        "stickerpicker_small",
        "stickerpicker_xsmall",
    ],
)
def test_files_preview_lottie(
    opponent_account,
    get_lottie_id,
    preview_size,
):
    with allure.step("Делаем запрос превью стикера"):
        opponent_account.store_lottie_preview(
            file_id=get_lottie_id,
            size=preview_size,
        )
