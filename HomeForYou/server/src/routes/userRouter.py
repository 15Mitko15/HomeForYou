from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.database import get_db
from src.services.userService import UserService
from src.schemas.userSchema import UserRead
from src.schemas.propertySchema import PropertyRead

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    """Gets a specific user by their ID."""
    user_service = UserService(db)
    user = await user_service.find_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )
    return user


@router.get(
    "/{user_id}/favorites",
    response_model=List[PropertyRead],
    status_code=status.HTTP_200_OK,
)
async def get_user_favorites(user_id: int, db: AsyncSession = Depends(get_db)):
    """Gets all favorite properties for a specific user."""
    user_service = UserService(db)
    user = await user_service.find_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    favorites = await user_service.get_favorites(user_id)
    return favorites
