from pydantic import BaseModel


class CityBase(BaseModel):
    name: str


class CityRead(CityBase):
    id: int

    class Config:
        from_attributes = True
