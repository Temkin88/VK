import uuid
from datetime import datetime, timezone

from fastapi import HTTPException
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.tickets_dao import TicketsDAO
from app.dao.quarantine_dao import QuarantineDAO


class TicketsService:
    def __init__(self, tickets_dao: TicketsDAO, quarantine_dao: QuarantineDAO):
        self.tickets_dao = tickets_dao
        self.quarantine_dao = quarantine_dao

    async def resolve(self, db: AsyncSession, project: str, ticket_id: str, decision: str) -> int:
        try:
            tid = uuid.UUID(ticket_id)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid ticket_id")

        ticket = await self.tickets_dao.get(db, tid)
        if ticket is None or ticket.project != project:
            raise HTTPException(status_code=404, detail="Ticket not found")

        if ticket.state != "pending":
            raise HTTPException(status_code=409, detail="Ticket already resolved")

        if decision not in ("active", "inactive"):
            raise HTTPException(status_code=400, detail="Invalid decision")

        now = datetime.now(timezone.utc)
        updated = await self.quarantine_dao.apply_ticket_decision(
            db=db,
            project=project,
            ticket_id=tid,
            target_state=decision,
            now=now,
        )
        await self.tickets_dao.resolve(ticket, now)
        return updated

    async def resolve_from_admin(self, db: AsyncSession, ticket_id: str, decision: str) -> int:
        logger.debug(f"resolve_from_admin => ticket_id: {ticket_id} decision: {decision}")
        try:
            tid = uuid.UUID(ticket_id)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid ticket_id")

        ticket = await self.tickets_dao.get(db, tid)
        logger.debug(f"resolve_from_admin => ticket_id: {ticket.id} project: {ticket.project}")

        if ticket.state != "pending":
            raise HTTPException(status_code=409, detail="Ticket already resolved")

        if decision not in ("active", "inactive"):
            raise HTTPException(status_code=400, detail="Invalid decision")

        now = datetime.now(timezone.utc)
        updated = await self.quarantine_dao.apply_ticket_decision(
            db=db,
            project=ticket.project,
            ticket_id=tid,
            target_state=decision,
            now=now,
        )
        await self.tickets_dao.resolve(ticket, now)
        return updated
