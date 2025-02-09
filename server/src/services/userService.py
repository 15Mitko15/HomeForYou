"""User service"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from server.src.models.usersModel import User
from server.src.models.propertiesModel import Property
from server.src.models.favoritesModel import Favorite
from server.src.errors import UniqueEmailError
from server.src.services.hashService import Hash


class UserService:
    """Service for handling user-related operations."""

    def __init__(self, db: Session):
        self.db = db

    def register(self, first_name: str, email: str, password: str) -> User:
        """Creates a new user. Raises UniqueEmailError if the email already exists."""
        try:
            hashed_password = Hash.hash(password)
            new_user = User(
                name=first_name, email=email, hashed_password=hashed_password
            )

            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)

            return new_user

        except IntegrityError as e:
            self.db.rollback()
            if "users_email_key" in str(e.orig):
                raise UniqueEmailError("Email already exists.") from e
            raise

    def login(self, email: str, password: str) -> User | None:
        """Finds a user by email and checks password correctness."""
        user = self.find_by_email(email)
        if not user or not Hash.verify(password, user.hashed_password):
            return None
        return user

    def find_by_email(self, email: str) -> User | None:
        """Finds a user by email or returns None if not found."""
        return self.db.query(User).filter(User.email == email).first()

    def find_by_id(self, user_id: int) -> User | None:
        """Finds a user by ID or returns None if not found."""
        return self.db.query(User).filter(User.id == user_id).first()

    def get_favorites(self, user_id: int):
        """Returns all favorite properties for a user."""
        return (
            self.db.query(Property)
            .join(Favorite)
            .filter(Favorite.user_id == user_id)
            .all()
        )
