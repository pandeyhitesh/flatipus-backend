# from pydantic import BaseModel
# from uuid import UUID
# from datetime import datetime
# from app.shared.utils.enums import UserRole
# from typing import Optional

# class CreateHouseRequest(BaseModel):
#     house_name: str
#     address: str

# class UpdateHouseRequest(BaseModel):
#     house_name: Optional[str] = None
#     address: Optional[str] = None

#     model_config = {
#         "from_attributes": True
#     }
    
# class HouseResponse(BaseModel):
#     id: UUID
#     house_name: str
#     house_key: str
#     address: str

#     class Config:
#         from_attributes = True

# class JoinHouseRequest(BaseModel):
#     house_key: str

# class MemberInfo(BaseModel):
#     id: str
#     name: str
#     email: str
#     role: str

#     class Config:
#         from_attributes = True

# class HouseDetailResponse(BaseModel):
#     id: UUID
#     house_name: str
#     house_key: str
#     address: str
#     created_by: UUID

#     class Config:
#         from_attributes = True

# class GetHouseResponse(BaseModel):
#     house: HouseDetailResponse
#     members: list[MemberInfo]

# class MyHouseItem(BaseModel):
#     id: UUID
#     house_name: str
#     house_key: str
#     address: str
#     joined_at: datetime
#     member_count: int
#     role: str

#     class Config:
#         from_attributes = True # pydantic v2 replacement for orm_mode

# class MyHousesResponse(BaseModel):
#     total: int
#     limit: int
#     offset: int
#     houses: list[MyHouseItem]

# class UpdateMemberRoleRequest(BaseModel):
#     new_role: UserRole

#     model_config = {
#         "from_attributes": True
#     }