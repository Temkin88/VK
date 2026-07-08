from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import TestStat


class TestStatsDAO:
    async def bulk_insert(self, db: AsyncSession, rows: list[TestStat]) -> None:
        # Для MVP можно просто add_all; при больших объемах можно перейти на bulk insert.
        db.add_all(rows)
