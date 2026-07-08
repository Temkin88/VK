"""quarantine: add id pk for admin compatibility

Revision ID: fa3c4a047b32
Revises: c4aeef86c39a
Create Date: 2026-03-14 10:44:18.364399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'fa3c4a047b32'
down_revision: Union[str, Sequence[str], None] = 'c4aeef86c39a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1) pgcrypto для gen_random_uuid()
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")

    # 2) Добавляем колонку id (пока nullable)
    op.add_column("quarantine", sa.Column("id", postgresql.UUID(as_uuid=True), nullable=True))

    # 3) Заполняем существующие строки UUID'ами
    op.execute("UPDATE quarantine SET id = gen_random_uuid() WHERE id IS NULL")

    # 4) Делаем NOT NULL
    op.alter_column("quarantine", "id", nullable=False)

    # 5) Убираем старый PK (project, test_key)
    op.drop_constraint("quarantine_pkey", "quarantine", type_="primary")

    # 6) Создаем новый PK на id
    op.create_primary_key("quarantine_pkey", "quarantine", ["id"])

    # 7) Добавляем уникальность на (project, test_key)
    op.create_unique_constraint(
        "quarantine_project_test_key_uniq",
        "quarantine",
        ["project", "test_key"],
    )

    # 8) Индекс на (project, test_key) обычно уже не нужен, но UNIQUE создаст индекс сам.
    # Если у вас были явные индексы на (project, test_key) — проверьте, не дублируются ли.


def downgrade() -> None:
    # Откат: возвращаем составной PK
    op.drop_constraint("quarantine_project_test_key_uniq", "quarantine", type_="unique")

    op.drop_constraint("quarantine_pkey", "quarantine", type_="primary")
    op.create_primary_key("quarantine_pkey", "quarantine", ["project", "test_key"])

    op.drop_column("quarantine", "id")

    # extension pgcrypto обычно не удаляют в downgrade
