import io
import os

import allure
import ujson as json

import pytest
from PIL import Image
from fastapi import FastAPI
from fastapi.testclient import TestClient

from web.main import app
from web.project.db import Account, init_db, Account_Pydantic, Product
from web.project.v1.product import ProductTypeEnum


@pytest.fixture(scope="session")
@allure.title("Выбора asyncio+uvloop для async функций")
def anyio_backend() -> tuple[str, dict[str, bool]]:
    """
    Выбора asyncio+uvloop для async функций
    """
    return 'asyncio', {'use_uvloop': True}


@pytest.fixture(scope="session")
@allure.title("Получение app: FastAPI()")
def get_app() -> FastAPI:
    """
    Получение экземпляра приложения app из web.main
    """
    yield app


@pytest.fixture(scope="session")
@allure.title("Получение app: FastAPI()")
def client(get_app: FastAPI) -> TestClient:
    """
    Получение экземпляра приложения app из web.main
    """
    yield TestClient(get_app)


@pytest.fixture(autouse=True, scope="session")
@allure.title("Загрузка базы данных")
async def populate_db():
    """
    Загрузка базы данных
    """
    with allure.step("Bнициализируем базу данных"):
        await init_db()

    with allure.step("Сохраняем аккаунты из базы в accounts-backup.json"):
        with open("accounts-backup.json", "w") as f:
            accounts_json = []
            async for account_model in Account.all():
                accounts_json.append(
                    (await Account_Pydantic.from_tortoise_orm(
                        account_model)).dict()
                )
            json.dump(accounts_json, f, indent=4)

    with allure.step("Заливаем в базу аккаунты из accounts.json"):
        with open("accounts.json", "rb") as f:
            accounts = json.load(f)
        await Account.filter().delete()
        await Account.bulk_create([
            Account(**account) for account in accounts
        ])

    with allure.step("Чистим базу от продуктов"):
        await Product.filter().delete()

    with allure.step("Подливаем новые продукты"):
        await Product.bulk_create([
            Product(
                name=product,
                status=True if product != ProductTypeEnum.armgs else False
            ) for product in ProductTypeEnum
        ])

    yield

    with allure.step("Чистим базу от аккаунтов"):
        await Account.filter().delete()

    with allure.step("Восстанавливаем базу из accounts-backup.json"):
        with open("accounts-backup.json", "r") as f:
            accounts_json = json.load(f)

        await Account.bulk_create(
            Account(**account) for account in accounts_json
        )


@pytest.fixture(scope="module")
@allure.title("Получение байтов скриншота test.png")
def get_test_image_bytes() -> bytes:
    """
    Получение байтов скриншота test.png
    """
    with open(os.path.join('tests', 'support', 'test.png'), 'rb') as f:
        yield f.read()


@pytest.fixture(scope="module")
@allure.title("Получение io.BytesIO скриншота test.png")
def get_test_image_bytes_IO(get_test_image_bytes) -> io.BytesIO:
    """
    Получение io.BytesIO скриншота test.png
    """
    yield io.BytesIO(
        get_test_image_bytes
    )


@pytest.fixture(scope="module")
@allure.title("Получение PIL.Image скриншота test.png")
def get_test_image_pil_image(get_test_image_bytes_IO) -> Image:
    """
    Получение PIL.Image скриншота test.png
    """
    yield Image.open(
        get_test_image_bytes_IO
    )


@pytest.fixture(scope="module")
@allure.title("Получение байтов скриншота test_alter.png")
def get_test_alter_image_bytes() -> bytes:
    """
    Получение байтов скриншота test_alter.png
    """
    with open(os.path.join('tests', 'support', 'test_alter.png'), 'rb') as f:
        yield f.read()


@pytest.fixture(scope="module")
@allure.title("Получение io.BytesIO скриншота test_alter.png")
def get_test_alter_image_bytes_IO(get_test_alter_image_bytes) -> io.BytesIO:
    """
    Получение io.BytesIO скриншота test_alter.png
    """
    yield io.BytesIO(
        get_test_alter_image_bytes
    )


@pytest.fixture(scope="module")
@allure.title("Получение PIL.Image скриншота test_alter.png")
def get_test_alter_image_pil_image(get_test_alter_image_bytes_IO) -> Image:
    """
    Получение PIL.Image скриншота test_alter.png
    """
    yield Image.open(
        get_test_alter_image_bytes_IO
    )
