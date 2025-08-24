from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.database import get_db
from src.schemas.neighborhoodSchema import NeighborhoodRead
from src.services.neighborhoodService import NeighborhoodService
from src.schemas.propertySchema import PropertyRead
from src.schemas.citySchema import CityRead

router = APIRouter(prefix="/neighborhoods", tags=["neighborhoods"])


@router.get(
    "/{id}/properties",
    response_model=List[PropertyRead],
    status_code=status.HTTP_200_OK,
)
async def get_properties_in_neighborhood(id: int, db: AsyncSession = Depends(get_db)):
    """Gets all properties located in a specific neighborhood."""
    neighborhood_service = NeighborhoodService(db)
    properties = await neighborhood_service.get_properties_by_neighborhood(id)

    if not properties:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No properties found for neighborhood '{id}' or neighborhood does not exist.",
        )
    return properties


@router.get("/{id}/city", response_model=CityRead, status_code=status.HTTP_200_OK)
async def get_city_of_neighborhood(id: int, db: AsyncSession = Depends(get_db)):
    """Gets the city that a specific neighborhood belongs to."""
    neighborhood_service = NeighborhoodService(db)
    city = await neighborhood_service.get_neighborhood_city(id)

    if not city:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not find a city for neighborhood '{id}'.",
        )
    return city


@router.get("/", response_model=list[NeighborhoodRead], status_code=status.HTTP_200_OK)
async def get_neighborhoods(db: AsyncSession = Depends(get_db)):
    """Gets all neighborhoods."""
    neighborhood_service = NeighborhoodService(db)
    db_neighborhood = await neighborhood_service.get_all_neighborhoods()

    if not db_neighborhood:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong.",
        )

    return db_neighborhood
