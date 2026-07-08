from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import Response

from app.models.database import Scan
from app.doc.doc_class import ScanDeleteQuery, responses


router = APIRouter()


@router.delete("/{sensorId}/scans/{scanId}", responses=responses)
async def delete_scan_result(
        request: Request,
        delete: ScanDeleteQuery = Depends()
) -> Response:
    """
    Для создания запроса на удаление результатов проверки одного или
    нескольких объектов используется метод **DELETE**. Создать запрос можно,
    например, с помощью утилиты командной строки cURL.

    Синтаксис команды

     **curl --cert <путь к файлу TLS-сертификата>
         --key <путь к файлу закрытого ключа>
         -X DELETE "<URL-адрес сервера с компонентом Central Node>:<порт,
         по умолчанию 443>/kata/scanner/v1/sensors/
         <идентификатор sensorId>/scans/<идентификатор scanId>"**

    При успешной обработке запроса результаты проверки объекта будут удалены.
    Отобразится статус "OK".
    """
    model = await Scan.get_or_none(
        sensorId=delete.sensorId,
        scanId=delete.scanId
    )

    if model:
        await model.delete()

        return Response()
    else:

        return Response(
            status_code=404
        )
