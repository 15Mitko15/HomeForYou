from pydantic import BaseModel


class PropertyBase(BaseModel):
    description: str
    price: int
    area: int
    neighborhood_id: int


class PropertyCreate(PropertyBase):
    user_id: int


class PropertyRead(PropertyBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
