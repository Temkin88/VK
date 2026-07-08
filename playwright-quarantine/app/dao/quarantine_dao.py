import uuid
from datetime import datetime, timedelta, timezone
from typing import Literal

from fastapi import HTTPException
from sqlalchemy import select, func, distinct, or_, literal, desc, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Run, TestStat, Quarantine


class QuarantineDAO:
    @staticmethod
    def counted_branch_clause():
        return or_(
            Run.branch == "develop",
            Run.branch.like("release/%"),
            Run.branch.like("task/%"),
        )

    async def list_active(self, db: AsyncSession, project: str) -> list[tuple[str, str]]:
        q = (
            select(Quarantine.test_key, Quarantine.reason)
            .where(Quarantine.project == project, Quarantine.state == "active")
            .order_by(Quarantine.test_key.asc())
        )
        return (await db.execute(q)).all()

    async def get(self, db: AsyncSession, project: str, test_key: str) -> Quarantine | None:
        q = (
            select(Quarantine)
            .where(Quarantine.project == project, Quarantine.test_key == test_key)
            .limit(1)
        )
        return (await db.execute(q)).scalars().first()

    async def upsert_activate(
        self,
        db: AsyncSession,
        project: str,
        test_key: str,
        reason: str,
        now: datetime,
        last_flaky_at: datetime | None,
    ) -> bool:
        q = await self.get(db, project, test_key)
        if q is None:
            q = Quarantine(
                project=project,
                test_key=test_key,
                state="active",
                reason=reason,
                activated_at=now,
                last_flaky_at=last_flaky_at,
                deactivated_at=None,
                ticket_id=None,
            )
            db.add(q)
            return True

        if q is not None and q.state == "pending" and q.ticket_id is not None:
            # pending в рамках тикета нельзя активировать автоматически
            return False

        changed = False
        if q.state != "active":
            q.state = "active"
            q.activated_at = now
            q.deactivated_at = None
            changed = True

        q.reason = reason
        q.last_flaky_at = last_flaky_at or q.last_flaky_at
        q.ticket_id = None
        return changed

    async def upsert_pending_with_ticket(
        self,
        db: AsyncSession,
        project: str,
        test_key: str,
        ticket_id: uuid.UUID,
        reason: str,
        now: datetime,
        last_flaky_at: datetime | None,
    ) -> Quarantine:
        q = await self.get(db, project, test_key)
        if q is None:
            q = Quarantine(
                project=project,
                test_key=test_key,
                state="pending",
                reason=reason,
                activated_at=None,
                last_flaky_at=last_flaky_at,
                deactivated_at=None,
                ticket_id=ticket_id,
            )
            db.add(q)
            return q

        if q.state == "active":
            return q

        if q.state == "pending" and q.ticket_id is not None:
            return q

        q.state = "pending"
        q.reason = reason
        q.ticket_id = ticket_id
        q.last_flaky_at = last_flaky_at or q.last_flaky_at
        q.deactivated_at = None
        return q

    async def deactivate(self, db: AsyncSession, project: str, test_key: str, now: datetime) -> bool:
        q = await self.get(db, project, test_key)
        if q is None or q.state != "active":
            return False
        q.state = "inactive"
        q.deactivated_at = now
        return True

    async def find_candidates_to_activate(
        self,
        db: AsyncSession,
        project: str,
        window_days: int,
        min_flaky_events: int,
        min_branches: int,
    ) -> list[tuple[str, int, int, datetime | None]]:
        window_start = datetime.now(timezone.utc) - timedelta(days=window_days)
        flaky_expr = or_(TestStat.had_failures.is_(True), TestStat.final_status == "failed")

        q = (
            select(
                TestStat.test_key.label("test_key"),
                func.count(literal(1)).filter(flaky_expr).label("flaky_count"),
                func.count(distinct(Run.branch)).filter(flaky_expr).label("flaky_branches"),
                func.max(Run.created_at).filter(flaky_expr).label("last_flaky_at"),
            )
            .select_from(Run)
            .join(TestStat, TestStat.run_id == Run.id)
            .where(
                Run.project == project,
                Run.created_at >= window_start,
                self.counted_branch_clause(),
            )
            .group_by(TestStat.test_key)
            .having(func.count(literal(1)).filter(flaky_expr) >= min_flaky_events)
            .having(func.count(distinct(Run.branch)).filter(flaky_expr) >= min_branches)
        )
        return (await db.execute(q)).all()

    async def list_active_test_keys(self, db: AsyncSession, project: str) -> list[str]:
        q = select(Quarantine.test_key).where(Quarantine.project == project, Quarantine.state == "active")
        return (await db.execute(q)).scalars().all()

    async def last_k_observe_results(
        self,
        db: AsyncSession,
        project: str,
        test_key: str,
        k: int,
    ) -> list[tuple[str, bool]]:
        q = (
            select(TestStat.final_status, TestStat.had_failures)
            .select_from(Run)
            .join(TestStat, TestStat.run_id == Run.id)
            .where(
                Run.project == project,
                Run.mode == "observe",
                Run.branch == "develop",
                TestStat.test_key == test_key,
            )
            .order_by(desc(Run.created_at))
            .limit(k)
        )
        return (await db.execute(q)).all()

    async def apply_ticket_decision(
        self,
        db: AsyncSession,
        project: str,
        ticket_id: uuid.UUID,
        target_state: str,
        now: datetime,
    ) -> int:
        values: dict = {"state": target_state}
        if target_state == "active":
            values["activated_at"] = now
            values["deactivated_at"] = None
            values["ticket_id"] = None
        else:
            values["deactivated_at"] = now
            values["ticket_id"] = None

        stmt = (
            update(Quarantine)
            .where(
                Quarantine.project == project,
                Quarantine.ticket_id == ticket_id,
                Quarantine.state == "pending",
            )
            .values(**values)
        )
        res = await db.execute(stmt)
        return res.rowcount or 0

    async def apply_new_status(self, db: AsyncSession, pk: int, new_status: Literal["active", "inactive"]) -> None:
        quarantine_model = await db.get(Quarantine, pk)

        if quarantine_model is None:
            raise HTTPException(status_code=404, detail=f"Quarantine ID {pk} not found")

        quarantine_model.state = new_status
        await db.flush()
        await db.commit()
