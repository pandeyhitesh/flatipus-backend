from uuid import UUID
from fastapi import HTTPException
from typing import Optional

from app.features.task.application.ports.task_assignment_repositories import (
    ITaskAssignmentRepository
)
from app.features.task.application.dto.task_assignment_responses import (
    TaskAssignmentResponse
)
from app.shared.utils.enums import (TaskAssignmentStatus)


class MarkAssignmentSkippedUseCase:
    def __init__(
        self,
        assignment_repo: ITaskAssignmentRepository
    ):
        self.assignment_repo = assignment_repo

    def execute(
        self,
        assignment_id: UUID,
        current_user_id: UUID    
    ) -> Optional[TaskAssignmentResponse]:
        assignment = self.assignment_repo.get_assignment_by_id(
            assignment_id=assignment_id)
        if not assignment:
            raise HTTPException(
                status_code=404, detail="Task Assignment not found")
        
        updated_assignment = self.assignment_repo.update_assignment_status(
            assignment_id=assignment_id,
            status=TaskAssignmentStatus.SKIPPED
        )

        # if task repeat is not ONCE,
        # TODO: create next assignments
        return updated_assignment
