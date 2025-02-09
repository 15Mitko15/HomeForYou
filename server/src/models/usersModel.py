"""User model"""

from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Integer, String
from server.src.database import Base


class User(Base):
    """User model"""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    favorites = relationship("Favorite", back_populates="users")
