from sqlalchemy.orm import Session
from uuid import UUID, uuid4
from datetime import datetime

from app.features.task.application.ports.task_repositories import ITaskRepository
from app.models import Task, TaskAssignment, TaskAssignment


class TaskRepositoryImpl(ITaskRepository):
    def __init__(self, db: Session):
        self.db = db

    # request -> request:CreateTaskRequest, created_by: UUID
    # response -> Optional[TaskResponse]
    def create_task(self, request, created_by):
        task_model = Task(
            id=uuid4(),
            title=request.title,
            description=request.description,
            house_id=request.house_id,
            space_id=request.space_id,
            created_by=created_by,
            repeat=request.repeat,
            created_at=datetime.utcnow(),
            is_completed=False
        )
        self.db.add(task_model)
        self.db.commit()
        self.db.refresh(task_model)
        return task_model

    
    # request -> task_id:UUID
    # response -> Optional[TaskDetailResponse]
    def get_task_by_id(self, task_id):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        return task

    
    # request -> request:UpdateTaskRequest, task_id:UUID
    # response -> Optional[TaskResponse]
    def update_task(self, request, task_id):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None

        if request.title is not None:
            task.title = request.title
        if request.description is not None:
            task.description = request.description
        if request.repeat is not None:
            task.repeat = request.repeat

        self.db.commit()
        self.db.refresh(task)
        return task

    
    # request -> task_id:UUID
    # response -> None
    def delete_task(self, task_id):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            self.db.delete(task)
            self.db.commit()

    
    # request -> house_id:UUID
    # response -> List[TaskResponse]
    def list_tasks_by_house(self, house_id):
        tasks = self.db.query(Task).filter(Task.house_id == house_id).all()
        return tasks

    
    # request -> space_id:UUID
    # response -> List[TaskResponse]
    def list_tasks_by_space(self, space_id):
        tasks = self.db.query(Task).filter(Task.space_id == space_id).all()
        return tasks

    
    # request -> request:UpdateTaskStatusRequest
    # response -> Optional[TaskResponse]
    def update_status(self, request):
        task = self.db.query(Task).filter(Task.id == request.task_id).first()
        if not task:
            return None

        task.is_completed = request.is_completed
        task.updated_by = request.updated_by
        task.updated_on = datetime.utcnow()

        self.db.commit()
        self.db.refresh(task)
        return task

    
    # request -> request:TaskByUserRequest
    # response -> List[UserTaskResponse]
    def get_tasks_by_user(self, request):
        tasks = self.db.query(Task).join(
            TaskAssignment,
            Task.id == TaskAssignment.task_id
        ).filter(
            TaskAssignment.user_id == request.user_id,
            Task.house_id == request.house_id
        ).all()
        return tasks