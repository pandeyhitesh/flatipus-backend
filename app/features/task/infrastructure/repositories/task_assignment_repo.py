from sqlalchemy.orm import Session
from uuid import UUID, uuid4
from datetime import datetime

from app.features.task.application.dto.task_assignment_requests import (
    UpdateTaskAssignmentStatusRequest)
from app.features.task.application.dto.task_assignment_responses import TaskAssignmentResponse
from app.features.task.application.ports.task_assignment_repositories import (
    ITaskAssignmentRepository)
from app.models import TaskAssignment

class TaskAssignmentRepositoryImpl(ITaskAssignmentRepository):
    def __init__(
        self,
        db: Session
    ):
        self.db = db

    # request -> request: TaskAssignmentRequest
    # response -> -> Optional[TaskAssignmentResponse]
    def create_assignment(
        self, request
    ):
        assignment_model = TaskAssignment(
            task_id=request.task_id,
            user_id=request.user_id,
            scheduled_on=request.scheduled_on,
            status=request.status,
        )

        self.db.add(assignment_model)
        self.db.commit()
        self.db.refresh(assignment_model)
        return assignment_model

    # request-> assignment_id: UUID, request: UpdateTaskAssignmentStatusRequest
    # response -> Optional[TaskAssignmentResponse]
    def update_assignment_status(
        self, 
        assignment_id: UUID, 
        request: UpdateTaskAssignmentStatusRequest
    ):
        assignment = self.db.query(TaskAssignment).filter(TaskAssignment.id == assignment_id).first()
        if not assignment:
            return None

        if request.status is not None:
            assignment.status = request.status
            assignment.updated_on = datetime.utcnow()

        self.db.commit()
        self.db.refresh(assignment)
        return assignment
    

    # request -> assignment_id: UUID
    # reaponse -> Optional[TaskAssignmentResponse]
    def get_assignment_by_id(self, assignment_id):
        return self.db.query(TaskAssignment).filter(
            TaskAssignment.id == assignment_id
        ).first()


    # request-> task_id: UUID
    # response -> List[TaskAssignmentResponse]
    def get_assignments_by_task_id(
        self, task_id
    ):
        assignments = self.db.query(TaskAssignment).filter(
            TaskAssignment.task_id == task_id).all()
        return assignments
    

    # request -> assignment_id: UUID, status: TaskAssignmentStatus
    # response -> TaskAssignmentResponse
    def update_assignment_status(
        self, assignment_id, status
    ):
        assignment = self.db.query(TaskAssignment).filter(
            TaskAssignment.id == assignment_id 
        ).first()
        if not assignment:
            return None
        
        assignment.status = status.value()
        self.db.commit()
        self.db.refresh(assignment)
        return assignment


    # request -> assignment_id: UUID, request: TaskAssignmentUpdateRequest
    # response -> TaskAssignmentResponse
    def update_assignment(self, assignment_id, request):
        assignment = self.db.query(TaskAssignment).filter(
            TaskAssignment.id == assignment_id
        ).first()

        if not assignment:
            return None
        
        if request.user_id is not None:
            assignment.user_id = request.user_id
        if request.scheduled_on is not None:
            assignment.scheduled_on = request.scheduled_on

        self.db.commit()
        self.db.refresh(assignment)
        return assignment