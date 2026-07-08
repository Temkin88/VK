import io
import os
from _socket import gethostname
from typing import Type

import allure
import pytest
from PIL import Image

from fastapi.testclient import TestClient

from web.project.v1.image import ImageTypeEnum, LanguageEnum, \
    CompareEventTypeEnum
from web.project.v1.image.shortcuts import image_to_BytesIO, validate_meta
from web.project.v1.image.tasks import \
    send_report_on_new_image, \
    send_report_on_image_diff


@pytest.mark.anyio
@allure.suite("Действия со скриншотами")
@allure.feature("Вспомогательные функции")
@allure.title("Преобразование из PIL.Image в io.BytesIO")
async def test_image_to_BytesIO(
        get_test_image_pil_image: Image
):
    """
    Проверка функции преобразования из PIL.Image в io.BytesIO
    """
    with allure.step("Вызываем image_to_BytesIO"):
        test_image_bytes_io = image_to_BytesIO(get_test_image_pil_image)

    with allure.step("Проверяем что вернулся io.BytesIO"):
        assert isinstance(test_image_bytes_io, io.BytesIO)


@pytest.mark.parametrize("meta,result", [
    ("{}", False),
    ("[[null, null, null, null]]", False),
    ([[100, 100, 100], [100, 100, 100, 100]], False),
    ([[100, 100, 100, 100], [100, 100, 100, 100]], True)
])
@pytest.mark.anyio
@allure.suite("Действия со скриншотами")
@allure.feature("Вспомогательные функции")
@allure.title("Валидация meta")
async def test_validate_meta_fail(
        meta,
        result: bool
):
    assert validate_meta(meta) == result


@pytest.mark.anyio
@allure.suite("Действия со скриншотами")
@allure.feature("Вспомогательные функции")
@allure.title("Отправка репорта на новый скриншот")
async def test_send_report_on_new_image(
        get_test_image_bytes: bytes
):
    """
    Проверка отправки репорта при сохранении нового изображения
    """
    with allure.step("Вызываем send_report_on_new_image"):
        result = send_report_on_new_image(
            node_name=gethostname(),
            BRANCH_NAME='master',
            screenshot_name='test',
            screenshot_bytes=os.path.join('tests', 'support', 'test.png')
        )
        assert result


@pytest.mark.anyio
@allure.suite("Действия со скриншотами")
@allure.feature("Вспомогательные функции")
@allure.title("Отправка репорта на ошибку сравнения скриншотов")
async def test_send_report_on_image_diff(
        get_test_image_pil_image: Image
):
    """
    Проверка отправки репорта при разнице между присланным и сохраненным скриншотами
    """
    with allure.step("Вызываем send_report_on_image_diff"):
        result = send_report_on_image_diff(
            node_name=gethostname(),
            BRANCH_NAME='master',
            test_case='test_test',
            screenshot_name='test',
            mean_sum=0.0,
            requested_mean_sum=1.0,
            diff=0.0,
            original_image=os.path.join('tests', 'support', 'test.png'),
            image_from_request=os.path.join('tests', 'support', 'test.png'),
            diff_image=os.path.join('tests', 'support', 'test.png')
        )
        assert result


@pytest.mark.parametrize("language", LanguageEnum)
@pytest.mark.parametrize("folder", ImageTypeEnum)
@pytest.mark.anyio
@allure.suite("Действия со скриншотами")
@allure.feature("Методы")
@allure.title("Ошибка получение несохраненного изображения")
async def test_get_image_fail(
        client: TestClient,
        folder: Type[ImageTypeEnum],
        language: Type[LanguageEnum]
):
    """
    Проверка ошибки получения несуществующего скриншота
    """
    IMAGE_NAME = 'ekekekekekekekqwfqfqefgqevqev'

    image_path = os.path.join(folder, IMAGE_NAME + language.value + '.png')

    with allure.step(f"Подчищаем {image_path}"):
        if os.path.exists(image_path):
            os.remove(image_path)

    with allure.step("Делаем запрос [GET] /api/v1/image/get_by_name"):
        response = client.get(
            url='/api/v1/image/get_by_name',
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                'folder': folder.value,
                'language': language.value,
                'name': IMAGE_NAME
            }
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 404, \
            f"Status: {response.status_code} - {response.text}"
        assert not response.json()["success"]
        assert 'FileNotFound' in response.json()["error"]
        assert IMAGE_NAME in response.json()["error"]


@pytest.mark.parametrize("language", LanguageEnum)
@pytest.mark.parametrize("folder", ImageTypeEnum)
@pytest.mark.anyio
@allure.suite("Действия со скриншотами")
@allure.feature("Методы")
@allure.title("Успешное получение скриншота по ссылке из папки {folder} ({language})")
async def test_get_image_success(
        client: TestClient,
        folder: Type[ImageTypeEnum],
        language: Type[LanguageEnum],
        get_test_image_pil_image: Image
):
    """
    Проверка успешного сравнения скриншотов
    """
    IMAGE_NAME = 'ekekekekekekek'

    image_path = os.path.join(folder, IMAGE_NAME + language.value + '.png')

    with allure.step(f"Создаем изображение в {image_path}"):
        with open(image_path, 'wb') as f:
            get_test_image_pil_image.save(
                f
            )
    with allure.step("Делаем запрос [GET] /api/v1/image/get_by_name"):
        response = client.get(
            url='/api/v1/image/get_by_name',
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                'folder': folder.value,
                'language': language.value,
                'name': IMAGE_NAME
            }
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"


