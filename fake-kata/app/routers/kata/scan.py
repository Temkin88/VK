import json
import asyncio

import logging
from typing import Optional

from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi.responses import Response

from app.doc.doc_class import ScanSensorQuery, ScanQuery, responses
from app.models.database import Scan


log = logging.getLogger('fake-kata')


router = APIRouter()


async def process_file(file_body: Optional[bytes], virus: bool, model: Scan):

    try:
        log.info(f'Trying to process scanId: {model.scanId}')

        file_json = json.loads(file_body)

        for key in ('awaited result', 'proccesing time'):
            assert key in file_json, f"Key '{key}' not file body"

        assert file_json['awaited result'] in (
                'error',
                'timeout',
                'detect',
                'not detected'
        ), "Awaited result has wrong value"

        processing_timeout = file_json['proccesing time']

        log.warning(f"SensorId: {model.sensorId}, Waiting {processing_timeout} seconds for file ID {model.scanId}")
        if processing_timeout > 0:
            model.result = 'processing'
            await model.save()

        await asyncio.sleep(processing_timeout)
        log.warning(f"SensorId: {model.sensorId}, Waiting {processing_timeout} seconds for file ID {model.scanId} (over)")

        model.result = file_json['awaited result']

        await model.save()

        log.warning(
            f'SensorId: {model.sensorId}, '
            f'ScanId: {model.scanId}, '
            f'result: {model.result}, '
            f'timeout: {file_json["proccesing time"]}'
        )

    except Exception as error:
        log.exception(error)

        model.result = 'not detected'
        await model.save()
        log.warning(
            f'SensorId: {model.sensorId}, ScanId: {model.scanId}, result: {model.result}, error: {error}'
        )


@router.post("/{sensorId}/scans", responses=responses)
async def scan_file_content(
        background_tasks: BackgroundTasks,
        sensor: ScanSensorQuery = Depends(),
        scan: ScanQuery = Depends(),
) -> Response:
    """
    Запрос на проверку объектов

    Для создания запроса на проверку объектов используется HTTP-метод POST.
    Создать запрос можно, например, с помощью утилиты командной строки cURL.

    Вы можете задавать параметры выполнения команды cURL с помощью
    дополнительных ключей (см. таблицу ниже).

    Подробную информацию о ключах команд cURL см. в документации cURL.

    Синтаксис команды

    **curl --cert <путь к файлу TLS-сертификата>
         --key <путь к файлу закрытого ключа>
         -X POST "<URL-адрес сервера с компонентом Central Node>:<порт,
         по умолчанию 443>/kata/scanner/v1/sensors/<идентификатор sensorId>/
         scans?sensorInstanceId=<идентификатор sensorInstanceId>"
         -F "content=<путь к файлу, который вы хотите проверить>"
         -F scanID=<идентификатор запроса на проверку>
         -F "objectType=file"**

    При успешной обработке запроса отобразится статус "OK".
    """

    model, _ = await Scan.get_or_create(
        scanId=scan.scanId,
        sensorId=sensor.sensorId,
        sensorInstanceId=sensor.sensorInstanceId
    )

    file_body = await scan.content.read()

    file_body_len = len(file_body)

    if file_body_len > 1000:
        file_body_len /= 100000

    background_tasks.add_task(
        process_file,
        file_body if file_body_len <= 256 else None,
        b'virus' in file_body or b'VIRUS' in file_body,
        model
    )

    return Response()
