"""A class for hashing data"""

from passlib.context import CryptContext  # type: ignore


class Hash:
    """Hash and verify"""

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def hash(password: str) -> str:
        """Hashes a plain text password."""
        return Hash.pwd_context.hash(password)

    @staticmethod
    def verify(plain_password: str, hashed_password: str) -> bool:
        """Verifies a plain text password against the hashed password."""
        return Hash.pwd_context.verify(plain_password, hashed_password)
