from pydantic import BaseModel
from loguru import logger

import utils


class CustomBaseModel(BaseModel):
    @classmethod
    def base64_validate(cls, data: str | bytes):
        logger.debug(f"data: {data}")
        return cls(**utils.decode.decode_dict(data))

    def base64_dump(self, **kwargs) -> str:
        model_dump = self.json(**kwargs)

        logger.debug(f"model_dump: {model_dump}")

        return utils.encode.encode(model_dump)
