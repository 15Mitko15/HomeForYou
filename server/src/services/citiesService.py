"""Service for handling city-related operations."""

from sqlalchemy.orm import Session
from server.src.models.neighborhoodsModel import Neighborhood
from server.src.models.propertiesModel import Property
from server.src.models.citiesModel import City


class CityService:
    """Service class for handling city-related operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_city_by_name(self, name: str) -> City | None:
        """Find a city by name."""
        return self.db.query(City).filter(City.name == name).first()

    def get_properties_by_city(self, city_name: str) -> list[Property]:
        """Get all properties in a specific city."""
        city = self.get_city_by_name(city_name)
        if not city:
            return []
        return (
            self.db.query(Property)
            .join(Neighborhood)
            .filter(Neighborhood.city_id == city.id)
            .all()
        )

    def get_neighborhoods_by_city(self, city_name: str) -> list[Neighborhood]:
        """Get all neighborhoods in a specific city."""
        city = self.get_city_by_name(city_name)
        if not city:
            return []
        return self.db.query(Neighborhood).filter(Neighborhood.city_id == city.id).all()

    def get_all_cities(self) -> list[City]:
        """Get all cities."""
        return self.db.query(City).all()
