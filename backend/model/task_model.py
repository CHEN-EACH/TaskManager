from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from database.database import Base

class Task(Base):
    
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status: Mapped[str] = mapped_column(String(50),nullable=False)
    title: Mapped[str] = mapped_column(String(100),nullable=False)
    content: Mapped[str | None] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    updated_at: Mapped[datetime] = mapped_column(nullable=False)
    priority: Mapped[int] = mapped_column(nullable=False)
    
    user : Mapped["User"] = relationship("User",back_populates="tasks")
    