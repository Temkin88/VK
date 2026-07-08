from fastapi import APIRouter
from fastapi.responses import UJSONResponse, Response

from app.models.database import Error


router = APIRouter()


@router.get('/error/get')
async def get_all_errors():
    """
    Получаем список всех зарегистрированных ошибок
    """

    errors = []

    async for error in Error.all():
        errors.append(
            {
                'uuid': error.uuid,
                'msg': error.exc_msg
            }
        )

    return UJSONResponse(
        {
            'errors': errors
        }
    )


@router.get('/error/{uuid)')
async def get_single_error(uuid: str):

    model = await Error.get_or_none(
        uuid=uuid
    )

    if model:

        return UJSONResponse(
            {
                'error': {
                    'uuid': model.uuid,
                    'exc_msg': model.exc_msg,
                    'traceback': model.traceback,
                    'datetime': str(model.datetime)
                }
            }
        )
    else:
        return Response(
            status_code=404
        )
