from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from app.features.task.application.dto.task_responses import TaskResponse
from app.features.task.application.ports.task_repositories import ITaskRepository



class GetTasksBySpaceUseCase:
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository

    async def execute(self, space_id: UUID) -> List[TaskResponse]:
        tasks = self.task_repository.list_tasks_by_space(space_id)
        return tasks