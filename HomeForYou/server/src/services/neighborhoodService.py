"""Service for handling neighborhood-related operations."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.neighborhoodsModel import Neighborhood
from src.models.propertiesModel import Property
from src.models.citiesModel import City
from typing import List, Optional


class NeighborhoodService:
    """Service class for handling neighborhood-related operations."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_neighborhood_by_id(self, id: int) -> Optional[Neighborhood]:
        """Find a neighborhood by id."""
        result = await self.db.execute(
            select(Neighborhood).filter(Neighborhood.id == id)
        )
        return result.scalars().first()

    async def get_all_neighborhoods(self) -> Optional[List[Neighborhood]]:
        """Find all neighborhoods."""

        result = await self.db.execute(select(Neighborhood))
        return list(result.scalars().all())

    async def get_properties_by_neighborhood(
        self, neighborhood_id: int
    ) -> List[Property]:
        """Get all properties in a specific neighborhood."""
        neighborhood = await self.get_neighborhood_by_id(neighborhood_id)
        if not neighborhood:
            return []
        result = await self.db.execute(
            select(Property).filter(Property.neighborhood_id == neighborhood.id)
        )
        return list(result.scalars().all())

    async def get_neighborhood_city(self, neighborhood_id: int) -> Optional[City]:
        """Get the city that this neighborhood is in."""
        neighborhood = await self.get_neighborhood_by_id(neighborhood_id)

        if not neighborhood:
            return None
        result = await self.db.execute(
            select(City).filter(City.id == neighborhood.city_id)
        )
        return result.scalars().first()
