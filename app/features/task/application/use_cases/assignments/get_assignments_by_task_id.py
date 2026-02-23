from uuid import UUID
from typing import Optional, List
from app.features.task.application.ports.task_assignment_repositories import (
    ITaskAssignmentRepository
)
from app.features.task.application.dto.task_assignment_responses import (
    TaskAssignmentResponse
)


class GetAssignmentsByTaskIdUseCase:
    def __init__(
            self,
            assignment_repo: ITaskAssignmentRepository
        ):
        self.assignment_repo = assignment_repo

    def execute(
            self, 
            task_id: UUID,
            current_user_id: UUID
    ) -> Optional[List[TaskAssignmentResponse]]:
        return self.assignment_repo.get_assignments_by_task_id(
            task_id=task_id)