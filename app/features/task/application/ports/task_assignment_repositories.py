from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from app.features.task.application.dto.task_assignment_requests import (
    TaskAssignmentRequest, UpdateTaskAssignmentStatusRequest, 
    TaskAssignmentUpdateRequest)
from app.features.task.application.dto.task_assignment_responses import (
    TaskAssignmentResponse)
from app.shared.utils.enums import TaskAssignmentStatus

class ITaskAssignmentRepository(ABC):
    @abstractmethod
    async def create_assignment(
        self, request: TaskAssignmentRequest
    ) -> Optional[TaskAssignmentResponse]:
        pass

    @abstractmethod
    async def get_assignment_by_id(
        self, assignment_id: UUID) -> Optional[TaskAssignmentResponse]:
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

    @abstractmethod
    def update_assignment_status(
        self, 
        assignment_id: UUID,
        status: TaskAssignmentStatus
    ) -> Optional[TaskAssignmentResponse]:
        pass

    @abstractmethod
    def update_assignment(
        self,
        assignment_id: UUID,
        request: TaskAssignmentUpdateRequest
    ) -> Optional[TaskAssignmentResponse]:
        pass


