from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.database import get_db
from src.services.citiesService import CityService
from src.schemas.citySchema import CityRead
from src.schemas.propertySchema import PropertyRead
from src.schemas.neighborhoodSchema import (
    NeighborhoodRead,
)

router = APIRouter(prefix="/cities", tags=["cities"])


@router.get("/", response_model=List[CityRead], status_code=status.HTTP_200_OK)
async def get_all_cities(db: AsyncSession = Depends(get_db)):
    """Gets a list of all cities."""
    city_service = CityService(db)
    return await city_service.get_all_cities()


@router.get(
    "/{city_name}/properties",
    response_model=List[PropertyRead],
    status_code=status.HTTP_200_OK,
)
async def get_properties_in_city(city_name: str, db: AsyncSession = Depends(get_db)):
    """Gets all properties located in a specific city."""
    city_service = CityService(db)
    properties = await city_service.get_properties_by_city(city_name)

    if not properties:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No properties found for city '{city_name}' or city does not exist.",
        )
    return properties


@router.get(
    "/{city_name}/neighborhoods",
    response_model=List[NeighborhoodRead],
    status_code=status.HTTP_200_OK,
)
async def get_neighborhoods_in_city(city_name: str, db: AsyncSession = Depends(get_db)):
    """Gets all neighborhoods within a specific city."""
    city_service = CityService(db)
    neighborhoods = await city_service.get_neighborhoods_by_city(city_name)

    if not neighborhoods:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No neighborhoods found for city '{city_name}' or city does not exist.",
        )
    return neighborhoods
