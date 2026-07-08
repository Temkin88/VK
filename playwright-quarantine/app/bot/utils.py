import base64
from typing import Optional

from loguru import logger


def decode_cmd(cmd: str) -> Optional[str]:
    logger.debug(f"decode cmd: {cmd}")
    try:
        cmd = base64.b64decode(cmd).decode("utf-8")
        logger.debug(f"decode cmd: {cmd}")
        return cmd
    except Exception as e:
        logger.debug(f"Failed to decode: {e}")
        return None
