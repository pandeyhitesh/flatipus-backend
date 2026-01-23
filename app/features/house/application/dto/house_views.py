from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class MemberInfo(BaseModel):
    id: str
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True


class MyHouseItem(BaseModel):
    id: UUID
    house_name: str
    house_key: str
    address: str
    joined_at: datetime
    member_count: int
    role: str

    class Config:
        from_attributes = True  # pydantic v2 replacement for orm_mode
