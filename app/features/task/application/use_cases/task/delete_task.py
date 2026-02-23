from sqlalchemy.orm import Session
from uuid import UUID

from app.features.task.application.ports.task_repositories import ITaskRepository


class DeleteTaskUseCase:
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository

    async def execute(self, task_id: UUID):
        # Check if task exists first
        task = self.task_repository.get_task_by_id(task_id=task_id)
        if not task:
            return None
        
        # Delete the task only if it exists
        self.task_repository.delete_task(task_id=task_id)
        return {"detail": "Task deleted successfully"}