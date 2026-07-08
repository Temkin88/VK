from datetime import datetime
from pydantic import BaseModel
from typing import Literal


class TicketResolveIn(BaseModel):
    project: str
    ticket_id: str
    decision: Literal["active", "inactive"]


class TicketResolveOut(BaseModel):
    status: Literal["ok"]
    updated: int
    ticket_id: str
    ticket_state: Literal["resolved"]
    at: datetime
