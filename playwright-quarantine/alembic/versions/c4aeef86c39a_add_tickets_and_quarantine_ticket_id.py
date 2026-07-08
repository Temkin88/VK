from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "c4aeef86c39a"
down_revision = "e7ca87370f8a"
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        "tickets",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("project", sa.Text(), nullable=False),
        sa.Column("state", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("resolved_at", sa.DateTime(timezone=True), nullable=True),
        sa.CheckConstraint("state in ('pending','resolved')", name="tickets_state_check"),
    )
    op.create_index("tickets_project_state_idx", "tickets", ["project", "state"])

    op.add_column("quarantine", sa.Column("ticket_id", postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(
        "quarantine_ticket_fk",
        "quarantine",
        "tickets",
        ["ticket_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_index("quarantine_ticket_idx", "quarantine", ["ticket_id"])
    op.create_index("quarantine_project_ticket_idx", "quarantine", ["project", "ticket_id"])

def downgrade() -> None:
    op.drop_index("quarantine_project_ticket_idx", table_name="quarantine")
    op.drop_index("quarantine_ticket_idx", table_name="quarantine")
    op.drop_constraint("quarantine_ticket_fk", "quarantine", type_="foreignkey")
    op.drop_column("quarantine", "ticket_id")

    op.drop_index("tickets_project_state_idx", table_name="tickets")
    op.drop_table("tickets")
