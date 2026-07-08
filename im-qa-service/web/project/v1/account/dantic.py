import uuid
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, AnyHttpUrl, EmailStr

from web.project.common_dantic import BaseResponseModel


class GroupNameEnum(str, Enum):
    """
    Варианты групп аккаунтов для автотестов
    """
    person = "person"
    stat1 = "stat1"
    stat2 = "stat2"
    stat3 = "stat3"
    group_channels = "group_channels"
    myteam = "myteam"
    myteam_on_premise = "myteam_on_premise"
    technical_users = "technical_users"
    email = "email"
    memstat = "memstat"
    empty = "empty"
    uin = "uin"
    phone = "phone"
    none = None


class AccountReleaseResponseModel(BaseResponseModel):
    """
    Модель успешного ответа на запрос очистки аккаунта
    """
    task_id: Optional[uuid.UUID] = Field(
        ..., description='ID задачи на очистку при выборе асинхронной очистки')


class AccountCleanResponseModel(BaseResponseModel):
    """
    Модель успешного ответа на запрос массовой очистки аккаунтов
    """
    released_count: int = Field(
        1, description='Количество аккаунтов, попавших под очистку')
    task_ids: list[uuid.UUID] = Field(
        ..., description='Список ID созданных задач на очистку')


class BaseAccountResponseModel(BaseModel):
    """
    Модель ответа на запрос аккаунта для автотестов
    """
    account_id: Optional[int] = Field(..., alias='id')


class IcqAccountResponseModel(BaseAccountResponseModel):
    """
    Учетка от ICQ
    """
    phone: str = Field(
        ...,
        description='Нарнийский номер телефона',
        regex=r'\+[0-9]{13}'
    )
    code: str = Field(
        ...,
        description='Фиксированный смс-код от учетки',
        alias='code'
    )


class VKTeamsAccountResponseModel(BaseAccountResponseModel):
    """
    Учетка от VK Teams
    """
    uin: EmailStr = Field(
        'v.korobov@corp.mail.ru', description='UIN учетной записи')
    password: str = Field('eleven', description='Фиксированный OTP-код')


class ProductTypeEnum(str, Enum):
    """
    Поддерживаемые типы продуктов
    """
    icq = "icq"
    myteam = "myteam"
    myteam_on_premise = "myteam_on_premise"
    agent = "agent"
    armgs = "armgs"


class OutAccountModel(BaseModel):
    """
    Базовый класс учетной записи для очистки
    """
    id: Optional[int] = 1000
    api_url: AnyHttpUrl = Field(
        'https://u.icq.net'
    )
    product: ProductTypeEnum = Field(..., alias='type')


class IcqAccountModel(OutAccountModel):
    """
    Данные учетной записи ICQ
    """
    phone: str = Field(
        ...,
        description='Нарнийский номер телефона',
        regex=r'\+[0-9]{13}'
    )
    sms_code: str = Field(
        ...,
        description='Фиксированный смс-код от учетки',
        alias='code'
    )


class VKTeamsAccountModel(OutAccountModel):
    """
    Данные учетной записи VK Teams
    """
    uin: EmailStr = Field(
        ...,
        description='UIN учетной записи'
    )
    password: str = Field(
        ...,
        description='OTP-код от учетной записи'
    )
