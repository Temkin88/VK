from datetime import datetime, timezone
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db, require_api_key
from app.dao.quarantine_dao import QuarantineDAO
from app.schemas.quarantine import QuarantineOut, QuarantineItemOut

router = APIRouter()

@router.get("/api/v1/quarantine", response_model=QuarantineOut, dependencies=[Depends(require_api_key)])
async def get_quarantine(project: str, db: AsyncSession = Depends(get_db)):
    qdao = QuarantineDAO()
    rows = await qdao.list_active(db, project)
    return QuarantineOut(
        project=project,
        generated_at=datetime.now(timezone.utc),
        quarantined=[QuarantineItemOut(test_key=t, reason=r) for t, r in rows],
    )
