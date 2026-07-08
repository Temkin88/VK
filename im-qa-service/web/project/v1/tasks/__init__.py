from fastapi import APIRouter, Query, Path, Body
from fastapi.responses import ORJSONResponse
from tortoise.exceptions import DoesNotExist

from web.project.v1.account.dantic import BaseResponseModel
from web.project.v1.tasks.dantic import JiraTaskStatusResponseModel, \
    JiraJsonDantic, JiraHookResponseModel
from web.project.db import JiraJsonData, JiraProjectEnum, \
    JiraJsonData_Pydantic

from web.project.v1.tasks.tasks import \
    imserver_map_priority, \
    imsupport_critical_notify

tasks_router = APIRouter(prefix='/jira', tags=["jira"])


@tasks_router.get(
    path="/task/hook/{hook_id}",
    name="Получение хука из базы по ID",
    responses={
        200: {
            "description": "Success",
            "model": JiraHookResponseModel
        }
    }
)
async def get_task_hook(hook_id: int):

    return {
        "success": True,
        "hook": await JiraJsonData_Pydantic.from_queryset_single(
            JiraJsonData.get(id=hook_id)
        )
    }


@tasks_router.get(
    "/task/{ISSUE_KEY}",
    name="Получение статуса задачи из JIRA",
    responses={
        200: {
            "description": "Success",
            "model": JiraTaskStatusResponseModel
        }
    })
async def status(
        ISSUE_KEY: str = Path(
            ...,
            description='Ключ задачи из JIRA'
        ),
        fields: str = Query(...)
):
    """
    Получение статуса задачи из JIRA
    """
    async for row in JiraJsonData.filter(issue_key=ISSUE_KEY).order_by('-id'):
        if row.issue is not None:

            return {
                "success": True,
                "issue": {
                    "key": ISSUE_KEY.strip(),
                    "fields": {
                        field: row.issue["fields"].get(field)
                        for field in fields.strip().split(',')
                    }
                }
            }
    else:
        raise DoesNotExist(f'Issue {ISSUE_KEY} not exist in DB')


@tasks_router.post(
    path='/task/{JIRA_PROJECT_KEY}/{JIRA_ISSUE_KEY}',
    name="Метод для получения webhook из JIRA",
    responses={
        200: {
            "description": "Success",
            "model": BaseResponseModel
        }
    })
async def jira_changelog(
        jira_event: JiraJsonDantic = Body(..., title='Тело вебхука'),
        user_id: str = Query(
            None, description='ID пользователя в Jira'
        ),
        user_key: str = Query(
            None, description='ID пользователя в Jira'
        ),
        JIRA_PROJECT_KEY: JiraProjectEnum = Path(
            description='Проект события',
            min_length=3,
            max_length=15,
            example=JiraProjectEnum.IMDESKTOP,
            regex='[' + ','.join(JiraProjectEnum) + ']+'
        ),
        JIRA_ISSUE_KEY: str = Path(
            description='Задача события',
            min_length=5,
            max_length=20,
            example='IMDESKTOP-18876',
            regex='[' + ','.join(JiraProjectEnum) + ']+\-[0-9]+'
        ),
) -> ORJSONResponse:
    model = await JiraJsonData.create(
        user_id=user_id,
        user_key=user_key,
        project_key=JIRA_PROJECT_KEY,
        issue_key=JIRA_ISSUE_KEY,
        date=jira_event.timestamp,
        event_type=jira_event.webhookEvent,
        issue=jira_event.issue.json()
        if jira_event.issue else jira_event.issue,
        user=jira_event.user.json()
        if jira_event.user else jira_event.user,
        changelog=jira_event.changelog.json()
        if jira_event.changelog else jira_event.changelog,
        comment=jira_event.comment.json()
        if jira_event.comment else jira_event.comment,
        issue_link=jira_event.issueLink.json()
        if jira_event.issueLink else jira_event.issueLink,
    )

    if JIRA_PROJECT_KEY in [
        JiraProjectEnum.IMSERVER,
        JiraProjectEnum.IMDESKTOP,
        JiraProjectEnum.IMWEB,
        JiraProjectEnum.IMIOS,
        JiraProjectEnum.IMA,
        JiraProjectEnum.IMVOIP
    ]:
        imserver_map_priority.delay(
            key=JIRA_ISSUE_KEY
        )

    if JIRA_PROJECT_KEY == JiraProjectEnum.IMSUPPORT:
        imsupport_critical_notify.delay(row_id=model.id)

    return ORJSONResponse(
        content={
            'success': True,
        }
    )


@tasks_router.post(
    path='/task/{JIRA_PROJECT_KEY}//',
    name="Метод для получения webhook из JIRA",
    responses={
        200: {
            "description": "Success",
            "model": BaseResponseModel
        }
    })
async def jira_changelog_misc_1(
        jira_event: JiraJsonDantic = Body(..., title='Тело вебхука'),
        user_id: str = Query(
            None, description='ID пользователя в Jira'
        ),
        user_key: str = Query(
            None, description='ID пользователя в Jira'
        ),
        JIRA_PROJECT_KEY: JiraProjectEnum = Path(
            description='Проект события',
            min_length=3,
            max_length=15,
            example=JiraProjectEnum.IMDESKTOP,
            regex='[' + ','.join(JiraProjectEnum) + ']+'
        )
) -> ORJSONResponse:
    # result_model = await JiraJsonData.create(
    #     user_id=user_id,
    #     user_key=user_key,
    #     project_key=JIRA_PROJECT_KEY,
    #     issue_key='COMMON',
    #     date=jira_event.timestamp,
    #     event_type=jira_event.webhookEvent,
    #     issue=jira_event.issue.json()
    #     if jira_event.issue else jira_event.issue,
    #     user=jira_event.user.json()
    #     if jira_event.user else jira_event.user,
    #     changelog=jira_event.changelog.json()
    #     if jira_event.changelog else jira_event.changelog,
    #     comment=jira_event.comment.json()
    #     if jira_event.comment else jira_event.comment,
    #     issue_link=jira_event.issueLink.json()
    #     if jira_event.issueLink else jira_event.issueLink,
    # )

    return ORJSONResponse(
        content={
            'success': True
        }
    )


@tasks_router.post(
    path='/task//',
    name="Метод для получения webhook из JIRA",
    responses={
        200: {
            "description": "Success",
            "model": BaseResponseModel
        }
    })
async def jira_changelog_misc_2(
        jira_event: JiraJsonDantic = Body(..., title='Тело вебхука'),
        user_id: str = Query(
            None, description='ID пользователя в Jira'
        ),
        user_key: str = Query(
            None, description='ID пользователя в Jira'
        ),
) -> ORJSONResponse:
    # result_model = await JiraJsonData.create(
    #     user_id=user_id,
    #     user_key=user_key,
    #     project_key='COMMON',
    #     issue_key='COMMON',
    #     date=jira_event.timestamp,
    #     event_type=jira_event.webhookEvent,
    #     issue=jira_event.issue.json()
    #     if jira_event.issue else jira_event.issue,
    #     user=jira_event.user.json()
    #     if jira_event.user else jira_event.user,
    #     changelog=jira_event.changelog.json()
    #     if jira_event.changelog else jira_event.changelog,
    #     comment=jira_event.comment.json()
    #     if jira_event.comment else jira_event.comment,
    #     issue_link=jira_event.issueLink.json()
    #     if jira_event.issueLink else jira_event.issueLink,
    # )

    return ORJSONResponse(
        content={
            'success': True,
        }
    )
