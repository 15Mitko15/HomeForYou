"""City model"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from server.src.database import Base


class City(Base):
    """City model"""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

    neighborhoods = relationship("Neighborhood", back_populates="city")
