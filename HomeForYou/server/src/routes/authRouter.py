from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any

from src.schemas.userSchema import UserCreate, UserLogin, UserRead
from src.database import get_db
from src.services.userService import UserService
from src.config import JWT_SECRET


# --- Configuration ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# --- JWT Service Functions ---
def create_access_token(data: dict[str, Any]) -> str:
    """Creates a JWT access token."""
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm="HS256")
    return encoded_jwt


# --- API Endpoints ---
@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)
    return await user_service.register(user.username, user.email, user.password)


@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)) -> JSONResponse:
    """Logs in a user and returns an access token."""
    user_service = UserService(db)

    db_user = await user_service.login(user.email, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
        )

    access_token: str = create_access_token(data={"sub": str(db_user.id)})

    response = JSONResponse(content={"message": "Login successful"})

    response.headers["Authorization"] = f"Bearer {access_token}"

    return response
