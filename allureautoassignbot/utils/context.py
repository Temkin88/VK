from contextvars import ContextVar
from typing import Optional

ChatIdContextVar: ContextVar[Optional[str]] = ContextVar("chat_id", default=None)
