import allure
import pytest
from fastapi.testclient import TestClient

from web.project.v1 import v1_router


@pytest.mark.parametrize("path,methods", [
    (route.path, route.methods) for route in v1_router.routes

], ids=(route.path for route in v1_router.routes))
@pytest.mark.parametrize("x_token,to_fail", [
    (None, True),
    ("X-Token", True),
    ("X-Tests", False)
])
@pytest.mark.anyio
@allure.suite("Базовые ответы FastAPI")
@allure.feature("X-Token")
@allure.title(
    "Depencies = get_token_header [{methods}] {path} - "
    "X-Token: {x_token} - {to_fail}"
)
async def test_x_token(
        path: str,
        methods: set[str],
        x_token: str,
        to_fail: bool,
        client: TestClient
):
    """
    Проверка механизма авторизации по токену
    """

    if path != '/v1/account/take':
        for method in methods:
            with allure.step(f"Делаем запрос [{method}] {path} - X-Token: {x_token}"):
                response = client.request(
                    method=method,
                    url=path,
                    headers={
                        'X-Token': x_token
                    } if x_token is not None else {}
                )
            with allure.step(f"Проверяем {response}"):
                if to_fail:
                    if x_token is None:
                        assert response.status_code == 422, \
                            f"Status: {response.status_code} - {response.text}"
                    else:
                        assert response.status_code == 403, \
                            f"Status: {response.status_code} - {response.text}"
                        assert response.json() == {
                            "detail": "X-Token header invalid"}
                else:
                    assert response.status_code != 403, \
                        f"Status: {response.status_code} - {response.text}"
                    assert response.json() != {
                        "detail": "X-Token header invalid"}
    else:
        for method in methods:
            if not to_fail:
                with allure.step(
                        f"Делаем запрос [{method}] {path} - "
                        f"X-Token: {x_token}"
                ):
                    with pytest.raises(ValueError):
                        response = client.request(
                            method=method,
                            url=path,
                            headers={
                                'X-Token': x_token
                            } if x_token is not None else {}
                        )
            else:
                with allure.step(
                        f"Делаем запрос [{method}] {path} - "
                        f"X-Token: {x_token}"
                ):
                    response = client.request(
                        method=method,
                        url=path,
                        headers={
                            'X-Token': x_token
                        } if x_token is not None else {}
                    )
                with allure.step(f"Проверяем {response}"):
                    if x_token is None:
                        assert response.status_code == 422, \
                            f"Status: {response.status_code} - {response.text}"
                    else:
                        assert response.status_code == 403, \
                            f"Status: {response.status_code} - {response.text}"
                        assert response.json() == {
                            "detail": "X-Token header invalid"}
