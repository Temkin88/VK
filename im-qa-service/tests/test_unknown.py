import allure
import pytest

from fastapi.testclient import TestClient


@pytest.mark.anyio
@allure.suite("Базовые ответы FastAPI")
@allure.feature("Ошибка")
@allure.title("Неизвестная страница")
async def test_unkwnown_page(client: TestClient):
    """
    Проверка запроса несуществущей страницы
    """
    with allure.step("Делаем запрос [GET] /kek"):
        response = client.get('/kek')
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 404, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json() == {"detail": "Not Found"}
