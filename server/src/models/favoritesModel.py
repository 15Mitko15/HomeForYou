"""Favorite model"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey
from server.src.database import Base


class Favorite(Base):
    """Favorite model"""

    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    property_id = Column(Integer, ForeignKey("properties.id"), nullable=False)

    user = relationship("User", back_populates="favorites")
    property = relationship("Property", back_populates="favorites")
