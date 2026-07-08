import os
import platform
import uuid

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.responses import UJSONResponse

from starlette.responses import StreamingResponse

from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk.integrations.starlette import StarletteIntegration
from sentry_sdk.integrations.fastapi import FastApiIntegration
from tortoise.contrib.fastapi import register_tortoise

from web.project import api_router
from web.project.db import Account, FailedRequest
from web.project.common_dantic import BaseResponseModel, FailedResponseModel

from web.project.logger import logger


sentry_sdk.init(
    "http://a147a3cbf86546fc8680ad931995d8bb@100.99.5.41:8000/3",
    traces_sample_rate=1.0,
    integrations=[
        StarletteIntegration(transaction_style="endpoint"),
        FastApiIntegration(transaction_style="endpoint"),
    ],
)
load_dotenv("../variables.env")


tags_metadata = [
    {
        "name": "accounts",
        "description": "Действия с тестовыми аккаунтами "
                       "для автотестов ICQ/VK Teams/M.Agent",
        "externalDocs": {
            "description": "Репозиторий с автотестами для десктопа",
            "url":
                "https://gitlab.corp.mail.ru/p.miroshnichenko/im-desktop-ci",
        },
    },
    {
        "name": "allure",
        "description": "Действия с тестовыми прогонами в Allure TestOps",
        "externalDocs": {
            "description": "Allure TestOps",
            "url": "https://allure.vk.team/",
        },
    },
    {
        "name": "builds",
        "description": "Действия связанные "
                       "с билдами клиента ICQ/VK Teams "
                       "(сохранение, выдача ссылок)"
    },
    {
        "name": "image",
        "description": "Работа со скриншотами из автотестов: "
                       "хранение, сравнение присланных с оригиналом"
    },
    {
        "name": "jira",
        "description": "Работа с задачами из JIRA (с кэшированием результатов)"
    },
    {
        "name": "healthcheck",
        "description": "Методы для Docker Healthcheck"
    },
    {
        "name": "product",
        "description": "Switcher статуса автотестов "
                       "отдельно по каждому продукту",
        "externalDocs": {
            "description": "Репозиторий с автотестами для десктопа",
            "url":
                "https://gitlab.corp.mail.ru/p.miroshnichenko/im-desktop-ci",
        },
    },
    {
        "name": "nignt release",
        "description": "Accounts for night checks"
    }
]


app = FastAPI(
    openapi_tags=tags_metadata,
    title="IM QA",
    version="1.0.0",
    contact={
        "name": "Valerii Korobov",
        "url":
            "https://u.internal.myteam.mail.ru/profile/v.korobov@corp.mail.ru",
        "email": "v.korobov@corp.mail.ru"
    },
    responses={
        200: {
            "description": "Successful Response",
            "model": BaseResponseModel
        },
        500: {
            "description": "Failed Response",
            "model": FailedResponseModel
        }
    }
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response: StreamingResponse = await call_next(request)

    request_uuid = str(uuid.uuid4())
    response.headers["X-Response-UUID"] = request_uuid

    logger.log(
        'INFO' if 200 <= response.status_code < 300 else 'WARNING',
        f'[{request.method}][{request_uuid}] {request.url} - '
        f'{response.status_code}'
    )
    return response


app.include_router(
    api_router,
)

register_tortoise(
    app,
    db_url=os.getenv('TORTOISE_DSN')
    if platform.system() != "Darwin" else "sqlite://db.sqlite",
    modules={'models': ['web.project.db']}
)


# @app.on_event("startup")
# @logger.catch
# async def startup():
#     await init_db()


@app.get(
    path='/healthcheck',
    tags=["healthcheck"],
    name="Проверка здоровья сервиса"
)
async def healthcheck():
    """
    Проверка здоровья сервиса
    """
    with logger.catch(reraise=True):
        await Account.filter().first()
    return {
        'success': True
    }


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
):

    content = jsonable_encoder({"detail": exc.errors(), "body": exc.body})

    logger.info(content)
    await FailedRequest.create(
        url=request.url,
        error_details=content
    )
    return await request_validation_exception_handler(request, exc)


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    """
    Хэндлер всех ошибок внутри сервиса
    """
    logger.exception(exc)
    return UJSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": f'{type(exc).__name__}: {str(exc)}'
        },
    )
