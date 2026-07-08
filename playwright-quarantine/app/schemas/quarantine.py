from datetime import datetime
from pydantic import BaseModel


class QuarantineItemOut(BaseModel):
    test_key: str
    reason: str


class QuarantineOut(BaseModel):
    project: str
    generated_at: datetime
    quarantined: list[QuarantineItemOut]
