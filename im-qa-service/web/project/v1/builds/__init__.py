from fastapi import APIRouter, BackgroundTasks, Query
from fastapi.responses import Response
from pydantic import AnyHttpUrl
from tortoise.exceptions import DoesNotExist

from web.project.db import Build, BuildUrl, Build_Pydantic, BuildUrl_Pydantic

from web.project.v1.builds.dantic import BuildPlatformEnum, BuildTypeEnum, BuildModel
from web.project.v1.builds.shortcuts import load_from_url_to_s3, send_build_text

builds_router = APIRouter(
    prefix="/builds",
    tags=["builds"]
)


@builds_router.get(
    '/receive',
    name='Сохранить билд из переданной ссылки c Jenkins',
    responses={
        200: {
            "description": "Request serverd with loading files to bucket",
            "model": BuildModel
        },
        201: {
            "description": "Request serverd without loading files to bucket",
        }
    }
)
async def receive(
        tasks: BackgroundTasks,
        BRANCH_NAME: str = Query(
            default='master',
            description='Ветка клиента',
            alias='branch'
        ),
        BUILD_ID: int = Query(
            ...,
            description="ID build на Jenkins",
            alias="build_id"
        ),
        BUILD_URLS: list[AnyHttpUrl] = Query(
            ...,
            description="Прямые URL для скачивания билдов с Jenkins",
            alias="build_urls"
        ),
        BUILD_PLATFORM: BuildPlatformEnum = Query(
            ...,
            description="Платформа билда клиента"
        ),
        BUILD_KIND: BuildTypeEnum = Query(
            default=BuildTypeEnum.icq,
            description="Тип билда",
            alias="type"
        ),
        BUILD_FULL_VERSION: str = Query(
            ...,
            description="Версия билда",
            alias='version'
        ),
        BUILD_TEXT: str = Query(
            default=None,
            alias='text'
        ),
        WITH_TESTING: bool = Query(
            False,
            description="Был ли билд создан для автотестов"
        )
):
    if BUILD_TEXT is not None:
        await send_build_text(
            BUILD_TEXT
        )
    if not WITH_TESTING:
        return Response(status_code=201)

    BUILD_MAJOR_VERSION, \
    BUILD_MINOR_VERSION, \
    BUILD_PATCH_VERSION, \
    BUILD_NUMBER = BUILD_FULL_VERSION.split('.')

    build_model = await Build.create(
        build_id=BUILD_ID,
        branch=BRANCH_NAME,
        platform=BUILD_PLATFORM,
        kind=BUILD_KIND,
        major=BUILD_MAJOR_VERSION,
        minor=BUILD_MINOR_VERSION,
        patch=BUILD_PATCH_VERSION,
        buildnumber=BUILD_NUMBER,
        full_version=BUILD_FULL_VERSION
    )

    for build_url in BUILD_URLS:
        FILE_NAME = build_url.split('/')[-1]

        tasks.add_task(
            load_from_url_to_s3,
            build_url,
            FILE_NAME,
            BUILD_KIND,
            BUILD_PLATFORM,
            BUILD_FULL_VERSION
        )

        await BuildUrl.create(
            build=build_model,
            url='/'.join([
                "http://im.builds.hb.bizmrg.com",
                BUILD_KIND,
                BUILD_PLATFORM,
                BUILD_FULL_VERSION,
                FILE_NAME
            ]),
            file_name=FILE_NAME
        )

    return {
        'BRANCH_NAME': BRANCH_NAME,
        'BUILD_ID': BUILD_ID,
        'BUILD_URLS': BUILD_URLS,
        'BUILD_PLATFORM': BUILD_PLATFORM,
        'BUILD_TYPE': BUILD_KIND.value,
        'BUILD_VERSION': {
            'major': BUILD_MAJOR_VERSION,
            'minor': BUILD_MINOR_VERSION,
            'patch': BUILD_PATCH_VERSION,
            'buildnumber': BUILD_NUMBER
        },
        'BUILD_TEXT': BUILD_TEXT,
        'WITH_TESTING': WITH_TESTING
    }


@builds_router.get('/get_build')
async def get_current_build(
        BRANCH_NAME: str = Query(
            default='master',
            description='Ветка клиента',
            alias='branch'
        ),
        BUILD_PLATFORM: BuildPlatformEnum = Query(
            ...,
            description="Платформа билда клиента"
        ),
        BUILD_KIND: BuildTypeEnum = Query(
            default=BuildTypeEnum.icq,
            description="Тип билда",
            alias="type"
        ),
        CURRENT: bool = Query(
            default=True,
            description="Получить инфу о текущем/предыдущем билде",
            alias="current"
        )
):
    build_model = await Build.filter(
        branch=BRANCH_NAME,
        platform=BUILD_PLATFORM.value,
        kind=BUILD_KIND.value
    ).order_by('-build_id').offset(
        0 if CURRENT else 1
    ).first()

    if build_model is None:
        raise DoesNotExist(f'Build(branch="{BRANCH_NAME}") not exist')

    await build_model.fetch_related()

    build_dantic = await Build_Pydantic.from_tortoise_orm(build_model)

    build_dict = build_dantic.dict()
    build_dict["urls"] = []

    async for build_url in build_model.build_urls.all():
        build_dict["urls"].append(
            (await BuildUrl_Pydantic.from_tortoise_orm(build_url)).dict()
        )

    return build_dict
