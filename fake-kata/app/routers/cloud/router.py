import os
from datetime import datetime, timedelta

from fastapi import APIRouter, Query, Request, Path, UploadFile, File, Header
from fastapi.responses import JSONResponse, Response

from pydantic import BaseModel, Field

from typing import List

from app.models.database import \
    User, UserLoader, UserFileInfo, UserFileInfo_Pydantic


cloud = APIRouter(prefix='/api')


@cloud.get('/v1/users/ids')
async def get_users_by_mail(
        request: Request,
        emails: List[str] = Query(...)
):
    uid_list = []

    for email in emails:
        model, _ = await User.get_or_create(
            email=email,
            x_real_ip=request.headers.get('x-real-ip') or request.headers.get('X-Real-IP') or 'none'
        )
        uid_list.append(model.id)

    return JSONResponse(
        content={
            "status": 200,
            "htmlencoded": False,
            "last_modified": int(
                (datetime.now() - timedelta(days=5)).timestamp()),
            "body": uid_list
        }
    )


@cloud.get('/v2/internal/loader')
async def get_loader_url(
        email: str = Query(..., alias='x-email'),
        uid: str = Query(..., alias='x-uid')
):

    loader_model = await UserLoader.create(
        user_id=uid,
    )

    return JSONResponse(
        content={
            'status': 200,
            'body': f"http://fake-kata.im-sandbox.devmail.ru/api/v2/upload/{loader_model.id}"
        }
    )


@cloud.post('/v2/upload/{loader_id}')
async def load_file(
        loader_id: int = Path(...),
        file: UploadFile = File(...)
):
    try:
        os.mkdir('/'.join(['files', str(loader_id)]))
    except FileExistsError:
        pass
    file_path = '/'.join(['files', str(loader_id), file.filename])

    file_bytes = await file.read()

    with open(file_path, 'wb') as f:
        f.write(file_bytes)

    await UserLoader.filter(id=loader_id).update(file_path=file_path)

    return Response(
        content=f'{hash(file_bytes)};{len(file_bytes)}'
    )


class FileAddRequest(BaseModel):
    path: str
    hash_: str = Field(..., alias='hash')
    size: int
    conflict: str
    publish: bool


@cloud.post('/v4/internal/file/add')
async def file_add(
        request: Request,
        file: FileAddRequest,
        email: str = Header(..., alias='X-Email'),
        uid: str = Header(..., alias='X-Uid')
):
    model, _ = await UserFileInfo.get_or_create(
        type='text',
        path=file.path,
        name=file.path.split('/')[-1],
        hash=file.hash_,
        size=file.size
    )

    return JSONResponse(
        content={
            'path': file.path,
            'node_id': str(model.node_id)
        }
    )


@cloud.get('/v4/internal/file/info')
async def get_file_info(
        node_id: int
):
    model = await UserFileInfo.get(node_id=node_id)

    py_model = await UserFileInfo_Pydantic.from_tortoise_orm(model)

    model_dict = py_model.dict()

    model_dict['node_id'] = str(model_dict['node_id'])

    return model_dict


@cloud.get('/v2/internal/folder')
async def folder_list(
        home_path: str = Query(..., alias='home'),
        email: str = Query(..., alias='x-email'),
        uid: str = Query(..., alias='x-uid')
):
    return JSONResponse(
        content={
            'status': 200,
            'body': {

            }
        }
    )
