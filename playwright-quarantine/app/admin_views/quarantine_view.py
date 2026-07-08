import logging
from typing import Literal, Any

from starlette.requests import Request
from starlette_admin.contrib.sqla import ModelView
from starlette_admin import RowActionsDisplayType, action, row_action

from app.api.deps import SessionLocal
from app.dao.quarantine_dao import QuarantineDAO
from app.dao.tickets_dao import TicketsDAO
from app.services.quarantine_service import QuarantineService


logger = logging.getLogger(__name__)


class QuarantineView(ModelView):
    row_actions_display_type = RowActionsDisplayType.ICON_LIST
    responsive_table = True

    actions = ["delete", "set_inactive_bulk", "set_active_bulk"]

    quarantine_svc = QuarantineService(
        quarantine_dao=QuarantineDAO(),
        tickets_dao=TicketsDAO(),
    )

    async def apply_new_status_to_record(self, pk: int, new_status: Literal["active", "inactive"]) -> None:
        async with SessionLocal() as session:
            logger.info(f"Setting quarantine record {pk} to {new_status}")
            await self.quarantine_svc.apply_new_status(session, pk, new_status)

    @row_action(
        name="set_active",
        text="Set active",
        confirmation="Are you sure you want to set quarantine record active?",
    )
    async def set_active(self, request: Request, pk: Any):
        await self.apply_new_status_to_record(pk=pk, new_status="active")

    @row_action(
        name="set_inactive",
        text="Set inactive",
        confirmation="Are you sure you want to set quarantine record inactive?",
    )
    async def set_inactive(self, request: Request, pk: Any):
        await self.apply_new_status_to_record(pk=pk, new_status="inactive")

    @action(
        name="set_inactive_bulk",
        text="Set inactive bulk",
        confirmation="Are you sure you want to set this quarantine records inactive?",
    )
    async def set_inactive_bulk(self, request: Request, pks: list[Any]):
        for pk in pks:
            await self.apply_new_status_to_record(pk=pk, new_status="inactive")

    @action(
        name="set_active_bulk",
        text="Set active bulk",
        confirmation="Are you sure you want to set this quarantine records active?",
    )
    async def set_active_bulk(self, request: Request, pks: list[Any]):
        for pk in pks:
            await self.apply_new_status_to_record(pk=pk, new_status="active")
