"""Service for handling city-related operations."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.neighborhoodsModel import Neighborhood
from src.models.propertiesModel import Property
from src.models.citiesModel import City
from typing import List, Optional


class CityService:
    """Service class for handling city-related operations."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_city_by_name(self, name: str) -> Optional[City]:
        """Find a city by name."""
        result = await self.db.execute(select(City).filter(City.name == name))
        return result.scalars().first()

    async def get_properties_by_city(self, city_name: str) -> List[Property]:
        """Get all properties in a specific city."""
        city = await self.get_city_by_name(city_name)
        if not city:
            return []
        result = await self.db.execute(
            select(Property).join(Neighborhood).filter(Neighborhood.city_id == city.id)
        )
        return list(result.scalars().all())

    async def get_neighborhoods_by_city(self, city_name: str) -> List[Neighborhood]:
        """Get all neighborhoods in a specific city."""
        city = await self.get_city_by_name(city_name)
        if not city:
            return []
        result = await self.db.execute(
            select(Neighborhood).filter(Neighborhood.city_id == city.id)
        )
        return list(result.scalars().all())

    async def get_all_cities(self) -> List[City]:
        """Get all cities."""
        result = await self.db.execute(select(City))
        return list(result.scalars().all())
