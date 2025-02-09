"""Service for handling neighborhood-related operations."""

from sqlalchemy.orm import Session
from server.src.models.neighborhoodsModel import Neighborhood
from server.src.models.propertiesModel import Property
from server.src.models.citiesModel import City


class NeighborhoodService:
    """Service class for handling neighborhood-related operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_neighborhood_by_name(self, name: str) -> Neighborhood | None:
        """Find a neighborhood by name."""
        return self.db.query(Neighborhood).filter(Neighborhood.name == name).first()

    def get_properties_by_neighborhood(self, neighborhood_name: str) -> list[Property]:
        """Get all properties in a specific neighborhood."""
        neighborhood = self.get_neighborhood_by_name(neighborhood_name)
        if not neighborhood:
            return []
        return self.db.query(Property).filter(Neighborhood.id == neighborhood.id).all()

    def get_neighborhood_city(self, neighborhood_name: str) -> City | None:
        """Get the city that this neighborhood is in."""
        neighborhood = self.get_neighborhood_by_name(neighborhood_name)

        if not neighborhood:
            return None
        return self.db.query(City).filter(neighborhood.city_id == City.id).first()
