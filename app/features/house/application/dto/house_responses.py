from pydantic import BaseModel
from uuid import UUID
from app.features.house.application.dto.house_views import (
    MemberInfo, MyHouseItem)


class HouseResponse(BaseModel):
    id: UUID
    house_name: str
    house_key: str
    address: str

    class Config:
        from_attributes = True


class HouseDetailResponse(BaseModel):
    id: UUID
    house_name: str
    house_key: str
    address: str
    created_by: UUID

    class Config:
        from_attributes = True


class GetHouseResponse(BaseModel):
    house: HouseDetailResponse
    members: list[MemberInfo]


class MyHousesResponse(BaseModel):
    total: int
    limit: int
    offset: int
    houses: list[MyHouseItem]
