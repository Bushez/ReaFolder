from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    path: Mapped[str] = mapped_column(String, unique=True)
    modified_at: Mapped[datetime] = mapped_column(DateTime)
    is_favorite: Mapped[bool] = mapped_column(Boolean, default=False)
    description: Mapped[str | None] = mapped_column(Text)

    renders: Mapped[list["RenderFile"]] = relationship(
        back_populates="project",
        cascade="all, delete-orphan"
    )

    tags: Mapped[list["Tag"]] = relationship(
        secondary="project_tags",
        back_populates="projects"
    )