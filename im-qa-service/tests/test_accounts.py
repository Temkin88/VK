import json
from typing import Union

import pytest
import allure

from fastapi.testclient import TestClient

from web.project.v1.account.dantic import GroupNamesEnum
from web.project.db import Account


@pytest.mark.parametrize(
    "group",
    (group.value for group in GroupNamesEnum),
    ids=(group.name for group in GroupNamesEnum),
)
@pytest.mark.anyio
@allure.suite("Действия с тестовыми аккаунтами")
@allure.feature("Получение тестового аккаунта")
@allure.title("Получение тестового аккаунта группы {group}")
async def test_take_account_by_group(
        client: TestClient,
        group: str
):
    """
    Проверка получения тестового аккаунта по названию группы.
    Если group = None - должна возникнуть ошибка
    ValueError("one of parameters must be not null").
    """
    if group != 'None':
        with allure.step("Делаем запрос [GET] /api/v1/account/take"):
            response = client.get(
                url='/api/v1/account/take',
                params={'group': group},
                headers={'X-Token': 'X-Tests'}
            )
        with allure.step(f"Проверяем {response}"):
            assert response.status_code == 200, \
                f"Status: {response.status_code} - {response.text}"
            assert response.json().get('group_name') == group
            assert sorted(list(response.json().keys())) == sorted([
                'id', 'group_name', 'phone', 'code', 'uin',
                'password', 'nickname', 'available', 'count_used', 'ts',
                'api_url', 'product'
            ])
        with allure.step("Проверяем изменения в БД"):
            account_model = await Account.filter(id=response.json().get('id')).first()
            if group not in ("group_channels", "technical_users", "email"):
                assert account_model.available == 0
            else:
                assert account_model.available == 1

    else:
        with allure.step("Делаем запрос [GET] /api/v1/account/take"):
            with pytest.raises(ValueError) as excinfo:
                response = client.get(
                    url='/api/v1/account/take',
                    headers={'X-Token': 'X-Tests'}
                )
        with allure.step("Проверям возникшую ошибку"):
            assert "one of parameters must be not null" in str(excinfo.value)


