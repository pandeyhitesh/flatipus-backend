from pydantic import BaseModel
from uuid import UUID
from typing import Optional

from app.features.house.application.dto.house_views import (
    MemberInfo, MyHouseItem)


class HouseResponse(BaseModel):
    id: UUID
    house_name: str
    house_key: str
    address: str

    class Config:
        from_attributes = True


# class HouseDetailResponse(BaseModel):
#     id: UUID
#     house_name: str
#     house_key: str
#     address: str
#     created_by: UUID

#     class Config:
#         from_attributes = True


class MyHousesResponse(BaseModel):
    total: int
    limit: int
    offset: int
    houses: list[MyHouseItem]

class HouseMemberResponse(BaseModel):
    id: UUID
    user_id: UUID
    house_id: UUID
    name: Optional[str] = None
    email: Optional[str] = None
    joined_at: Optional[str] = None
    role: Optional[str] = None
    order: Optional[int] = None
    photo_url: Optional[str] = None
    
    class Config:
        from_attributes = True


class HouseDetailResponse(BaseModel):
    house: HouseResponse
    members: list[HouseMemberResponse]
