from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from app.features.task.domain.entities.task import Task
from app.features.task.domain.entities.task_assignments import TaskAssignments
from app.features.task.application.dto.task_requests import (
    CreateTaskRequest, UpdateTaskRequest, UpdateTaskStatusRequest)
from app.features.task.application.dto.task_responses import (
    TaskResponse, TaskDetailResponse, UserTaskResponse)


class ITaskRepository(ABC):
    @abstractmethod
    async def create_task(self, request: CreateTaskRequest, created_by: UUID) -> Optional[TaskResponse]:
        pass

    @abstractmethod
    async def get_task_by_id(self, task_id: UUID) -> Optional[TaskResponse]:
        pass

    @abstractmethod
    async def update_task(self, request: UpdateTaskRequest, task_id: UUID) -> Optional[TaskResponse]:
        pass

    @abstractmethod
    async def delete_task(self, task_id: UUID) -> None:
        pass

    @abstractmethod
    async def list_tasks_by_house(self, house_id: UUID) -> List[TaskResponse]:
        pass

    @abstractmethod
    async def list_tasks_by_space(self, space_id: UUID) -> List[TaskResponse]:
        pass

    @abstractmethod
    async def update_status(self, request: UpdateTaskStatusRequest) -> Optional[TaskResponse]:
        pass

    @abstractmethod
    async def get_tasks_by_user(self, user_id: UUID) -> List[UserTaskResponse]:
        pass