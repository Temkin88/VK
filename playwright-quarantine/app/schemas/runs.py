from datetime import datetime
from pydantic import BaseModel, Field
from typing import Literal, Optional


class TestStatIn(BaseModel):
    test_key: str
    final_status: Literal["passed", "failed", "skipped"]
    had_failures: bool
    attempts: int = Field(ge=1)
    failures_count: int = Field(ge=0)
    duration_ms: Optional[int] = Field(default=None, ge=0)


class RunIn(BaseModel):
    project: str
    pipeline_id: int
    commit_sha: str
    branch: str
    mode: Literal["gated", "observe"]
    created_at: datetime
    tests: list[TestStatIn]


class ActivatedRecomputeResult(BaseModel):
    mode: Literal["pending_bulk", "auto", "noop"]
    activated: int = 0
    pending: int = 0


class IngestRunOut(BaseModel):
    status: Literal["ok"]
    dedup: bool = False
    activated: ActivatedRecomputeResult
    deactivated: int = 0
