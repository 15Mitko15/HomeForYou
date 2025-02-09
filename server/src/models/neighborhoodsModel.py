"""Neighborhood model"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from server.src.database import Base


class Neighborhood(Base):
    """Neighborhood model"""

    __tablename__ = "neighborhoods"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)

    city = relationship("City", back_populates="neighborhoods")
    properties = relationship("Property", back_populates="neighborhoods")
