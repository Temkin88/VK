from datetime import datetime, timezone
from typing import Literal

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.dao.quarantine_dao import QuarantineDAO
from app.dao.tickets_dao import TicketsDAO
from app.integrations.alerts import send_quarantine_alert


class QuarantineService:
    def __init__(self, quarantine_dao: QuarantineDAO, tickets_dao: TicketsDAO):
        self.quarantine_dao = quarantine_dao
        self.tickets_dao = tickets_dao

    async def get_active(self, db: AsyncSession, project: str):
        return await self.quarantine_dao.list_active(db, project)

    async def apply_new_status(self, db: AsyncSession, pk: int, new_status: Literal["active", "inactive"]) -> None:
        await self.quarantine_dao.apply_new_status(db=db, pk=pk, new_status=new_status)

    async def recompute_activate(self, db: AsyncSession, project: str, pipeline_id: int) -> dict:
        """
        Возвращает:
        - mode: auto | pending_bulk | noop
        - activated: int
        - pending: int
        - ticket_id: str | None
        """
        now = datetime.now(timezone.utc)
        base_reason = (
            f"N{settings.quarantine_min_flaky_events}_M{settings.quarantine_min_branches}"
            f"_window{settings.quarantine_window_days}d"
        )

        candidates = await self.quarantine_dao.find_candidates_to_activate(
            db=db,
            project=project,
            window_days=settings.quarantine_window_days,
            min_flaky_events=settings.quarantine_min_flaky_events,
            min_branches=settings.quarantine_min_branches,
        )

        # ВАЖНО: исключаем уже pending+ticket_id (чтобы не алертить повторно)
        to_new_pending: list[tuple[str, datetime | None]] = []
        for test_key, flaky_count, flaky_branches, last_flaky_at in candidates:
            q = await self.quarantine_dao.get(db, project, test_key)

            if q is None:
                to_new_pending.append((test_key, last_flaky_at))
                continue

            if q.state == "active":
                continue

            if q.state == "pending" and q.ticket_id is not None:
                # уже в тикете -> не учитываем
                continue

            # inactive или pending без ticket_id
            to_new_pending.append((test_key, last_flaky_at))

        if len(to_new_pending) == 0:
            return {"mode": "noop", "activated": 0, "pending": 0, "ticket_id": None}

        # bulk -> pending ticket
        if len(to_new_pending) >= settings.quarantine_max_auto_activate:
            pending_reason = f"pending_bulk_{base_reason}"

            # (опционально) можно переиспользовать открытый тикет, чтобы не плодить
            ticket = await self.tickets_dao.get_open_pending(db, project)
            if ticket is None:
                ticket = await self.tickets_dao.create_pending(db, project, now)

            pending_count = 0
            for test_key, last_flaky_at in to_new_pending:
                q = await self.quarantine_dao.upsert_pending_with_ticket(
                    db=db,
                    project=project,
                    test_key=test_key,
                    ticket_id=ticket.id,
                    reason=pending_reason,
                    now=now,
                    last_flaky_at=last_flaky_at,
                )
                # считаем pending только если реально стало pending и привязано к тикету
                if q.state == "pending" and q.ticket_id == ticket.id:
                    pending_count += 1

            if pending_count > 0 and settings.quarantine_alert_chat_id:
                await send_quarantine_alert(
                    chat_id=settings.quarantine_alert_chat_id,
                    project=project,
                    pipeline_id=pipeline_id,
                    ticket_id=str(ticket.id),
                    count=pending_count,
                )

            return {"mode": "pending_bulk", "activated": 0, "pending": pending_count, "ticket_id": str(ticket.id)}

        # auto activate (не bulk)
        activated = 0
        for test_key, flaky_count, flaky_branches, last_flaky_at in candidates:
            q = await self.quarantine_dao.get(db, project, test_key)

            # ВАЖНО: pending с ticket_id — только вручную через тикет
            if q is not None and q.state == "pending" and q.ticket_id is not None:
                continue

            changed = await self.quarantine_dao.upsert_activate(
                db=db,
                project=project,
                test_key=test_key,
                reason=base_reason,
                now=now,
                last_flaky_at=last_flaky_at,
            )
            if changed:
                activated += 1

        return {"mode": "auto", "activated": activated, "pending": 0, "ticket_id": None}

    async def recompute_deactivate_by_observe_streak(self, db: AsyncSession, project: str) -> int:
        K = settings.quarantine_clean_observe_streak
        now = datetime.now(timezone.utc)

        active_test_keys = await self.quarantine_dao.list_active_test_keys(db, project)
        deactivated = 0

        for test_key in active_test_keys:
            last_k = await self.quarantine_dao.last_k_observe_results(db, project, test_key, K)
            if len(last_k) < K:
                continue

            all_clean = all((status == "passed" and had_failures is False) for status, had_failures in last_k)
            if all_clean:
                if await self.quarantine_dao.deactivate(db, project, test_key, now):
                    deactivated += 1

        return deactivated
