"""Property model"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from src.database import Base


class Property(Base):
    """Property model"""

    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    area = Column(Integer, nullable=False)
    neighborhood_id = Column(Integer, ForeignKey("neighborhoods.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    neighborhood = relationship("Neighborhood", back_populates="properties")
    favorites = relationship("Favorite", back_populates="properties")
    owner = relationship("User", back_populates="properties")