@pytest.mark.parametrize("account_id", [2, 243, 5, 300])
@pytest.mark.anyio
@allure.suite("Действия с тестовыми аккаунтами")
@allure.feature("Получение тестового аккаунта")
@allure.title("Получение тестового аккаунта ID {account_id}")
async def test_take_account_by_id(
        client: TestClient,
        account_id: int
):
    """
    Получение тестового аккаунта по ID
    """
    with allure.step("Делаем запрос [GET] /api/v1/account/take"):
        response = client.get(
            url='/api/v1/account/take',
            params={'id': account_id},
            headers={'X-Token': 'X-Tests'}
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json().get('id') == account_id
        assert sorted(list(response.json().keys())) == sorted([
            'id', 'group_name', 'phone', 'code', 'uin',
            'password', 'nickname', 'available', 'count_used', 'ts',
            'api_url', 'product'
        ])
    with allure.step("Проверяем изменения в БД"):
        account_model = await Account.filter(id=account_id).first()
        assert account_model.available == 0


@pytest.mark.parametrize("account_id", [2, 243, 5, 300])
@pytest.mark.anyio
@allure.suite("Действия с тестовыми аккаунтами")
@allure.feature("Возвращение тестовых аккаунтов")
@allure.title("Возвращение тестового аккаунта ID {account_id}")
async def test_release_account_by_id(
        client: TestClient,
        account_id: int
):
    """
    Проверка очистки аккаунта после освобождения от автотестов
    """
    with allure.step("Делаем запрос [POST] /api/v1/account/release"):
        response = client.post(
            url='/api/v1/account/release',
            params={'id': account_id},
            headers={'X-Token': 'X-Tests'}
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json() == {"success": True, "error": None}

    with allure.step("Проверяем изменения в БД"):
        account_model = await Account.filter(id=account_id).first()
        assert account_model.available == 1


@pytest.mark.parametrize("account_id", [2, 243, 5, 300])
@pytest.mark.anyio
@allure.suite("Действия с тестовыми аккаунтами")
@allure.feature("Возвращение тестовых аккаунтов")
@allure.title("Очистка аккаунта без разлогина ID {account_id}")
async def test_clean_account_by_id(
        client: TestClient,
        account_id: int
):
    """
    Проверка очистки аккаунта после освобождения от автотестов
    """
    with allure.step("Делаем запрос [POST] /api/v1/account/release"):
        response = client.post(
            url='/api/v1/account/clean',
            params={'id': account_id},
            headers={'X-Token': 'X-Tests'}
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json() == {"success": True, "error": None}

    with allure.step("Проверяем изменения в БД"):
        account_model = await Account.filter(id=account_id).first()
        assert account_model.available == 0


@pytest.mark.parametrize(
    "group",
    (group.value for group in GroupNamesEnum),
    ids=(group.name for group in GroupNamesEnum),
)
@pytest.mark.anyio
@allure.suite("Действия с тестовыми аккаунтами")
@allure.feature("Возвращение тестовых аккаунтов")
@allure.title("Возвращение тестовых аккаунтов группы {group}")
async def test_release_account_by_group(
        client: TestClient,
        group: str
):
    """
    Проверка очистки группых недоступных аккаунтов
    """
    with allure.step("Делаем запрос [POST] /api/v1/account/release_all"):
        response = client.post(
            url='/api/v1/account/release_all',
            params={'group': group} if group != 'None' else {},
            headers={'X-Token': 'X-Tests'}
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json()['success']
        assert tuple(response.json().keys()) == (
            'success', 'error', 'released_count')

    with allure.step("Проверяем изменения в БД"):
        if group == 'None':
            assert 0 == len(await Account.filter(available=0).all())
        else:
            assert 0 == len(await Account.filter(
                available=0,
                group_name=group
            ).all())


@pytest.mark.anyio
@allure.suite("Действия с тестовыми аккаунтами")
@allure.feature("Добавление аккаунтов")
@allure.title("Добавление пака аккаунтов")
async def test_batch_account_add(
        client: TestClient,
):
    """
    Проверка добавления пака аккаунтов
    """
    with allure.step("Удаляем все аккаунты из БД"):
        await Account.filter().delete()

    with allure.step("Делаем запрос [PUT] /api/v1/account/batch"):
        try:
            with open("accounts.json", "rb") as f:
                accounts = json.load(f)
        except FileNotFoundError:
            with open("accounts.json", "rb") as f:
                accounts = json.load(f)
        response = client.put(
            url='/api/v1/account/batch',
            json=accounts,
            headers={'X-Token': 'X-Tests'}
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json() == {'error': None, 'success': True}

    with allure.step("Проверяем изменения в БД"):
        assert len(accounts) == len(await Account.all())


@pytest.mark.anyio
@allure.suite("Действия с тестовыми аккаунтами")
@allure.feature("Удаление аккаунтов")
@allure.title("Удаление всех аккаунтов из базы данных")
async def test_drop_all(
        client: TestClient
):
    """
    Проверка удаления всех аккаунтов из базы данных
    """
    with allure.step("Делаем запрос [PUT] /api/v1/account/drop_all"):
        response = client.delete(
            url='/api/v1/account/drop_all',
            headers={'X-Token': 'X-Tests'}
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert tuple(response.json().keys()) == ('success', 'error', 'released_count')
        assert response.json().get('success')

    with allure.step("Проверяем изменения в БД"):
        assert 0 == len(await Account.all())


@pytest.mark.parametrize('mode', (True, False), ids=('sync', 'async'))
@pytest.mark.parametrize(
    'account',
    [
        {
            "type": "icq",
            "phone": "+9999202003201",
            "code": "402457",
            "uin": None,
            "password": None,
            "api_url": "https://u.icq.net"
        },
        {
            "type": "myteam",
            "phone": None,
            "code": None,
            "uin": "autotest10@im-auto.com",
            "password": "eleven",
            "api_url": "https://u-im-testing.v3.im-sandbox.devmail.ru"
        },
        {
            "type": "myteam_on_premise",
            "phone": None,
            "code": None,
            "uin": "autotest10@im-auto.hb.bizmrg.com",
            "password": "twelve",
            "api_url": "https://u-im-testing.v3.im-sandbox.devmail.ru"
        },
    ],
    ids=[
        "icq",
        "myteam",
        "myteam_on_premise"
    ]
)
@pytest.mark.anyio
@allure.suite("Действия с тестовыми аккаунтами")
@allure.feature("Очистка внешних аккаунтов")
@allure.title("Очистка аккаунтов не из базы данных")
async def test_outside_clean(
        client: TestClient,
        mode: bool,
        account: dict[str, Union[str, int, None]]
):
    """
    Проверка очистки аккаунта не из базы данных
    """
    with allure.step("Делаем запрос [POST] /api/v1/account/outside_clean"):
        response = client.post(
            url='/api/v1/account/outside_clean',
            headers={'X-Token': 'X-Tests'},
            params={'sync': mode},
            json=account
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        if response.json()["success"]:
            assert response.json() == {"success": True, "error": None}
        else:
            assert "error" in response.json()
