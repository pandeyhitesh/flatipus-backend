from pydantic import BaseModel
from uuid import UUID

class CreateUserRequest(BaseModel):
    email: str
    name: str
    google_id: str
    phone_number: str | None = None
    photo_url: str | None = None

class GoogleMobileLoginRequest(BaseModel):
    id_token: str
