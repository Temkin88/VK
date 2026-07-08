"""add pending quarantine state

Revision ID: e7ca87370f8a
Revises: 2d608ff8ebe0
Create Date: 2026-03-13 21:21:47.722514

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'e7ca87370f8a'
down_revision: Union[str, Sequence[str], None] = '2d608ff8ebe0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # имя constraint должно совпадать с тем, что в модели: quarantine_state_check
    op.drop_constraint("quarantine_state_check", "quarantine", type_="check")
    op.create_check_constraint(
        "quarantine_state_check",
        "quarantine",
        "state in ('active','inactive','pending')",
    )


def downgrade() -> None:
    op.drop_constraint("quarantine_state_check", "quarantine", type_="check")
    op.create_check_constraint(
        "quarantine_state_check",
        "quarantine",
        "state in ('active','inactive')",
    )