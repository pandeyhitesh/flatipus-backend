from sqlalchemy.orm import Session

from app.features.task.application.ports.task_repositories import (
    ITaskRepository
)
from app.features.task.application.dto.task_requests import (
    UpdateTaskStatusRequest
)


class UpdateTaskStatusUseCase:
    def __init__(
        self,
        task_repository: ITaskRepository
    ):
        self.task_repository = task_repository

    async def execute(self, request: UpdateTaskStatusRequest):
        return self.task_repository.update_status(request)