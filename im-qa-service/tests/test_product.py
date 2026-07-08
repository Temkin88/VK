from typing import Type

import allure
import pytest
from fastapi.testclient import TestClient

from web.project.v1.product import ProductTypeEnum


@pytest.mark.parametrize(
    "product_type", ProductTypeEnum
)
@pytest.mark.anyio
@allure.suite("Действия с продуктовыми статусами")
@allure.feature("Получение статуса продукта")
@allure.title("Получение статуса продукта {product_type}")
async def test_product_status_success(
        client: TestClient,
        product_type: Type[ProductTypeEnum]
):
    with allure.step("Делаем запрос [GET] /api/v1/jira/task/status"):
        response = client.get(
            url='/api/v1/product/status',
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                'type': product_type
            }
        )

    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json()["success"]
        assert response.json()["product"] == {
            "name": product_type.value,
            "status": True if product_type != 'armgs' else False
        }
