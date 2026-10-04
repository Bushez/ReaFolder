from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class RenderFile(Base):
    __tablename__ = "renders"

    id: Mapped[int] = mapped_column(primary_key=True)

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE")
    )

    path: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String(100))
    modified_at: Mapped[datetime] = mapped_column(DateTime)
    description: Mapped[str | None] = mapped_column(Text)

    project: Mapped["Project"] = relationship(
        back_populates="renders"
    )

    tags: Mapped[list["Tag"]] = relationship(
        secondary="render_tags",
        back_populates="renders"
    )