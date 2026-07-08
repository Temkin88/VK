import io
import json
import os

import aioboto3
from PIL import Image
from fastapi import APIRouter, Query, File, BackgroundTasks
from fastapi.responses import Response, UJSONResponse

from web.project.logger import logger

from web.project.v1.image.dantic import ImageTypeEnum, LanguageEnum, \
    ImageCompareResponse, CompareEventTypeEnum
from web.project.v1.image.tasks import \
    send_report_on_new_image_task, \
    send_report_on_image_diff_task
from web.project.v1.image.shortcuts import validate_meta, \
    load_image_from_path, get_mean_sum_and_extrema

image_router = APIRouter(prefix='/image', tags=['image'])


session = aioboto3.Session(
    aws_access_key_id='minio-root-user',
    aws_secret_access_key='minio-root-password'
)


@image_router.get(
    '/get_by_name',
    name="Получение скриншота по имени",
    responses={
        200: {
            "description": "Successful Response",
            "content": {"image/png": {}},
        }
    }
)
async def get_image(
        image_folder:  ImageTypeEnum = Query(
            ...,
            description="Папка со скриншотами",
            alias='folder'
        ),
        image_language: LanguageEnum = Query(
            ...,
            description='Язык клиента на момент создания скриншота',
            alias='language'
        ),
        image_name: str = Query(
            ...,
            description='Имя скриншота',
            alias='name'
        )
):
    """
    Получение тестового скриншота
    """
    image_path = os.path.join(
        image_folder, image_name + image_language.value + '.png')

    if os.path.exists(image_path):

        with open(image_path, 'rb') as f:
            return Response(content=f.read(), media_type="image/png")
    else:
        return UJSONResponse(
            status_code=404,
            content={
                'success': False,
                'error': f'FileNotFound: {image_path}'
            }
        )