@pytest.mark.parametrize("language", LanguageEnum)
@pytest.mark.parametrize("no_report", [True, False], ids=('no_report', 'report'))
@pytest.mark.anyio
@allure.suite("Действия со скриншотами")
@allure.feature("Методы")
@allure.title("Сохранение нового скриншота")
async def test_compare_new_image(
        client: TestClient,
        get_test_image_bytes_IO: io.BytesIO,
        language: Type[LanguageEnum],
        no_report: bool
):
    """
    Проверка сохранения скринщота если скриншота с таким названием нет в указанной папке
    """
    IMAGE_NAME = 'ekekekekekekek'

    image_path = os.path.join(
        ImageTypeEnum.origins.value, IMAGE_NAME + language.value + '.png')

    with allure.step(f"Подчищаем {image_path}"):
        if os.path.exists(image_path):
            os.remove(image_path)
    with allure.step("Делаем запрос [POST] /api/v1/image/compare"):
        response = client.post(
            url='/api/v1/image/compare',
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                'name': IMAGE_NAME,
                'language': language.value,
                'size': 1.0,
                'requested_mean_sum': 0.1,
                'no_report': no_report,
                'meta': [[0, 0, 100, 100]]
            },
            files={
                'image': get_test_image_bytes_IO
            }
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 201, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json() == {
            "success": True,
            "image": {
                "result": "NewImageCreated",
                "url": f"/api/v1/image/get_by_name?"
                       f"folder={ImageTypeEnum.origins.value}&"
                       f"language={language.value}&"
                       f"name={IMAGE_NAME}"
            }
        }
        assert os.path.exists(image_path)


@pytest.mark.parametrize("language", LanguageEnum)
@pytest.mark.parametrize("no_report", [True, False], ids=('no_report', 'report'))
@pytest.mark.anyio
@allure.suite("Действия со скриншотами")
@allure.feature("Методы")
@allure.title("Успешное сравнение сохранненого скриншота с присланным")
async def test_compare_existing_image_success(
        client: TestClient,
        get_test_image_pil_image: Image,
        get_test_image_bytes_IO: io.BytesIO,
        language: Type[LanguageEnum],
        no_report: bool
):
    """
    Проверка успешности сравнения при одинаковости скриншотов (имеющегося и присланного)
    """
    IMAGE_NAME = 'ekekekekekekek'

    image_path = os.path.join(
        ImageTypeEnum.origins.value, IMAGE_NAME + language.value + '.png')

    with allure.step(f"Создаем изображение в {image_path}"):
        with open(image_path, 'wb') as f:
            get_test_image_pil_image.save(
                f
            )

    with allure.step("Делаем запрос [POST] /api/v1/image/compare"):
        response = client.post(
            url='/api/v1/image/compare',
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                'name': IMAGE_NAME,
                'language': language.value,
                'size': 1.0,
                'requested_mean_sum': 0.1,
                'no_report': no_report,
                'meta': str([[0, 0, 100, 100]])
            },
            files={
                'image': get_test_image_bytes_IO
            }
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json() == {
            "success": True,
            "image": {
                "result": "OK",
                "url": f"/api/v1/image/get_by_name?"
                       f"folder={ImageTypeEnum.origins.value}&"
                       f"language={language.value}&"
                       f"name={IMAGE_NAME}"
            }
        }


@pytest.mark.parametrize("language", LanguageEnum)
@pytest.mark.parametrize("no_report", [True, False], ids=('no_report', 'report'))
@pytest.mark.anyio
@allure.suite("Действия со скриншотами")
@allure.feature("Методы")
@allure.title("Ошибка расшифровки meta")
async def test_compare_existing_image_fail_decode_meta(
        client: TestClient,
        get_test_image_pil_image: Image,
        get_test_image_bytes_IO: io.BytesIO,
        language: Type[LanguageEnum],
        no_report: bool
):
    """
    Проверка ошибки при неверном значении meta
    """
    IMAGE_NAME = 'ekekekekekekek'

    image_path = os.path.join(
        ImageTypeEnum.origins.value, IMAGE_NAME + language.value + '.png')

    with allure.step(f"Создаем изображение в {image_path}"):
        with open(image_path, 'wb') as f:
            get_test_image_pil_image.save(
                f
            )

    image_cut_region = [[0, 0, 100, 100]]

    with allure.step("Делаем запрос [POST] /api/v1/image/compare"):
        response = client.post(
            url='/api/v1/image/compare',
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                'name': IMAGE_NAME,
                'language': language.value,
                'size': 1.0,
                'requested_mean_sum': 0.1,
                'no_report': no_report,
                'meta': image_cut_region
            },
            files={
                'image': get_test_image_bytes_IO
            }
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 400, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json() == {
            "success": False,
            "image": {
                "result": CompareEventTypeEnum.InvalidCutRegions
            }
        }


