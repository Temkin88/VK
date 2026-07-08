from datetime import datetime, timedelta

import allure
import pytest

from fastapi.testclient import TestClient
from jira import JIRA
from jira.resources import Issue

from web.project.jira_acc import get_jira
from web.project.db import JiraTasks


@pytest.mark.anyio
@allure.suite("Действия с JIRA тасками")
@allure.feature("JIRA API wrapper")
@allure.title("Проверка aiojira.JIRA.create")
async def test_jira_integration():
    """
    Проверка aiojira.JIRA.create
    """
    with allure.step("Конструируем объект класса jira.Jira"):
        jira_acc = await get_jira()
        assert isinstance(jira_acc, JIRA)

    with allure.step(f"Проверям работоспособность {jira_acc}"):
        issue = await jira_acc.issue("IMDESKTOP-18876")
        assert isinstance(issue, Issue)


@pytest.mark.parametrize("jira_key", [
    "IMDESKTOP-18876",
    "IMSUPPORT-7204"
])
@pytest.mark.anyio
@allure.suite("Действия с JIRA тасками")
@allure.feature("Получение статуса JIRA таски")
@allure.title("Успешное получение статуса JIRA таски")
async def test_jira_get_status(
        client: TestClient,
        jira_key: str
):
    """
    Проверка получения статуса задачи в JIRA
    """
    with allure.step("Делаем запрос [GET] /api/v1/jira/task/status"):
        response = client.get(
            url="/api/v1/jira/task/status",
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                "key": jira_key
            }
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json()["success"]
        assert response.json()["issue"]["key"] == jira_key
        assert set(response.json()["issue"].keys()).issubset({"key", "status"})

    with allure.step("Проверяем что результаты запроса закэшировались в БД"):
        issue_model = await JiraTasks.filter(
            key=jira_key
        ).first()
        assert issue_model is not None
        assert issue_model.key == jira_key
        assert issue_model.status == response.json()["issue"]["status"]


@pytest.mark.anyio
@allure.suite("Действия с JIRA тасками")
@allure.feature("Получение статуса JIRA таски")
@allure.title("Успешное получение статуса JIRA таски не из кэша")
async def test_jira_get_status_not_from_db(client: TestClient):
    """
    Проверка получения статуса не закэшированной задачи
    """
    JIRA_KEY = "IMSUPPORT-7205"

    with allure.step("Подчищаем базу от кэша"):
        await JiraTasks.filter(
            key=JIRA_KEY
        ).delete()
    with allure.step("Делаем запрос [GET] /api/v1/jira/task/status"):
        response = client.get(
            url="/api/v1/jira/task/status",
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                "key": JIRA_KEY
            }
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json()["success"]
        assert response.json()["issue"]["key"] == JIRA_KEY
        assert set(response.json()["issue"].keys()).issubset({"key", "status"})


@pytest.mark.anyio
@allure.suite("Действия с JIRA тасками")
@allure.feature("Получение статуса JIRA таски")
@allure.title("Успешное получение статуса JIRA таски при инвалидации кэша [ДНИ=5]")
async def test_jira_get_status_passed_time_by_days(client: TestClient):
    """
    Проверка получения статуса задачи при инвалидации кэша (дни)
    """
    JIRA_KEY = "IMSUPPORT-7205"

    with allure.step("Инвалидируем кэш в БД"):
        issue_model = await JiraTasks.filter(key=JIRA_KEY).first()
        if issue_model is None:
            issue_model = JiraTasks(key=JIRA_KEY, status="Closed")

        issue_model.last_updated = datetime.now() - timedelta(days=5)
        await issue_model.save()

    with allure.step("Делаем запрос [GET] /api/v1/jira/task/status"):
        response = client.get(
            url="/api/v1/jira/task/status",
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                "key": JIRA_KEY
            }
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json()["success"]
        assert response.json()["issue"]["key"] == JIRA_KEY
        assert set(response.json()["issue"].keys()).issubset({"key", "status"})


@pytest.mark.parametrize("hours", [i for i in range(10)])
@pytest.mark.anyio
@allure.suite("Действия с JIRA тасками")
@allure.feature("Получение статуса JIRA таски")
@allure.title(
    "Успешное получение статуса JIRA "
    "таски при инвалидации кэша [ЧАСЫ={hours}]"
)
async def test_jira_get_status_passed_time_by_hours(
        client: TestClient,
        hours: int
):
    """
    Проверка получения статуса задачи при инвалидации кэша (часы)
    """
    JIRA_KEY = "IMSUPPORT-7205"
    with allure.step("Инвалидируем кэш в БД"):
        issue_model = await JiraTasks.filter(key=JIRA_KEY).first()
        if issue_model is None:
            issue_model = JiraTasks(key=JIRA_KEY, status="Closed")

        issue_model.last_updated = datetime.now() - timedelta(hours=hours)
        await issue_model.save()

    with allure.step("Делаем запрос [GET] /api/v1/jira/task/status"):
        response = client.get(
            url="/api/v1/jira/task/status",
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                "key": JIRA_KEY
            }
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json()["success"]
        assert response.json()["issue"]["key"] == JIRA_KEY
        assert set(response.json()["issue"].keys()).issubset({"key", "status"})
