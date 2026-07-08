import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Run


class RunsDAO:
    async def get_run_id_by_project_pipeline(self, db: AsyncSession, project: str, pipeline_id: int) -> uuid.UUID | None:
        q = select(Run.id).where(Run.project == project, Run.pipeline_id == pipeline_id)
        return (await db.execute(q)).scalar_one_or_none()

    async def insert_run(self, db: AsyncSession, run: Run) -> None:
        db.add(run)
