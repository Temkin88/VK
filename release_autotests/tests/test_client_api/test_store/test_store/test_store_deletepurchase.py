import allure
import pytest

from support.markers import VKTI, SAAS, TARM, PRE_VKTI, PRE_TARM, SANDBOX, PRE_SAAS


@pytest.fixture
def not_added_sticker_pack(auth_account):
    not_added_sticker_pack = next(
        filter(
            lambda x: not x["is_added"],
            auth_account.store_showcase()["result"]["showcase"],
        ),
    )

    auth_account.store_buy_free(
        store_id=not_added_sticker_pack["store_id"],
    )

    return not_added_sticker_pack


@allure.id("30146")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite("Стикеры")
@allure.feature("Действия со стикерпаками")
@allure.title("Удаление стикерпака")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
def test_store_deletepurchase(
    auth_account,
    not_added_sticker_pack,
):
    with allure.step("Пытаемся удалить стикер пак"):
        auth_account.store_deletepurchase(
            product_id=not_added_sticker_pack["id"],
        )
