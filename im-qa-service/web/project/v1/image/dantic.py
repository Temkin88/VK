from enum import Enum
from typing import Optional

from pydantic import BaseModel, AnyHttpUrl

from web.project.common_dantic import BaseResponseModel


class ImageTypeEnum(str, Enum):
    origins = 'Origins'
    attention = 'Attention'
    diff = 'Difference'


class LanguageEnum(str, Enum):
    ru = 'ru'
    en = 'en'


class CompareEventTypeEnum(str, Enum):
    OK = "OK"
    NewImageCreated = "NewImageCreated"
    FailedDiff = "FailedDiff"
    InvalidCutRegions = "InvalidCutRegions"


class CompareEvent(BaseModel):
    result: CompareEventTypeEnum
    url: Optional[AnyHttpUrl] = None


class ImageCompareResponse(BaseResponseModel):
    image: Optional[CompareEvent]
