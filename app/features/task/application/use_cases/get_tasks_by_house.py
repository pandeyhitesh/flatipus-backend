from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID


from app.features.task.application.ports.task_repositories import ITaskRepository
from app.features.task.application.dto.task_responses import TaskResponse
from app.api.dependencies import get_db, get_current_user
from app.features.task.infrastructure.repositories.task_repo import TaskRepositoryImpl


class GetTasksByHouseUseCase:
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository

    async def execute(self, house_id: UUID) -> List[TaskResponse]:
        tasks = self.task_repository.list_tasks_by_house(house_id)
        return tasks
