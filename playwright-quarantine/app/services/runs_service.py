import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger

from app.dao.runs_dao import RunsDAO
from app.dao.test_stats_dao import TestStatsDAO
from app.db.models import Run, TestStat
from app.schemas.runs import RunIn
from app.services.quarantine_service import QuarantineService


class RunsService:
    def __init__(
        self,
        runs_dao: RunsDAO,
        test_stats_dao: TestStatsDAO,
        quarantine_service: QuarantineService,
    ):
        self.runs_dao = runs_dao
        self.test_stats_dao = test_stats_dao
        self.quarantine_service = quarantine_service

    async def ingest_run(self, db: AsyncSession, payload: RunIn) -> tuple[bool, dict, int]:
        """
        Returns (dedup, activated, deactivated)
        """
        existing = await self.runs_dao.get_run_id_by_project_pipeline(db, payload.project, payload.pipeline_id)
        logger.debug(f"existing: {existing}")
        if existing is not None:
            return True, {"mode": "auto"}, 0

        run = Run(
            id=uuid.uuid4(),
            project=payload.project,
            pipeline_id=payload.pipeline_id,
            commit_sha=payload.commit_sha,
            branch=payload.branch,
            mode=payload.mode,
            created_at=payload.created_at,
        )
        logger.info(f"Adding new run to db => project={payload.project} pipeline_id={payload.pipeline_id} branch={payload.branch}")
        await self.runs_dao.insert_run(db, run)

        rows = [
            TestStat(
                run_id=run.id,
                test_key=t.test_key,
                final_status=t.final_status,
                had_failures=t.had_failures,
                attempts=t.attempts,
                failures_count=t.failures_count,
                duration_ms=t.duration_ms,
            )
            for t in payload.tests
        ]
        logger.info(
            f"Adding test stats for run => id={run.id} pipeline_id={run.pipeline_id} branch={run.branch}")
        await self.test_stats_dao.bulk_insert(db, rows)

        # Пересчет карантина можно делать синхронно (MVP) или вынести в background job.
        activate_result = await self.quarantine_service.recompute_activate(db, project=payload.project, pipeline_id=payload.pipeline_id)
        deactivated = await self.quarantine_service.recompute_deactivate_by_observe_streak(db, project=payload.project)

        logger.info(f"run id={run.id} => dedup=False activated={activate_result} deactivated={deactivated}")
        # наружу можно вернуть activate_result["mode"], pending count и т.д.
        return False, activate_result, deactivated
