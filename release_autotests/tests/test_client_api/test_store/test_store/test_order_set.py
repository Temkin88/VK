import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@pytest.fixture
def fill_my_sticker_list(auth_account):
    sticker_packs = auth_account.store_my()["result"]["sticker_packs"]

    is_to_fill = not sticker_packs

    if is_to_fill:
        showcase = auth_account.store_showcase()["result"]["showcase"]

        for pack in showcase[:5]:
            auth_account.store_buy_free(
                store_id=pack["store_id"],
            )

    yield

    if is_to_fill:
        sticker_packs = auth_account.store_my()["result"]["sticker_packs"]

        for pack in sticker_packs:
            auth_account.store_deletepurchase(
                product_id=pack["id"],
            )


@allure.id("30150")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Стикеры")
@allure.feature("Действия со стикерпаками")
@allure.title("Изменения порядка стикерпаков в витрине")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_store_order_set(
    auth_account,
    fill_my_sticker_list,
):
    with allure.step("Получаем список стикер паков"):
        sticker_packs = auth_account.store_my()["result"]["sticker_packs"]

        current_order = [x["id"] for x in sticker_packs]

        reversed_list = list(reversed(sticker_packs))

        new_priority = {f"priority[{case['id']}]": str(i + 1) for i, case in enumerate(reversed_list)}
    with allure.step("Делаем запрос на изменение порядка"):
        auth_account.store_order_set(new_priority)

    with allure.step("Получаем список стикер паков"):
        sticker_packs = auth_account.store_my()["result"]["sticker_packs"]

        new_order = [x["id"] for x in sticker_packs]

        assert list(reversed(current_order)) == new_order, "Wrong sticker packs order after request"
