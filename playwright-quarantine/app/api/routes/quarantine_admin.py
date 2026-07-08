from datetime import datetime, timezone
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db, require_api_key
from app.dao.quarantine_dao import QuarantineDAO
from app.schemas.quarantine_admin import QuarantineActionIn, QuarantineActionOut
from app.schemas.quarantine import QuarantineOut, QuarantineItemOut
from app.services.quarantine_admin_service import QuarantineAdminService

router = APIRouter()

def svc() -> QuarantineAdminService:
    return QuarantineAdminService(QuarantineDAO())

@router.get(
    "/api/v1/quarantine/pending",
    response_model=QuarantineOut,
    dependencies=[Depends(require_api_key)],
)
async def get_pending(project: str, db: AsyncSession = Depends(get_db)):
    items = await svc().list_pending(db, project)
    return QuarantineOut(
        project=project,
        generated_at=datetime.now(timezone.utc),
        quarantined=[QuarantineItemOut(test_key=q.test_key, reason=q.reason) for q in items],
    )

@router.post("/api/v1/quarantine/approve", response_model=QuarantineActionOut, dependencies=[Depends(require_api_key)])
async def approve(payload: QuarantineActionIn, db: AsyncSession = Depends(get_db)):
    updated, skipped, not_found = await svc().approve(db, payload.project, payload.test_keys)
    await db.commit()
    return QuarantineActionOut(
        status="ok",
        updated=updated,
        skipped=skipped,
        not_found=not_found,
        project=payload.project,
        at=datetime.now(timezone.utc),
    )

@router.post("/api/v1/quarantine/reject", response_model=QuarantineActionOut, dependencies=[Depends(require_api_key)])
async def reject(
    payload: QuarantineActionIn,
    mode: str = Query(default="inactive", pattern="^(inactive|delete)$"),
    db: AsyncSession = Depends(get_db),
):
    service = svc()
    if mode == "delete":
        updated, skipped, not_found = await service.reject_delete(db, payload.project, payload.test_keys)
    else:
        updated, skipped, not_found = await service.reject_to_inactive(db, payload.project, payload.test_keys)

    await db.commit()
    return QuarantineActionOut(
        status="ok",
        updated=updated,
        skipped=skipped,
        not_found=not_found,
        project=payload.project,
        at=datetime.now(timezone.utc),
    )