@pytest.mark.parametrize("language", LanguageEnum)
@pytest.mark.parametrize("no_report", [True, False], ids=('no_report', 'report'))
@pytest.mark.anyio
@allure.suite("Действия со скриншотами")
@allure.feature("Методы")
@allure.title("Возврат разницы между сохраненным и присланным скриншотами")
async def test_compare_existing_image_fail_diff_image(
        client: TestClient,
        get_test_image_pil_image: Image,
        get_test_image_bytes_IO: io.BytesIO,
        get_test_alter_image_pil_image: Image,
        get_test_alter_image_bytes_IO: io.BytesIO,
        language: Type[LanguageEnum],
        no_report: bool
):
    """
    Проверка отправки разницы при сравнении разных скриншотов
    """
    IMAGE_NAME = 'ekekekekekekek'

    image_path = os.path.join(
        ImageTypeEnum.origins.value, IMAGE_NAME + language.value + '.png')
    alter_image_path = os.path.join(
        ImageTypeEnum.attention.value, IMAGE_NAME + language.value + '.png')

    with allure.step(f"Создаем изображение в {image_path}"):
        with open(image_path, 'wb') as f:
            get_test_image_pil_image.save(
                f
            )
    with allure.step(f"Подчищаем изображение в {alter_image_path}"):
        if os.path.exists(alter_image_path):
            os.remove(alter_image_path)

    with allure.step("Делаем запрос [POST] /api/v1/image/compare"):
        response = client.post(
            url='/api/v1/image/compare',
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                'name': IMAGE_NAME,
                'language': language.value,
                'size': 1.0,
                'requested_mean_sum': 0.1,
                'no_report': no_report,
                'meta': str([[0, 0, 100, 100]])
            },
            files={
                'image': get_test_alter_image_bytes_IO
            }
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 418, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json() == {
            "success": False,
            "image": {
                "result": "FailedDiff",
                "url": f"/api/v1/image/get_by_name?"
                       f"folder={ImageTypeEnum.diff.value}&"
                       f"language={language.value}&"
                       f"name={IMAGE_NAME}"
            }
        }

    with allure.step(f"Проверяем наличие изображения {alter_image_path}"):
        assert os.path.exists(alter_image_path), \
            f'New image not saved to "{alter_image_path}"'


@pytest.mark.parametrize("language", LanguageEnum)
@pytest.mark.parametrize("folder", ImageTypeEnum)
@pytest.mark.anyio
@allure.suite("Действия со скриншотами")
@allure.feature("Методы")
@allure.title("Ошибка удаление несуществующего скриншота")
async def test_delete_image_not_existing(
        client: TestClient,
        folder: Type[ImageTypeEnum],
        language: Type[LanguageEnum]
):
    """
    Проверка возникновения ошибки при удалении скриншота,
    несуществующего в папках Origins/Attention
    """
    IMAGE_NAME = 'ekekekekekekek'

    image_path = os.path.join(
        folder.value, IMAGE_NAME + language + '.png')

    with allure.step(f"Подчищаем изображение {image_path}"):
        if os.path.exists(image_path):
            os.remove(image_path)

    with allure.step("Делаем запрос [DELETE] /api/v1/image/delete_by_name"):
        response = client.delete(
            url='/api/v1/image/delete_by_name',
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                'folder': folder.value,
                'language': language.value,
                'name': IMAGE_NAME
            }
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 201, \
            f"Status: {response.status_code} - {response.text}"
        assert not response.json()["success"]
        assert 'FileNotFound' in response.json()["error"]


@pytest.mark.parametrize("language", LanguageEnum)
@pytest.mark.parametrize("folder", ImageTypeEnum)
@pytest.mark.anyio
@allure.suite("Действия со скриншотами")
@allure.feature("Методы")
@allure.title("Успешное удаление скриншота")
async def test_delete_image_success(
        client: TestClient,
        get_test_image_pil_image: Image,
        folder: Type[ImageTypeEnum],
        language: Type[LanguageEnum]
):
    """
    Проверка успешного удаления скриншота, существующего в папках Origins/Attention
    """
    IMAGE_NAME = 'ekekekekekekek'

    image_path = os.path.join(
        folder.value, IMAGE_NAME + language + '.png')

    with allure.step(f"Создаем изображение {image_path}"):
        with open(image_path, 'wb') as f:
            get_test_image_pil_image.save(
                f
            )
    with allure.step("Делаем запрос [DELETE] /api/v1/image/delete_by_name"):
        response = client.delete(
            url='/api/v1/image/delete_by_name',
            headers={
                'X-Token': 'X-Tests'
            },
            params={
                'folder': folder.value,
                'language': language.value,
                'name': IMAGE_NAME
            }
        )
    with allure.step(f"Проверяем {response}"):
        assert response.status_code == 200, \
            f"Status: {response.status_code} - {response.text}"
        assert response.json()["success"]
    with allure.step(f"Проверяем удаление {image_path}"):
        assert not os.path.exists(image_path), \
            f"Скриншот {image_path} не удален"

