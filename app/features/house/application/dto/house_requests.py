from pydantic import BaseModel
from typing import Optional
from app.shared.utils.enums import UserRole


class CreateHouseRequest(BaseModel):
    house_name: str
    address: str


class UpdateHouseRequest(BaseModel):
    house_name: Optional[str] = None
    address: Optional[str] = None

    model_config = {
        "from_attributes": True
    }


class JoinHouseRequest(BaseModel):
    house_key: str


class UpdateMemberRoleRequest(BaseModel):
    new_role: UserRole

    model_config = {
        "from_attributes": True
    }
