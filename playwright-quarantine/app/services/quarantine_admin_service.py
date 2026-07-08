from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.quarantine_dao import QuarantineDAO

class QuarantineAdminService:
    def __init__(self, quarantine_dao: QuarantineDAO):
        self.quarantine_dao = quarantine_dao

    async def list_pending(self, db: AsyncSession, project: str):
        return await self.quarantine_dao.list_by_state(db, project, "pending")

    async def approve(self, db: AsyncSession, project: str, test_keys: list[str]) -> tuple[int, int, int]:
        now = datetime.now(timezone.utc)
        updated = skipped = not_found = 0

        for key in test_keys:
            res = await self.quarantine_dao.approve_pending(db, project, key, now)
            if res == "updated":
                updated += 1
            elif res == "skipped":
                skipped += 1
            else:
                not_found += 1

        return updated, skipped, not_found

    async def reject_to_inactive(self, db: AsyncSession, project: str, test_keys: list[str]) -> tuple[int, int, int]:
        now = datetime.now(timezone.utc)
        updated = skipped = not_found = 0

        for key in test_keys:
            res = await self.quarantine_dao.reject_pending_to_inactive(db, project, key, now)
            if res == "updated":
                updated += 1
            elif res == "skipped":
                skipped += 1
            else:
                not_found += 1

        return updated, skipped, not_found

    async def reject_delete(self, db: AsyncSession, project: str, test_keys: list[str]) -> tuple[int, int, int]:
        updated = skipped = not_found = 0

        for key in test_keys:
            res = await self.quarantine_dao.delete_pending(db, project, key)
            if res == "updated":
                updated += 1
            elif res == "skipped":
                skipped += 1
            else:
                not_found += 1

        return updated, skipped, not_found