@image_router.post(
    '/compare',
    name="Сравнение скриншотов",
    responses={
        200: {
            "description": "Screens are equal",
            "model": ImageCompareResponse
        },
        201: {
            "description": "Image saved as Origin",
            "model": ImageCompareResponse
        },
        400: {
            "description": "Invalid meta value",
            "model": ImageCompareResponse
        },
        418: {
            "description": "Compare failed",
            "model": ImageCompareResponse
        }
    }
)
async def compare(
        tasks: BackgroundTasks,
        image_name: str = Query(
            ...,
            description='Имя скриншота',
            alias='name'
        ),
        image_language: LanguageEnum = Query(
            ...,
            description='Язык клиента на момент создания скриншота',
            alias='language'
        ),
        image_file: bytes = File(
            ...,
            description='Содержимое файла скриншота',
            alias='image'
        ),
        image_size: float = Query(
            default=1.0,
            description='Масштаб клиента на момент скриншота',
            alias='size'
        ),
        test_case: str = Query(
            default=None,
            description='Название тесткейса',
            alias='test_case'
        ),
        BRANCH_NAME: str = Query(
            default=None,
            description='Название ветки клиента',
            alias='branch_name'
        ),
        node_name: str = Query(
            default=None,
            description='Названия тестового хоста',
            alias='node'
        ),
        requested_mean_sum: float = Query(
            default=0.0,
            description='Минимальная разница между скриншотами',
            alias='requested_mean_sum'
        ),
        no_report: bool = Query(
            default=False,
            description='Не отправлять репорт на фейл сравнения скриншотов'
        ),
        image_cut_region: str = Query(
            ...,
            description='Зоны, которые надо вырезать со сравниваемых скринов',
            alias='meta'
        ),
):
    """
    Сравнение скриншотов
    """
    screenshot_name = image_name + \
                 image_language
    image_from_request = Image.open(
        io.BytesIO(
            image_file
        )
    )

    origin_image_path = os.path.join('Origins', screenshot_name + '.png')

    if not os.path.exists(origin_image_path):
        logger.info(f'[screenshot_compare] '
                    f'Original image {origin_image_path} is not exist,'
                    f' save new origin image')
        image_from_request.save(origin_image_path)
        async with session.client('s3', endpoint_url='http://minio:9000') as s3:
            await s3.put_object(
                Bucket='origins',
                Body=image_from_request.tobytes(),
                ACL='public-read'
            )
        task = send_report_on_new_image_task.delay(
            node_name, BRANCH_NAME, test_case, origin_image_path
        )
        return UJSONResponse(
            status_code=201,
            content={
                "success": True,
                "image": {
                    "task_id": task.id,
                    "result": CompareEventTypeEnum.NewImageCreated,
                    "url": f"/api/v1/image/get_by_name?"
                           f"folder={ImageTypeEnum.origins.value}&"
                           f"language={image_language.value}&"
                           f"name={image_name}"
                }
            }
        )

    image_cut_region = json.loads(image_cut_region)

    if not validate_meta(image_cut_region):
        return UJSONResponse(
            status_code=400,
            content={
                "success": False,
                "image": {
                    "result": CompareEventTypeEnum.InvalidCutRegions
                }
            }
        )

    origin_image = load_image_from_path(origin_image_path)

    diff_extrema, mean_sum, diff_img = get_mean_sum_and_extrema(
        image_from_request,
        origin_image,
        image_cut_region,
        image_size
    )

    if mean_sum > requested_mean_sum and \
            (diff_extrema[0] >= 22 or diff_extrema[1] >= 22):

        image_from_request.convert('RGBA').save(
            os.path.join('Attention', screenshot_name + '.png')
        )

        diff_img = diff_img.convert('RGBA')

        pixdata = diff_img.load()

        for y in range(diff_img.size[1]):
            for x in range(diff_img.size[0]):
                if pixdata[x, y][0] <= 0 \
                    and pixdata[x, y][1] <= 0 \
                        and pixdata[x, y][2] <= 0:
                    pixdata[x, y] = (0, 0, 0, 0)

        red = Image.new('RGBA', diff_img.size, color='red')

        difference_img = Image.composite(
            red,
            diff_img,
            diff_img
        )

        diff_image_path = os.path.join(
            ImageTypeEnum.diff.value, screenshot_name + '.png')

        image_from_request_path = os.path.join(
            ImageTypeEnum.attention.value, screenshot_name + '.png'
        )

        difference_img.save(
            diff_image_path
        )

        task_id = None
        if not no_report:
            task_id = send_report_on_image_diff_task.delay(
                node_name,
                BRANCH_NAME,
                test_case,
                screenshot_name,
                mean_sum,
                requested_mean_sum,
                diff_extrema,
                origin_image_path,
                image_from_request_path,
                diff_image_path
            ).id
        return UJSONResponse(
            status_code=418,
            content={
                "success": False,
                "image": {
                    "task_id": task_id,
                    "result": CompareEventTypeEnum.FailedDiff,
                    "url": f"/api/v1/image/get_by_name?"
                           f"folder={ImageTypeEnum.diff.value}&"
                           f"language={image_language.value}&"
                           f"name={image_name}"
                }
            }
        )

    return UJSONResponse(
        content={
            "success": True,
            "image": {
                "result": CompareEventTypeEnum.OK,
                "url": f"/api/v1/image/get_by_name?"
                       f"folder={ImageTypeEnum.origins.value}&"
                       f"language={image_language.value}&"
                       f"name={image_name}"
            }
        }
    )


@image_router.delete(
    '/delete_by_name',
    name="Удаление скриншотов",
)
async def delete_image(
        image_folder:  ImageTypeEnum = Query(
            ...,
            description="Папка со скриншотами",
            alias='folder'
        ),
        image_language: LanguageEnum = Query(
            ...,
            description='Язык клиента на момент создания скриншота',
            alias='language'
        ),
        image_name: str = Query(
            ...,
            description='Имя скриншота',
            alias='name'
        )
):
    """
    Удаление тестовых скриншотов
    """
    image_path = os.path.join(image_folder, image_name + image_language + '.png')

    if os.path.exists(image_path):
        os.remove(
            image_path
        )
        return UJSONResponse(
            content={
                'success': True
            }
        )
    else:
        return UJSONResponse(
            status_code=201,
            content={
                'success': False,
                'error': f'FileNotFound: {image_path}'
            }
        )
