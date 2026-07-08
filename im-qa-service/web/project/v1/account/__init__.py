import time
from typing import Optional, Union

from fastapi import APIRouter, Query, Body

from pyvkteamsclient.client import DesktopClient
from web.project.logger import logger

from web.project.db import Account, Account_Pydantic
from web.project.v1.account.tasks import clean_client, clean_client_task
from web.project.v1.account.shortcuts import account_dict_modify
from web.project.v1.account.dantic import GroupNameEnum, \
    AccountCleanResponseModel, AccountReleaseResponseModel, IcqAccountModel, \
    VKTeamsAccountModel, IcqAccountResponseModel, VKTeamsAccountResponseModel

account_router = APIRouter(
    prefix='/account',
    tags=["accounts"]
)


@account_router.get(
    path='/take',
    name="Получение чистого аккаунта",
    responses={
        200: {
            "description": "Successful Response",
            "model": Union[
                IcqAccountResponseModel, VKTeamsAccountResponseModel]
        }
    }
)
async def take(
        group: GroupNameEnum = Query(
            default=None,
            description='Имя группы тестовых аккаунтов'
        ),
        account_id: Optional[int] = Query(
            default=None,
            description='ID тестового аккаунта',
            alias='id'
        )
):
    """
    Выдача аккаунта с предварительной отчисткой
    (удаление групп из рисентов, отписка от тредов,
    удаление лишних контактов, рисет настроек приватности и тд)
    """

    if group is None and account_id is None:
        raise ValueError('one of parameters must be not null: group, id')

    if account_id:
        account_model = await Account \
            .filter(id=account_id).order_by('ts', 'count_used').first()
    else:
        account_model = await Account.filter(
            group_name=group.value,
            available=1
        ).order_by('ts', 'count_used').first()

    account_dantic = await Account_Pydantic.from_tortoise_orm(account_model)

    account_dict = account_dict_modify(account_dantic)


    if account_model.group_name not in [
        "technical_users", "group_channels", "email"]:

        account_dict = account_dict_modify(account_dantic)
        clean_client(account_dict)
        account_model.available = 0
        account_model.count_used += 1
        account_model.ts = int(time.time())
        await account_model.save()

    return account_dantic


@account_router.post(
    path="/release",
    name="Освобождение тестового аккаунта",
    responses={
        200: {
            "description": "Successful Response",
            "model": AccountReleaseResponseModel
        }
    }
)
async def release(
        account_id: int = Query(
            ...,
            description='ID тестового аккаунта',
            alias='id'
        )
):
    """
    Очистка указанного аккаунта и пометка его как доступного
    """

    account_model = await Account.filter(id=account_id).first()
    account_model.available = 1
    await account_model.save()

    account_dantic = await Account_Pydantic.from_tortoise_orm(account_model)

    account_dict = account_dict_modify(account_dantic)
    task = clean_client_task.delay(
        account_dict, account_model.group_name, True
    )
    return {
        'success': True,
        'task_id': task.id
    }


@account_router.post(
    path="/release_all",
    name="Массовое освобождение аккаунтов",
    responses={
        200: {
            "description": "Successful Response",
            "model": AccountCleanResponseModel
        }
    }
)
async def release_all(
        group: Optional[GroupNameEnum] = Query(
            None,
            description='Имя группы тестовых аккаунтов'
        )
):
    """
    Очистка и освобождение занятых аккаунтов указанной группы.
    Если не указать группу - проход по всем занятым аккаунтам.
    """
    if group is None:
        query = Account.filter(available=0).all()
    else:
        query = Account.filter(
            available=0,
            group_name=group.value
        ).all()
    task_ids = []
    async for account in query:
        account_dantic = await Account_Pydantic.from_tortoise_orm(account)
        account_dict = account_dict_modify(account_dantic)
        task = clean_client_task.delay(
            account_dict, account.group_name
        )
        task_ids.append(task.id)

    if group is None:
        released_count = await Account.filter(available=0).update(available=1)
    else:
        released_count = await Account.filter(
            available=0,
            group_name=group.value
        ).update(available=1)
    return {
        'success': True,
        'released_count': released_count,
        'task_ids': task_ids
    }


@account_router.post(
    path="/clean",
    name="Очистка тестового аккаунта без разлогина",
    responses={
        200: {
            "description": "Successful Response",
            "model": AccountReleaseResponseModel
        }
    }
)
async def clean(
        account_id: int = Query(
            ...,
            description='ID тестового аккаунта',
            alias='id'
        )
):
    """
    Очистка тестового аккаунта без разлогина
    """

    account_model = await Account.filter(id=account_id).first()
    account_model.available = 0
    await account_model.save()

    account_dantic = await Account_Pydantic.from_tortoise_orm(account_model)

    account_dict = account_dict_modify(account_dantic)
    task = clean_client_task.delay(
        account_dict, account_model.group_name, False
    )
    return {
        'success': True,
        'task_id': task.id
    }


@account_router.post(
    path="/outside_clean",
    name="Очистка аккаунта не из базы",
    responses={
        200: {
            "description": "Successful Response",
            "model": AccountReleaseResponseModel
        }
    }
)
async def outside_clean(
        account_m: Union[IcqAccountModel, VKTeamsAccountModel] = Body(
            ...,
            description='Данные тестового аккаунта'
        ),
        sync: bool = Query(
            False,
            description='Флаг Sync/Async очистки'
        ),
):
    """
    Очистка аккаунта не из базы
    """
    logger.info(account_m)
    if sync:
        result, error = await clean_client(
            account_m.dict(), account_m.product.value
        )
        return {
            'success': result,
            "error": f'{type(error).__name__}: {str(error)}'
            if error is not None else None
        }
    else:
        task = clean_client_task.delay(
            account_m.dict(), account_m.product.value)
        return {
            'success': True,
            'task_id': task.id
        }


@account_router.put(
    path="/batch",
    name="Массовое добавление тестовых аккаунтов в базу",
)
async def batch_add(
        accounts: list[Account_Pydantic] = Body(
            ...,
            description="Список добавляемых тестовых аккаунтов"
        )
):
    """
    Добавление пака аккаунтов в базу
    """
    await Account.bulk_create([
        Account(**account.dict()) for account in accounts
    ])
    return {
        'success': True
    }


@account_router.get(
    path="/all",
    name="Получение списка всех аккаунтов"
)
async def get_all_accounts():
    """
    Получение списка всех аккаунтов
    :return:
    """
    return {
        "success": True,
        "accounts": await Account_Pydantic.from_queryset(
            Account.all().order_by('id'))
    }


@account_router.delete(
    path="/drop_all",
    name="Удаление всех аккаунтов из базы",
)
async def drop_all():
    """
    Удаление всех аккаунтов из базы
    """
    await Account.filter().delete()
    return {
        'success': True,
    }
