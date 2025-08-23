from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt, JWTError

from typing import Any, Dict, Optional, Union

from src.models.usersModel import User
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


# --- Dependencies ---
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    """Decodes token, validates user, and returns user object."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user_id: Union[int, str, None] = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user: Optional[User] = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user


# --- API Endpoints ---
@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Registers a new user."""
    user_service = UserService(db)
    new_user: User = user_service.register(user.username, user.email, user.password)
    return new_user


# @router.post("/login")
# def login(user: UserLogin, db: Session = Depends(get_db)) -> Dict[str, str]:
#     """Logs in a user and returns an access token."""
#     user_service = UserService(db)
#     db_user: Optional[User] = user_service.authenticate_user(user.email, user.password)
#     if not db_user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect email or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     access_token: str = create_access_token(data={"sub": str(db_user.id)})
#     return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserRead)
def me(current_user: User = Depends(get_current_user)) -> User:
    """Returns the current authenticated user's details."""
    return current_user


# from fastapi import APIRouter, Depends, HTTPException
# from fastapi_jwt_auth.auth_jwt import AuthJWT  # type: ignore
# from sqlalchemy.orm import Session
# from passlib.context import CryptContext
# from src.models.usersModel import User
# from src.schemas.userSchema import UserCreate, UserLogin, UserRead
# from src.database import get_db
# from src.services.userService import UserService

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# router = APIRouter(prefix="/auth", tags=["auth"])


# @router.post("/register", response_model=UserRead, status_code=201)
# def register(user: UserCreate, db: Session = Depends(get_db)):
#     user_service = UserService(db)
#     new_user = user_service.register(user.username, user.email, user.password)
#     return new_user


# @router.post("/login")
# def login(
#     user: UserLogin, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()
# ):
#     db_user = db.query(User).filter(User.email == user.email).first()
#     if not db_user or not pwd_context.verify(user.password, db_user.password_hash):
#         raise HTTPException(status_code=401, detail="Invalid email or password")

#     access_token = Authorize.create_access_token(subject=db_user.id)  # type: ignore
#     return {"access_token": access_token}


# @router.get("/me", response_model=UserRead)
# def me(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
#     Authorize.jwt_required()
#     user_id = Authorize.get_jwt_subject()
#     user = db.query(User).get(user_id)
#     return user
