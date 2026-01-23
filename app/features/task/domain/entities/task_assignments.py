from uuid import UUID
from datetime import datetime


from app.shared.utils.enums import TaskAssignmentStatus


class TaskAssignments:
    def __init__(
        self,
        id: UUID,
        task_id: UUID,
        user_id: UUID,
        scheduled_on: datetime,
        completed_on: datetime | None,
        status: TaskAssignmentStatus,
        is_completed: bool,
    ):
        self.id = id
        self.task_id = task_id
        self.user_id = user_id
        self.scheduled_on = scheduled_on
        self.completed_on = completed_on
        self.status = status
        self.is_completed = is_completed