import base64
import orjson

from loguru import logger


def encode(obj: str | bytes | dict) -> str:
    """
    Encode input object to base64 string
    :param obj: Any
    :return: base64 string
    """

    logger.debug(f"obj: {obj}, type: {type(obj)}")

    if not isinstance(obj, (str, bytes, dict)):
        raise ValueError(f"Wrong object type for encoding: {type(obj)}")

    if isinstance(obj, dict):
        obj = orjson.dumps(obj)

    if isinstance(obj, str):
        obj = obj.encode(encoding="utf-8")

    return base64.b64encode(obj).decode("utf-8")
