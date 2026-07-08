import allure
import pytest

from web.project.db import init_db


@pytest.mark.anyio
@allure.suite("База данных")
@allure.feature("Создание базы данных")
@allure.title("Проверка инициализации базы данных")
async def test_init_db():
    """
    Проверка инициализации базы данных
    """
    with allure.step("Проверям инициализацию базы данных"):
        await init_db()
