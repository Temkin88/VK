import logging
from typing import Union

from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import UJSONResponse, Response

from app.models.database import Scan
from app.doc.doc_class import ScanStateQuery, ScansStateResponse, \
    ScanSensorQuery, responses


log = logging.getLogger('fake-kata')

router = APIRouter()


@router.get("/{sensorId}/scans/state",
            response_model=ScansStateResponse,
            responses=responses)
async def get_scans_states(
        request: Request,
        sensor: ScanSensorQuery = Depends(),
        states: ScanStateQuery = Depends(),
) -> Union[UJSONResponse, Response]:
    """
    Для создания запроса на получение результатов проверки используется
    HTTP-метод GET. Создать запрос можно, например,
    с помощью утилиты командной строки cURL.

    Вы можете задавать параметры выполнения команды cURL
    с помощью дополнительных ключей (см. таблицу ниже).

    Подробную информацию о ключах команд cURL см. в документации cURL.

    Синтаксис команды

    **curl --cert <путь к файлу TLS-сертификата>
         --key <путь к файлу закрытого ключа>
         -X GET <URL-адрес сервера с компонентом Central Node>:<порт,
         по умолчанию 443>/kata/scanner/v1/sensors/
         <идентификатор sensorId>/scans/state?
         sensorInstanceId=<идентификатор sensorInstanceId>&
         state=<один или несколько статусов проверки, которые вы хотите
         отобразить в результатах проверки>"**

    При успешной отправке запроса отобразится список запросов на проверку
    объектов и результаты проверки этих объектов. Результаты проверки будут
    отфильтрованы по статусам, которые вы указали в параметре state.
    Например, если в запросе на получение результатов проверки вы указали
    статусы **state=processing,detect**, отобразятся только запросы на проверку
    объектов, которые находятся в обработке или в которых программа
    обнаружила угрозу.
    """
    query = await Scan.filter(
        result__in=states.state,
        sensorId=sensor.sensorId,
        sensorInstanceId=sensor.sensorInstanceId
    )

    scans = [
        {
            'scanId': model.scanId,
            'state': model.result
        } for model in query
    ]

    log.warning(f'Returned scan results for {sensor.sensorId}: {scans}')

    return UJSONResponse(
        {
            'scans':  scans
        }
    )
