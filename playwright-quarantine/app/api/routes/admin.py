from starlette_admin import DropDown
from starlette_admin.contrib.sqla import Admin, ModelView
from starlette_admin.views import Link

from app.admin_views.quarantine_view import QuarantineView
from app.admin_views.ticket_view import TicketView
from app.core.config import settings
from app.db.models import (
    Ticket,
    Quarantine,
    TestStat,
    Run,
)
from app.db.session import make_engine

# Create admin
router = Admin(
    make_engine(settings.database_url),
    base_url="/playwright/admin",
    title="Playwright Quarantine Service",
    debug=True,
)

# Add view
router.add_view(TicketView(Ticket, icon="fa fa-list"))
router.add_view(QuarantineView(Quarantine, icon="fa fa-list"))
router.add_view(ModelView(TestStat, icon="fa fa-list"))
router.add_view(ModelView(Run, icon="fa fa-list"))
router.add_view(
    DropDown(
        "Resources",
        icon="fa fa-book",
        views=[
            Link(
                "Gitlab Repo",
                url="https://gitlab.corp.mail.ru/imqa/playwright-quarantine",
                target="_blank",
            ),
            Link(
                "Swagger",
                url="/playwright/docs",
                target="_blank",
            ),
        ],
    )
)
router.add_view(Link(label="Go Back to Home", icon="fa fa-link", url="/playwright/admin",))
