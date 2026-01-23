from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from app.shared.utils.enums import TaskRepeat


class CreateTaskRequest(BaseModel):
    title: str
    description: str
    house_id: UUID
    space_id: UUID
    repeat: TaskRepeat

    model_config = {
        "from_attributes":True
    }

class UpdateTaskRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    repeat: TaskRepeat | None = None

    model_config = {
        "from_attributes": True
    }


class UpdateTaskStatusRequest(BaseModel):
    task_id: UUID
    updated_by: UUID
    is_completed: bool

    model_config = {
        "from_attributes": True
    }


class TaskByUserRequest(BaseModel):
    user_id: UUID
    house_id: UUID

    model_config = {
        "from_attributes": True
    }