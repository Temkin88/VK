from enum import Enum

from web.project.common_dantic import BaseResponseModel
from web.project.db import Product_Pydantic


class ProductTypeEnum(str, Enum):
    agent = 'agent'
    armgs = 'armgs'
    icq = 'icq'
    myteam = 'myteam'
    myteam_onpremise = 'myteam_onpremise'


class ProductResponseModel(BaseResponseModel):
    product: Product_Pydantic
