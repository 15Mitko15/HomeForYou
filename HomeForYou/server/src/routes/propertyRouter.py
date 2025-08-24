from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.propertySchema import PropertyCreate, PropertyRead
from src.database import get_db
from src.services.propertyService import PropertyService


# --- Configuration ---
router = APIRouter(prefix="/property", tags=["property"])


# --- API Endpoints ---
@router.post("/add", response_model=PropertyRead, status_code=status.HTTP_201_CREATED)
async def add_property(property: PropertyCreate, db: AsyncSession = Depends(get_db)):
    property_service = PropertyService(db)
    return await property_service.add_new_property(property)


@router.get("/", response_model=list[PropertyRead], status_code=status.HTTP_200_OK)
async def get_properties(db: AsyncSession = Depends(get_db)):
    """Gets all properties."""
    property_service = PropertyService(db)
    db_property = await property_service.get_all_properties()

    if not db_property:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Something went wrong.",
        )

    return db_property


@router.get(
    "/{property_id}", response_model=PropertyRead, status_code=status.HTTP_200_OK
)
async def get_property_by_id(
    property_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Gets a specific property by its unique ID."""
    property_service = PropertyService(db)
    db_property = await property_service.get_property_by_id(property_id)

    if not db_property:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Property with id {property_id} not found",
        )

    return db_property
