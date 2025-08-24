"""Service for handling property-related operations."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.favoritesModel import Favorite
from src.models.propertiesModel import Property
from src.models.usersModel import User
from typing import List, Optional

from src.schemas.propertySchema import PropertyCreate


class PropertyService:
    """Service class for handling property-related operations."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_property_by_id(self, property_id: int) -> Optional[Property]:
        """Find a property by its ID."""
        result = await self.db.execute(
            select(Property).filter(Property.id == property_id)
        )

        return result.scalars().first()

    async def get_all_properties(self) -> List[Property]:
        """Get all properties."""
        result = await self.db.execute(select(Property))
        return list(result.scalars().all())

    async def get_properties_for_page(
        self, page: int, page_size: int
    ) -> List[Property]:
        """Get properties for a specific page (pagination)."""
        result = await self.db.execute(
            select(Property).offset((page - 1) * page_size).limit(page_size)
        )
        return list(result.scalars().all())

    async def get_users_that_put_property_in_favorites(
        self, property_id: int
    ) -> List[User]:
        """Get all users who have added a specific property to their favorites."""
        result = await self.db.execute(
            select(User)
            .join(Favorite, Favorite.user_id == User.id)
            .filter(Favorite.property_id == property_id)
        )
        return list(result.scalars().all())

    async def get_property_owner(self, property_id: int) -> Optional[User]:
        """Get the owner of a specific property."""
        prop = await self.get_property_by_id(property_id)

        if not prop:
            return None

        result = await self.db.execute(select(User).filter(User.id == prop.user_id))
        return result.scalars().first()

    async def add_new_property(
        self,
        property_data: PropertyCreate,
    ) -> Property:
        """Add a new property to the database."""
        new_property = Property(
            **property_data.model_dump(),
        )
        self.db.add(new_property)
        await self.db.commit()
        await self.db.refresh(new_property)

        return new_property
