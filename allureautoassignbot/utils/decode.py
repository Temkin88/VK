import base64
import orjson

from loguru import logger


def decode_bytes(obj: str | bytes) -> bytes:
    """
    Decode base64 string to bytes
    :param obj: base64 string
    :return: bytes
    """

    logger.debug(f"obj: {obj}, type: {type(obj)}")

    if isinstance(obj, str):
        obj = obj.encode(encoding="utf-8")

    return base64.b64decode(obj)


def decode_dict(obj: str | bytes) -> dict:
    """
    Decode base64 string to dict
    :param obj: base64 string
    :return: dict
    """

    proxy_obj = decode_bytes(obj=obj)

    return orjson.loads(proxy_obj)


def decode_string(obj: str | bytes) -> str:
    """
    Decode base64 string to string
    :param obj: base64 string
    :return: string
    """

    return decode_bytes(obj=obj).decode(encoding="utf-8")
