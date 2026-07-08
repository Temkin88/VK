import uuid
from datetime import datetime

from sqlalchemy import (
    BigInteger,
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Run(Base):
    __tablename__ = "runs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    project: Mapped[str] = mapped_column(Text, nullable=False)
    pipeline_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    commit_sha: Mapped[str] = mapped_column(Text, nullable=False)
    branch: Mapped[str] = mapped_column(Text, nullable=False)
    mode: Mapped[str] = mapped_column(Text, nullable=False)  # gated|observe
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    tests: Mapped[list["TestStat"]] = relationship(back_populates="run", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint("mode in ('gated','observe')", name="runs_mode_check"),
        UniqueConstraint("project", "pipeline_id", name="runs_project_pipeline_uniq"),
        Index("runs_project_branch_created_idx", "project", "branch", "created_at"),
    )


class TestStat(Base):
    __tablename__ = "test_stats"

    run_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("runs.id", ondelete="CASCADE"),
        primary_key=True,
    )
    test_key: Mapped[str] = mapped_column(Text, primary_key=True)

    final_status: Mapped[str] = mapped_column(Text, nullable=False)  # passed|failed|skipped
    had_failures: Mapped[bool] = mapped_column(Boolean, nullable=False)
    attempts: Mapped[int] = mapped_column(Integer, nullable=False)
    failures_count: Mapped[int] = mapped_column(Integer, nullable=False)
    duration_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)

    run: Mapped["Run"] = relationship(back_populates="tests")

    __table_args__ = (
        CheckConstraint("final_status in ('passed','failed','skipped')", name="test_stats_final_status_check"),
        Index("test_stats_test_key_idx", "test_key"),
    )


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project: Mapped[str] = mapped_column(Text, nullable=False)
    state: Mapped[str] = mapped_column(Text, nullable=False)  # pending|resolved
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    resolved_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    quarantines: Mapped[list["Quarantine"]] = relationship(back_populates="ticket")

    __table_args__ = (
        CheckConstraint("state in ('pending','resolved')", name="tickets_state_check"),
        Index("tickets_project_state_idx", "project", "state"),
    )


class Quarantine(Base):
    __tablename__ = "quarantine"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    project: Mapped[str] = mapped_column(Text, nullable=False)
    test_key: Mapped[str] = mapped_column(Text, nullable=False)

    state: Mapped[str] = mapped_column(Text, nullable=False)  # active|inactive|pending
    reason: Mapped[str] = mapped_column(Text, nullable=False)

    activated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    last_flaky_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    deactivated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    ticket_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tickets.id", ondelete="SET NULL"),
        nullable=True,
    )
    ticket: Mapped["Ticket | None"] = relationship(back_populates="quarantines")

    __table_args__ = (
        UniqueConstraint("project", "test_key", name="quarantine_project_test_key_uniq"),
        CheckConstraint("state in ('active','inactive','pending')", name="quarantine_state_check"),
        Index("quarantine_project_state_idx", "project", "state"),
        Index("quarantine_ticket_idx", "ticket_id"),
        Index("quarantine_project_ticket_idx", "project", "ticket_id"),
    )
