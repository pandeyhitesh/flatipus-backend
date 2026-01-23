from pydantic import BaseModel, field_validator
from typing import Optional
from uuid import UUID
import json

from app.features.space.domain.entities.space import Space

class GetChoresResponse(BaseModel):
    id: UUID
    space_id: UUID
    title: str
    items: list[str]

    model_config = {
        "from_attributes": True
    }

class GetSpaceResponse(BaseModel):
    id: UUID
    house_id: UUID
    name: str
    chores: Optional[list[GetChoresResponse]] = None

    model_config = {
        "from_attributes": True
    }
    
    @field_validator('chores', mode='before')
    @classmethod
    def parse_chores(cls, v):
        if isinstance(v, str):
            try:
                chores_data = json.loads(v)
                if isinstance(chores_data, list):
                    return chores_data
                else:
                    return [chores_data]
            except (json.JSONDecodeError, TypeError):
                return None
        return v
