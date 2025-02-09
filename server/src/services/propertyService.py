"""Service for handling property-related operations."""

from sqlalchemy.orm import Session
from server.src.models.favoritesModel import Favorite
from server.src.models.propertiesModel import Property
from server.src.models.usersModel import User


class PropertyService:
    """Service class for handling property-related operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_property_by_id(self, property_id: int) -> Property | None:
        """Find a property by its ID."""
        return self.db.query(Property).filter(Property.id == property_id).first()

    def get_all_properties(self) -> list[Property]:
        """Get all properties."""
        return self.db.query(Property).all()

    def get_properties_for_page(self, page: int, page_size: int) -> list[Property]:
        """Get properties for a specific page (pagination)."""
        return (
            self.db.query(Property)
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

    def get_users_that_put_property_in_favorites(self, property_id: int) -> list[User]:
        """Get all users who have added a specific property to their favorites."""
        return (
            self.db.query(User)
            .join(Favorite, Favorite.user_id == User.id)
            .filter(Favorite.property_id == property_id)
            .all()
        )

    def get_property_owner(self, property_id: int) -> User | None:
        """Get the owner of a specific property."""
        property = self.get_property_by_id(property_id)

        if not property:
            return None

        user = self.db.query(User).filter(User.id == property.user_id).first()

        return user
