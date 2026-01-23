from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class ChoresRequest(BaseModel):
    title: str
    items: list[str]


class CreateSpaceRequest(BaseModel):
    space_name: str
    house_id: UUID
    chores: Optional[list[ChoresRequest]] = None

    model_config = {
        "from_attributes": True,
        "populate_by_name": True
    }


class DeleteSpaceRequest(BaseModel):
    space_id: str

    model_config = {
        "from_attributes": True
    }
