from pydantic import BaseModel


class NeighborhoodBase(BaseModel):
    name: str
    city_id: int


class NeighborhoodRead(NeighborhoodBase):
    id: int

    class Config:
        from_attributes = True
