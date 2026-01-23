from uuid import UUID
from datetime import datetime

from app.shared.utils.enums import TaskAssignmentStatus, TaskRepeat


class Task:
    def __init__(
        self,
        id: UUID,
        title: str,
        description: str,
        house_id: UUID,
        space_id: UUID,
        created_by: UUID,
        created_at: datetime,
        repeat: TaskRepeat,
        is_completed: bool,
        
    ):
        self.id = id
        self.title = title
        self.description = description
        self.house_id = house_id
        self.space_id = space_id
        self.created_by = created_by
        self.created_at = created_at
        self.repeat = repeat
        self.is_completed = is_completed
        