from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

class User(Base):
    
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    account: Mapped[str] = mapped_column(String(15),nullable=False,unique=True)
    password_hash: Mapped[str] = mapped_column(String(100),nullable=False)
    nickname: Mapped[str | None] = mapped_column(String(100))