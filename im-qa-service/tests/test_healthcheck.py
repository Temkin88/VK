import allure
import pytest

from fastapi.testclient import TestClient


@pytest.mark.anyio
@allure.suite("Подготовка к Docker")
@allure.feature("Healthcheck")
@allure.title("Проверка метода /healthcheck")
async def test_healthcheck(client: TestClient):
    """
    Проверка метода /healthcheck
    """
    with allure.step("Делаем запрос [GET] /healthcheck"):
        response = client.get('/healthcheck')
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json() == {'success': True}
