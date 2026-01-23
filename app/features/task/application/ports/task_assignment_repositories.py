from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from app.features.task.application.dto.task_assignment_requests import (
    TaskAssignmentRequest, UpdateTaskAssignmentStatusRequest)
from app.features.task.application.dto.task_assignment_responses import (
    TaskAssignmentResponse)

class ITaskAssignmentRepository(ABC):
    @abstractmethod
    async def create_assignment(
        self, request: TaskAssignmentRequest
    ) -> Optional[TaskAssignmentResponse]:
        pass

    @abstractmethod
    async def update_assignment_status(
        self, 
        assignment_id: UUID, 
        request: UpdateTaskAssignmentStatusRequest
    ) -> Optional[TaskAssignmentResponse]:
        pass

    @abstractmethod
    def get_assignments_by_task_id(
        self, task_id: UUID
    ) -> List[TaskAssignmentResponse]:
        pass
