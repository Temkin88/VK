import allure
import pytest


@pytest.fixture(
    scope="session",
    params=["image", "animated"],
)
def get_sticker_id(auth_account, request):
    with allure.step("Получаем список стикер паков"):
        response = auth_account.store_showcase()

    with allure.step("Ищем нужный тип стикерпака"):
        sticker_packs = list(
            filter(
                lambda x: x["type"] == request.param,
                response["result"]["showcase"],
            )
        )

        if len(sticker_packs) == 0:
            pytest.skip(f'Sticker pack with type "{request.param}" not found')

    with allure.step("Получаем file_id стикера"):
        yield sticker_packs[0]["main_sticker"]


@pytest.fixture(
    scope="session",
)
def get_lottie_id(auth_account):
    with allure.step("Получаем список стикер паков"):
        response = auth_account.store_showcase()

    with allure.step("Ищем нужный тип стикерпака"):
        sticker_packs = list(
            filter(
                lambda x: x["type"] == "animated",
                response["result"]["showcase"],
            )
        )

        if len(sticker_packs) == 0:
            pytest.skip('Sticker pack with type "animated" not found')

    with allure.step("Получаем file_id стикера"):
        yield sticker_packs[0]["main_sticker"]
