from sqlalchemy.orm import Session
from uuid import UUID

from app.features.task.application.dto.task_requests import UpdateTaskRequest
from app.features.task.application.ports.task_repositories import ITaskRepository


class UpdateTaskUseCase:
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository

    async def execute(self, request: UpdateTaskRequest, task_id: UUID) -> UUID:
        task = self.task_repository.update_task(request=request, task_id=task_id)
        return task