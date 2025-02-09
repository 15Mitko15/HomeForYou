"""User model"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from server.src.database import Base


class User(Base):
    """User model"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)

    favorites = relationship(
        "Favorite", back_populates="user", cascade="all, delete-orphan"
    )
