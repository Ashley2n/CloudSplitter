from datetime import UTC, datetime
import uuid
from sqlalchemy import UUID, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.core.database import Base


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))

    participants: Mapped[list["Participant"]] = relationship(
        back_populates="group"
    )

    def __repr__(self):
        return (
        f"Group(id={self.id}, "
        f"name='{self.name}', "
        f"created_at={self.created_at})"
    )
        


class Participant(Base):
    __tablename__ = "participants"

    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey('groups.id'))
    name:Mapped[str] = mapped_column(String(30), unique=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(UTC))

    group: Mapped['Group'] = relationship(back_populates='participants')

    def __repr__(self):
        return (
        f"Participant(id={self.id}, "
        f"group_id={self.group_id},"
        f"name='{self.name}', "
        f"created_at={self.created_at})"
    )