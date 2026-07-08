import uuid

from pydantic import Field

from web.project.common_dantic import BaseResponseModel


class AllureCloseResponseModel(BaseResponseModel):
    """
    Модель успешного ответа на запрос очистки аккаунта
    """
    task_id: uuid.UUID = Field(..., description='ID задачи')
