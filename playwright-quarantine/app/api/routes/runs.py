from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db, require_api_key
from app.dao.quarantine_dao import QuarantineDAO
from app.dao.runs_dao import RunsDAO
from app.dao.test_stats_dao import TestStatsDAO
from app.dao.tickets_dao import TicketsDAO
from app.schemas.runs import RunIn, IngestRunOut, ActivatedRecomputeResult
from app.services.quarantine_service import QuarantineService
from app.services.runs_service import RunsService

router = APIRouter()

def build_runs_service() -> RunsService:
    qdao = QuarantineDAO()
    tdao = TicketsDAO()
    quarantine_service = QuarantineService(quarantine_dao=qdao, tickets_dao=tdao)
    return RunsService(
        runs_dao=RunsDAO(),
        test_stats_dao=TestStatsDAO(),
        quarantine_service=quarantine_service,
    )

@router.post("/api/v1/runs", response_model=IngestRunOut, dependencies=[Depends(require_api_key)])
async def ingest_run(payload: RunIn, db: AsyncSession = Depends(get_db)):
    svc = build_runs_service()
    dedup, activated, deactivated = await svc.ingest_run(db, payload)
    activated_model = ActivatedRecomputeResult.model_validate(activated)
    await db.commit()
    return IngestRunOut(status="ok", dedup=dedup, activated=activated_model, deactivated=deactivated)
