from typing import List

from models.feedback import Feedback
from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Section(Base):
    __tablename__ = "section"
    __table_args__ = (
        UniqueConstraint("report_id", "number", name="section_report_id_number_key"),
    )

    id: Mapped[int] = mapped_column(index=True, primary_key=True, autoincrement="auto")
    report_id: Mapped[int] = Column(Integer, ForeignKey("report.id"))
    number: Mapped[int]= mapped_column(nullable=True)
    decision: Mapped[str] = mapped_column(nullable=True)
    title: Mapped[str] = mapped_column(nullable= True)
    feedback: Mapped[List["Feedback"]] = relationship()