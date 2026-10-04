from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)

    projects: Mapped[list["Project"]] = relationship(
        secondary="project_tags",
        back_populates="tags"
    )

    renders: Mapped[list["RenderFile"]] = relationship(
        secondary="render_tags",
        back_populates="tags"
    )