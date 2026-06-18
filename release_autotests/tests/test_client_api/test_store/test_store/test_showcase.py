import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@allure.id("30148")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Стикеры")
@allure.feature("Информация о стикерах")
@allure.title("Получение витрины стикеров")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.STORE_SHOWCASE
def test_store_showcase(
    auth_account,
):
    with allure.step("Получаем список стикер паков"):
        response = auth_account.store_showcase()

    with allure.step("Проверяем наличие базовых стикеров"):
        assert response["result"]["showcase"], "Sticker packs not found"

        for pack in filter(
            lambda x: x["title"] == "Seal",
            response["result"]["showcase"],
        ):
            assert pack["stickers_count"] == 35, 'Wrong stickers count in "Seal" pack'

            assert pack["type"] == "image", 'Wrong type for "Seal" pack'


@pytest.fixture
def sticker_pack(
    auth_account,
):
    with allure.step("Получаем список стикер паков"):
        response = auth_account.store_showcase()

    if not response["result"]["showcase"]:
        pytest.skip("There is not sticker packs found")

    else:
        return response["result"]["showcase"][1]


@pytest.fixture
def sticker_pack_title(
    sticker_pack,
):
    return sticker_pack["title"]


@pytest.fixture
def sticker_pack_stickers_count(
    sticker_pack,
):
    return sticker_pack["stickers_count"]


@pytest.fixture
def sticker_pack_type(
    sticker_pack,
):
    return sticker_pack["type"]


@allure.id("30147")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Стикеры")
@allure.feature("Информация о стикерах")
@allure.title("Поиск по витрине стикеров")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.STORE_SHOWCASE
def test_store_showcase_search(
    auth_account,
    sticker_pack_title,
    sticker_pack_stickers_count,
    sticker_pack_type,
):
    with allure.step("Получаем список стикер паков"):
        response = auth_account.store_showcase_search(search=sticker_pack_title)

    with allure.step("Проверяем наличие базовых стикеров"):
        assert response["result"]["showcase"], f"Sticker pack '{sticker_pack_title}' not found"

        for pack in filter(
            lambda x: x["title"] == sticker_pack_title,
            response["result"]["showcase"],
        ):
            assert pack["stickers_count"] == sticker_pack_stickers_count, (
                f'Wrong stickers count in "{sticker_pack_title}" pack'
            )

            assert pack["type"] == sticker_pack_type, f'Wrong type for "{sticker_pack_title}" pack'
