import os
import logging

from typing import Optional

from fastapi.responses import Response
from starlette.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from fastapi.responses import UJSONResponse

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.routers.errors import error
from app.routers.kata import scan_delete, scans_state, scan
from app.routers.miniapp.spa import spa
from app.routers.data_test import data_router
from app.routers.cloud.router import cloud

from app.models.database import Error


prefix = '/kata/scanner/v1/sensors'

app = FastAPI(title='Fake KATA')

app.mount("/static", StaticFiles(directory='app/static'), name="static")

log = logging.getLogger('fake-kata')
log.setLevel(logging.WARNING)
# log = Logger.with_default_handlers(
#             name='fake-kata',
#             formatter=Formatter(
#                 '%(asctime)s - '
#                 '%(name)s - '
#                 '%(levelname)s - '
#                 '%(module)s:%(funcName)s:%(lineno)d - '
#                 '%(message)s'
#             ),
#             level=LogLevel.DEBUG
#         )

app.include_router(scan.router, prefix=prefix, tags=['scan', 'scan_init'])
app.include_router(scans_state.router, prefix=prefix, tags=['scan', 'scan_get_state'])
app.include_router(scan_delete.router, prefix=prefix, tags=['scan', 'scan_delete'])
app.include_router(error.router, tags=['errors'])
app.include_router(spa)
app.include_router(data_router)
app.include_router(cloud)

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


templates = Jinja2Templates(directory="app/templates")


@app.api_route(
    "/{template_name}", methods=["GET", "HEAD"])
async def read_item(
        request: Request,
        template_name: str,
        platform: Optional[str] = 'web',
        aimsid: Optional[str] = None
):
    if request.method == "GET":
        return templates.TemplateResponse(
            template_name, {
                "request": request, "platform": platform, "aimsid": aimsid})
    else:
        return Response()


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    log.exception(exc)

    model = await Error.create(
        exc_msg=str(exc)
    )

    return UJSONResponse(
        status_code=500,
        content={
            "message": f"InternalServerError: {exc}",
            "error_uuid": model.uuid
        },
    )


@app.on_event('startup')
async def app_init():
    """
    Here we create a SQLite DB using file "db.sqlite3"
     also specify the app name of "database"
     which contain models from "app.database"
    """

    register_tortoise(
        app,
        db_url=os.getenv('DB_URL', 'sqlite://db.sqlite3'),
        modules={'models': ['app.models.database']},
        generate_schemas=True,
        add_exception_handlers=True,
    )


@app.get('/{folder}/{filename}')
async def get_file(
        folder: str,
        filename: str
):

    return HTMLResponse(
        content=f'<pre><h1>Folder</h1><code>{folder}</code><br><h1>Filename</h1><code>{filename}</code></pre>'
    )


@app.get('/home/{folder}/{filename}')
async def get_file(
        folder: str,
        filename: str
):

    return HTMLResponse(
        content=f'<pre><h1>Folder</h1><code>{folder}</code><br><h1>Filename</h1><code>{filename}</code></pre>'
    )
