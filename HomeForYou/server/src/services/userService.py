from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from src.models.usersModel import User
from src.models.propertiesModel import Property
from src.models.favoritesModel import Favorite
from src.errors import UniqueEmailError
from src.services.hashService import Hash


class UserService:
    """Service for handling user-related operations."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def register(self, username: str, email: str, password: str) -> User:
        try:
            hashed_password = Hash.hash(password)
            new_user = User(
                username=username, email=email, hashed_password=hashed_password
            )

            self.db.add(new_user)
            await self.db.commit()
            await self.db.refresh(new_user)

            return new_user

        except IntegrityError as e:
            await self.db.rollback()
            if "users_email_key" in str(e.orig):
                raise UniqueEmailError("Email already exists.") from e
            raise

    async def login(self, email: str, password: str) -> User | None:
        """Finds a user by email and checks password correctness."""
        user = await self.find_by_email(email)
        if not user or not Hash.verify(password, user.hashed_password):
            return None  # Return None on failure
        return user

    async def find_by_email(self, email: str) -> User | None:
        """Finds a user by email or returns None if not found."""
        result = await self.db.execute(select(User).filter(User.email == email))
        return result.scalars().first()

    async def find_by_id(self, user_id: int) -> User | None:
        """Finds a user by ID or returns None if not found."""
        result = await self.db.execute(select(User).filter(User.id == user_id))
        return result.scalars().first()

    async def get_favorites(self, user_id: int):
        """Returns all favorite properties for a user."""
        result = await self.db.execute(
            select(Property).join(Favorite).filter(Favorite.user_id == user_id)
        )
        return result.scalars().all()
