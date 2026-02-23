from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class TaskAssignmentResponse(BaseModel):
    id: UUID
    task_id: UUID
    user_id: UUID
    scheduled_on: datetime
    status: str
    updated_on: datetime | None
    is_completed: bool

    class Config:
        from_attributes = True