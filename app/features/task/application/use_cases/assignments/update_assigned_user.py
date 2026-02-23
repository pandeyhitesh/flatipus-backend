from uuid import UUID
from fastapi import HTTPException
from typing import Optional

from app.features.task.application.ports.task_assignment_repositories import (
    ITaskAssignmentRepository
)
from app.features.task.application.dto.task_assignment_responses import (
    TaskAssignmentResponse
)
from app.features.task.application.dto.task_assignment_requests import (
    TaskAssignmentUpdateRequest
)


class UpdateAssignedUserUseCase:
    def __init__(
        self,
        assignment_repo: ITaskAssignmentRepository
    ):
        self.assignment_repo = assignment_repo

    def execute(
        self,
        assignment_id: UUID,
        request: TaskAssignmentUpdateRequest,
        current_user_id: UUID
    ) -> Optional[TaskAssignmentResponse]:
        assignment = self.assignment_repo.get_assignment_by_id(
            assignment_id=assignment_id
        )
        if not assignment:
            raise HTTPException(
                status_code=404, detail="Task Assignment not found."
            )
        
        updated_assignment = self.assignment_repo.update_assignment(
            assignment_id=assignment_id,
            request=request,
        )

        return updated_assignment