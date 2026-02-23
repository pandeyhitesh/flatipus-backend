from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class UserResponse(BaseModel):
    id: str
    email: str
    name: str
    google_id: str
    created_at: datetime

    class Config:
        from_attributes = True


class AuthUserResponse(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    access_token: str
    token_type: str
    user: AuthUserResponse

    class Config:
        from_attributes = True