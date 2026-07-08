import uuid
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Ticket


class TicketsDAO:
    async def create_pending(self, db: AsyncSession, project: str, now: datetime) -> Ticket:
        t = Ticket(project=project, state="pending", created_at=now, resolved_at=None)
        db.add(t)
        return t

    async def get(self, db: AsyncSession, ticket_id: uuid.UUID) -> Ticket | None:
        return await db.get(Ticket, ticket_id)

    async def get_open_pending(self, db: AsyncSession, project: str) -> Ticket | None:
        q = (
            select(Ticket)
            .where(Ticket.project == project, Ticket.state == "pending")
            .order_by(Ticket.created_at.desc())
            .limit(1)
        )
        return (await db.execute(q)).scalars().first()

    async def resolve(self, ticket: Ticket, now: datetime) -> None:
        ticket.state = "resolved"
        ticket.resolved_at = now
