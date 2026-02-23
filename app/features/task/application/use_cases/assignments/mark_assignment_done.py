from uuid import UUID
from typing import Optional
from fastapi import HTTPException

from app.features.task.application.ports.task_assignment_repositories import (
    ITaskAssignmentRepository
)
from app.features.task.application.dto.task_assignment_responses import (
    TaskAssignmentResponse
)
from app.shared.utils.enums import (TaskAssignmentStatus)


class MaskAssignmentDoneUseCase:
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
            assignment_id=assignment_id
        )
        if not assignment:
            HTTPException(status_code=404, detail="Assignment not found")

        # Update assignment Status
        updated_assignment = self.assignment_repo.update_assignment_status(
            assignment_id=assignment_id,
            status=TaskAssignmentStatus.COMPLETED,
        )

        # if repeat is not ONCE,
        # TODO: create next assignment

        return updated_assignment


        
