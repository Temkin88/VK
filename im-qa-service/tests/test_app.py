import allure
import pytest

from fastapi import FastAPI

from web.main import app
from web.project.v1 import v1_router


routes = [
    (route.path, route.methods) for route in app.routes
]


@pytest.mark.anyio
@allure.suite("Тесты характеристик приложения")
@allure.feature("Paths")
@allure.title("Проверка наличия routes in app.routes")
async def test_app_routes():
    """
    Проверка наличия v1_router.routes в app.routes
    """
    for route in v1_router.routes:
        with allure.step(
                f"Проверяем наличием "
                f"{(f'/api{route.path}', route.methods)} в app.routes"
        ):
            assert (f'/api{route.path}', route.methods) in routes, \
                f"Route {(route.path, route.methods)} not in app.routes"


@pytest.mark.anyio
@allure.suite("Тесты характеристик приложения")
@allure.feature("Debug mode")
@allure.title("Проверка отключенности debug mode")
async def test_app_mode(get_app: FastAPI):
    """
    Проверка отключенности debug mode
    """
    with allure.step("Проверяем app.debug"):
        assert get_app.debug is False, "App in debug mode"


@pytest.mark.anyio
@allure.suite("Тесты характеристик приложения")
@allure.feature("Описание")
@allure.title("Контакты")
async def test_app_contact(get_app: FastAPI):
    """
    Проверка правильной заполненности данных в /docs
    """
    with allure.step("Проверяем app.contact"):
        assert get_app.contact == {
            "name": "Valerii Korobov",
            "url": "https://u.internal.myteam.mail.ru/profile/v.korobov@corp.mail.ru",
            "email": "v.korobov@corp.mail.ru"
        }, f"Fail: app.contact - {app.contact}"


@pytest.mark.anyio
@allure.suite("Тесты характеристик приложения")
@allure.feature("Описание")
@allure.title("Версия")
async def test_app_version(get_app: FastAPI):
    """
    Проверка указанной версии приложения
    """
    with allure.step("Проверяем app.version"):
        assert get_app.version == "1.0.0", f"Wrong app version: {app.version}"


@pytest.mark.anyio
@allure.suite("Тесты характеристик приложения")
@allure.feature("Описание")
@allure.title("Title")
async def test_app_title(get_app: FastAPI):
    """
    Проверка указанного Title в /docs
    """
    with allure.step("Проверяем app.title"):
        assert get_app.title == "IM QA", f"Wrong app title: {app.title}"


@pytest.mark.anyio
@allure.suite("Тесты характеристик приложения")
@allure.feature("Events on startup/shutdown")
@allure.title("Startup event")
async def test_app_startup(get_app: FastAPI):
    """
    Проверка действий на старте приложения
    """
    for func in get_app.router.on_startup:
        with allure.step(f"Проверяем {func.__name__}"):
            await func()
