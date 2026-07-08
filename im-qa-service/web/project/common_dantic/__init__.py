from pydantic import BaseModel, Field


example_exception = Exception('Example exception')


class BaseResponseModel(BaseModel):
    """
    Базовая модель ответа на запрос
    """
    success: bool = Field(..., description='Успешность запроса')


class FailedResponseModel(BaseModel):
    """
    Ответ при ошибке обработки запроса
    """
    success: bool = Field(False, description='Успешность запроса')
    error: str = Field(
        description='Ошибка обработки запроса',
        default=f'{type(example_exception).__name__}: {str(example_exception)}'
    )
