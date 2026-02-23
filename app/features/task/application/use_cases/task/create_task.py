

from app.features.task.application.dto.task_requests import CreateTaskRequest
from app.features.task.application.ports.task_repositories import (
    ITaskRepository)
from app.features.task.application.ports.task_assignment_repositories import (
    ITaskAssignmentRepository)


class CreateTaskUseCase:
    def __init__(
        self,
        task_repository: ITaskRepository,
        task_assignment_repository: ITaskAssignmentRepository
    ):
        self.task_repository = task_repository
        self.task_assignment_repository = task_assignment_repository

    async def execute(self, request: CreateTaskRequest, current_user_id):
        #TODO: Validate the house_id and space_id
        task = self.task_repository.create_task(
            request=request, created_by=current_user_id
        )
        # TODO: create task assignements
        # 1. Get the member list
        # 2. Create assignments for the members
        return task
    