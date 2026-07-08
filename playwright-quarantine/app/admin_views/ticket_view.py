from typing import Any, Literal

from starlette.requests import Request
from starlette_admin import RowActionsDisplayType, action, row_action
from starlette_admin.contrib.sqla import ModelView

from app.api.deps import SessionLocal
from app.dao.quarantine_dao import QuarantineDAO
from app.dao.tickets_dao import TicketsDAO
from app.services.tickets_service import TicketsService


class TicketView(ModelView):
    row_actions_display_type = RowActionsDisplayType.ICON_LIST

    page_size = 50
    page_size_options = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

    responsive_table = True

    actions = ["delete", "approve_tickets", "reject_tickets"]

    ticket_svc = TicketsService(
        tickets_dao=TicketsDAO(),
        quarantine_dao=QuarantineDAO(),
    )

    async def manual_apply(self, request: Request, pk: Any, decision: Literal["active", "inactive"]) -> str:
        async with SessionLocal() as session:
            try:
                await self.ticket_svc.resolve_from_admin(
                    db=session,
                    ticket_id=pk,
                    decision=decision,
                )
                await session.commit()
                return f"{'Approved' if decision == 'active' else 'Rejected'} \"{pk}\" ticket"
            except Exception as e:
                await session.rollback()
                return f"Something went wrong: {e}"

    @row_action(
        name="approve_ticket",
        text="Approve",
        confirmation="Are you sure you want to approve ticket?",
    )
    async def manual_approve_ticket(self, request: Request, pk: Any):
        return await self.manual_apply(
            request=request,
            pk=pk,
            decision="active"
        )

    @row_action(
        name="reject_ticket",
        text="Reject",
        confirmation="Are you sure you want to reject ticket?",
    )
    async def manual_reject_ticket(self, request: Request, pk: Any):
        return await self.manual_apply(
            request=request,
            pk=pk,
            decision="inactive"
        )

    async def manual_bulk_apply(self, request: Request, pks: list[Any], decision: Literal["active", "inactive"]) -> str:
        success_list: list[Any] = []
        error_list: list[dict[Any, Exception]] = []

        async with SessionLocal() as session:
            for pk in pks:
                try:
                    await self.ticket_svc.resolve_from_admin(
                        db=session,
                        ticket_id=pk,
                        decision=decision,
                    )
                    success_list.append(pk)
                    await session.commit()
                except Exception as e:
                    await session.rollback()
                    error_list.append({str(pk): e})

            if len(error_list) == 0:
                return f"{'Approved' if decision == 'active' else 'Rejected'} {len(pks)} tickets"
            else:
                result_text = (f"Success: {len(success_list)} tickets\n"
                               f"Errors: \n") + "\n".join(
                    [f"{key}: {value}" for item in error_list for key, value in item.items()])

                return result_text

    @action(
        name="approve_tickets",
        text="Manually approve mass quarantine tickets",
        confirmation="Are you sure you want to approve mass quarantine ticket?",
    )
    async def manual_quarantine(self, request: Request, pks: list[Any]):
        return await self.manual_bulk_apply(request=request, pks=pks, decision="active")

    @action(
        name="reject_tickets",
        text="Manually reject mass quarantine tickets",
        confirmation="Are you sure you want to reject mass quarantine ticket?",
    )
    async def manual_unquarantine(self, request: Request, pks: list[Any]):
        return await self.manual_bulk_apply(request=request, pks=pks, decision="inactive")
