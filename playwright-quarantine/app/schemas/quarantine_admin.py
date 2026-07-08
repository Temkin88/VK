from datetime import datetime
from pydantic import BaseModel, Field
from typing import Literal


class QuarantineActionIn(BaseModel):
    project: str
    test_keys: list[str] = Field(min_length=1)


class QuarantineActionOut(BaseModel):
    status: Literal["ok"]
    updated: int
    skipped: int
    not_found: int
    project: str
    at: datetime
