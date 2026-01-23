from sqlalchemy.orm import Session
from uuid import UUID

from app.features.task.application.ports.task_repositories import (
    ITaskRepository)
from app.features.task.application.ports.task_assignment_repositories import (
    ITaskAssignmentRepository
)
from app.features.task.application.dto.task_responses import TaskDetailResponse


class GetTaskByIdUseCase:
    def __init__(
        self,
        task_repository: ITaskRepository,
        task_assignment_repository: ITaskAssignmentRepository
    ):
        self.task_repository = task_repository
        self.task_assignment_repository = task_assignment_repository

    async def execute(self, task_id: UUID):
        task = self.task_repository.get_task_by_id(task_id=task_id)
        assignment_list = self.task_assignment_repository.get_assignments_by_task_id(task_id=task_id)
        if not task:
            return None
        if not assignment_list:
            assignment_list = []
        result = TaskDetailResponse(
            task=task,
            assignments=assignment_list
        )
        return result