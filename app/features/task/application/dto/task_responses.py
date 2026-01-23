from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from app.features.task.application.dto.task_assignment_responses import (
    TaskAssignmentResponse)



class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str
    house_id: UUID
    space_id: UUID
    created_by: UUID
    repeat: str
    created_at: datetime
    updated_by: datetime | None
    is_completed: bool

    class Config:
        from_attributes = True


class TaskDetailResponse(BaseModel):
    task: TaskResponse
    assignments: list[TaskAssignmentResponse]

    class Config:
        from_attributes = True


class UserTaskResponse(BaseModel):
    task_id: UUID
    title: str
    description: str
    house_id: UUID
    space_id: UUID
    space_name: str
    is_completed: bool
    assignment_status: str | None
    scheduled_on: datetime | None

    class Config:
        from_attributes = True 


