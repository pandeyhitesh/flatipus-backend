from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from app.shared.utils.enums import TaskAssignmentStatus


class TaskAssignmentRequest(BaseModel):
    task_id: UUID
    user_id: UUID
    scheduled_on: datetime
    status: TaskAssignmentStatus

    model_config = {
        "from_attributes": True
    }


class UpdateTaskAssignmentStatusRequest(BaseModel):
    status: TaskAssignmentStatus | None = None
    completed_on: datetime | None = None

    model_config = {
        "from_attributes": True
    }