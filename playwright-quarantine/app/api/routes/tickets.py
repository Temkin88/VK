from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db, require_api_key
from app.dao.tickets_dao import TicketsDAO
from app.dao.quarantine_dao import QuarantineDAO
from app.schemas.tickets import TicketResolveIn, TicketResolveOut
from app.services.tickets_service import TicketsService

router = APIRouter()

def svc() -> TicketsService:
    return TicketsService(TicketsDAO(), QuarantineDAO())

@router.post("/api/v1/tickets/resolve", response_model=TicketResolveOut, dependencies=[Depends(require_api_key)])
async def resolve_ticket(payload: TicketResolveIn, db: AsyncSession = Depends(get_db)):
    updated = await svc().resolve(db, payload.project, payload.ticket_id, payload.decision)
    await db.commit()
    return TicketResolveOut(
        status="ok",
        updated=updated,
        ticket_id=payload.ticket_id,
        ticket_state="resolved",
        at=datetime.now(timezone.utc),
    )
