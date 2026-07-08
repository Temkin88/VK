import typing

from datetime import datetime

from pydantic import BaseModel, Field

from web.project.common_dantic import BaseResponseModel
from web.project.db import JiraEventTypeEnum, JiraProjectEnum


class Issue(BaseModel):
    key: str
    status: str


class JiraIssue(BaseModel):
    id: typing.Union[str, int]
    key: str = Field(..., regex='[' + ','.join(JiraProjectEnum) + ']+\-[0-9]+')
    fields: dict[str, typing.Union[str, int, list, dict, None]]


class JiraUser(BaseModel):
    name: typing.Optional[str] = Field(
        ..., title='Системное имя пользователя')
    key: typing.Optional[str] = Field(..., title='key')
    emailAddress: typing.Optional[str] = Field(..., title='email')
    displayName: typing.Optional[str] = Field(..., title='Отображаемое имя')
    active: bool = Field(..., title='Активен ли пользователь')


class JiraChangelogItem(BaseModel):
    to: typing.Optional[str]
    toString: typing.Optional[str] = Field(..., title='Строковое значение')
    from_: typing.Optional[str] = Field(..., alias='from')
    fromString: typing.Optional[str] = Field(..., title='Строковое значение')
    fieldtype: str = Field(..., title='Тип поля')
    field: str = Field(..., title='Название поля')


class JiraChangelogItems(BaseModel):
    __root__: list[JiraChangelogItem] = Field(..., title='Список изменений')


class JiraChangelog(BaseModel):
    items: JiraChangelogItems = Field(..., title='Список изменений')


class JiraComment(BaseModel):
    body: str = Field(..., title='Текст комментария')

    created: typing.Optional[datetime] = Field(..., title='Дата создания')
    author: typing.Optional[JiraUser] = Field(..., title='Автор комментария')

    updated: typing.Optional[datetime] = Field(..., title='Дата обновления')
    updateAuthor: typing.Optional[JiraUser] = Field(
        ..., title='Автор обновления комментария')


class IssueLinkType(BaseModel):
    id: int
    name: str
    outwardName: str
    inwardName: str
    subTask: bool
    system: bool


class IssueLink(BaseModel):
    id: int
    sourceIssueId: int
    destinationIssueId: int
    issueLinkType: IssueLinkType
    sequence: int = None
    systemLink: bool


class JiraJsonDantic(BaseModel):
    timestamp: datetime = Field(..., title='Дата события')
    issue: typing.Optional[JiraIssue] = Field(
        None, title='Инфо об изменениях в задаче')
    user: typing.Optional[JiraUser] = Field(None, title='Инфо о пользователе')
    changelog: typing.Optional[JiraChangelog] = Field(
        None, title='Изменения в задачах')
    comment: typing.Optional[JiraComment] = Field(
        None, title='Комментарий к задаче')
    issueLink: typing.Optional[IssueLink] = Field(
        None, title='Ссылка')
    webhookEvent: JiraEventTypeEnum = Field(..., title='Тип события')


class JiraHookResponseModel(BaseResponseModel):
    hook: typing.Optional[JiraJsonDantic]

class JiraTaskStatusResponseModel(BaseResponseModel):
    issue: Issue
