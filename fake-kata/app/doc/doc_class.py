from typing import List, Optional
from fastapi import Query, Form, UploadFile, Path

from pydantic import BaseModel

from types import MappingProxyType


class ScanState(BaseModel):

    scanId: str
    state: str


class ScansStateResponse(BaseModel):

    scans: List[ScanState]


class ScanSensorQuery:

    __slots__ = (
        'sensorId',
        'sensorInstanceId',
    )

    def __init__(
            self,
            sensorId: str = Path(
                ...,
                title='Идентификатор внешней системы',
                description='Уникальный идентификатор внешней системы, '
                            'используемый для авторизации в Kaspersky Anti '
                            'Targeted Attack Platform.',
                example='dd11a1ee-a00b-111c-b11a-11001b1f1111'
            ),
            sensorInstanceId: Optional[str] = Query(
                default='instanceId-1',
                title='Идентификатор экземпляра внешней системы',
                description='Уникальный идентификатор экземпляра внешней '
                            'системы. Экземплярами внешней системы считаются '
                            'также серверы, объединенные в кластер. '
                            'Параметр не является обязательным.',
                example='instance1'
            ),
    ):
        self.sensorId = sensorId
        self.sensorInstanceId = sensorInstanceId


class ScanQuery:

    __slots__ = (
        'scanId',
        'objectType',
        'content'
    )

    def __init__(
            self,
            scanId: str = Form(
                ...,
                title='Идентификатор запроса на проверку',
                media_type='multipart/form-data',
                description='Уникальный идентификатор запроса на проверку. '
                            'Должен быть сформирован на стороне внешней '
                            'системы. Не может содержать пробелы и '
                            'специальные символы. Не используйте имена файлов '
                            'в качестве идентификатора запроса на проверку. '
                            'Если этот параметр не указан, просмотр '
                            'результатов проверки недоступен.',
                example='1'
            ),
            objectType: Optional[str] = Form(
                title='Тип проверяемого объекта',
                media_type='multipart/form-data',
                default='file',
                description='Тип проверяемого объекта.',
                example='file'
            ),
            content: UploadFile = Form(
                ...,
                title='Содержимое проверяемого файла',
                media_type='multipart/form-data',
                description='Содержимое проверяемого объекта.'
            ),
    ):
        self.scanId = scanId
        self.objectType = objectType
        self.content = content


class ScanStateQuery:

    __slots__ = (
        'state'
    )

    def __init__(
            self,
            state: str = Query(
                ...,
                title='Список статусов проверки',
                description='Статус проверки объекта. '
                            'При указании этого параметра результаты проверки '
                            'будут отфильтрованы по статусу. '
                            'Указывайте один или несколько статусов '
                            'через запятую.',
                examples={
                    "detect": {
                        "summary": "Найдена угроза в файле",
                        "value": "detect",
                    },
                    "not detected": {
                        "summary": "Угроз в файле не найдено",
                        "value": "not detected"
                    },
                    "processing": {
                        "summary": "Файл проверяется",
                        "value": "processing"
                    },
                    "timeout": {
                        "summary": "Проверка завершилась ошибкой по таймауту",
                        "value": "timeout"
                    },
                    "error": {
                        "summary": "Проверка завершилась ошибкой",
                        "value": "error"
                    }
                }
            )
    ):
        self.state = state.split(',')


class ScanDeleteQuery:

    __slots__ = (
        'sensorId',
        'scanId'
    )

    def __init__(
            self,
            sensorId: str = Path(
                ...,
                title='Идентификатор внешней системы',
                description='Уникальный идентификатор внешней системы, '
                            'используемый для авторизации в Kaspersky Anti '
                            'Targeted Attack Platform.'
            ),
            scanId: str = Path(
                ...,
                title='Идентификатор запроса на проверку',
                description='Уникальный идентификатор запроса на проверку. '
                            'Должен быть сформирован на стороне внешней '
                            'системы. Не может содержать пробелы и '
                            'специальные символы. Не используйте имена файлов '
                            'в качестве идентификатора запроса на проверку. '
                            'Если этот параметр не указан, просмотр '
                            'результатов проверки недоступен.'
            ),
    ):
        self.sensorId = sensorId
        self.scanId = scanId


class InternalServerError(BaseModel):
    message: str


responses = MappingProxyType({
              204: {'description': 'Нет содержимого.'},
              401: {'description': 'Требуется авторизация.'},
              404: {'description': 'Не найдены результаты проверки '
                                   'по указанному идентификатору.'},
              429: {'description': 'Превышено количество запросов. '
                                   'Повторите запрос позднее.'},
              500: {
                 'description': 'Внутренняя ошибка сервера. '
                                'Повторите запрос позднее.'
              }
         })