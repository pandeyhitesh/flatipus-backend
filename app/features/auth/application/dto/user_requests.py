from pydantic import BaseModel
from uuid import UUID

class CreateUser(BaseModel):
    email: str
    name: str
    google_id: UUID

class GoogleMobileLoginRequest(BaseModel):
    id_token: str
