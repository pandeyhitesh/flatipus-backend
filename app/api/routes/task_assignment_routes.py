from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

from app.api.dependencies import get_db, get_current_user
from app.features.task.application.dto.task_assignment_requests import (
    TaskAssignmentUpdateRequest
)
from app.features.task.application.use_cases.assignments.get_assignments_by_task_id import (
    GetAssignmentsByTaskIdUseCase
)
from app.features.task.application.use_cases.assignments.mark_assignment_done import (
    MaskAssignmentDoneUseCase
)
from app.features.task.application.use_cases.assignments.mark_assignment_skipped import (
    MarkAssignmentSkippedUseCase
)
from app.features.task.application.use_cases.assignments.reschedule_assignment import (
    RescheduleAssignmentUseCase
)
from app.features.task.application.use_cases.assignments.update_assigned_user import (
    UpdateAssignedUserUseCase
)
from app.features.task.infrastructure.repositories.task_assignment_repo import (
    TaskAssignmentRepositoryImpl
)
from app.features.task.application.dto.task_assignment_responses import (
    TaskAssignmentResponse
)

router = APIRouter(prefix='/task', tags=['task-assignment'])


@router.get('/{task_id:uuid}/assignments',
            response_model=List[TaskAssignmentResponse])
async def get_assignemts_by_task_id(
    task_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    assignmennt_repo = TaskAssignmentRepositoryImpl(db)
    use_case = GetAssignmentsByTaskIdUseCase(assignmennt_repo)
    return await use_case.execute(task_id=task_id, current_user_id=current_user.id)

@router.put('/assignment/{assignment_id:uuid}/mark-done',
            response_model=TaskAssignmentResponse)
async def mark_assignment_done(
    assignment_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    assignment_repo = TaskAssignmentRepositoryImpl(db)
    use_case = MaskAssignmentDoneUseCase(assignment_repo)
    return await use_case.execute(
        assignment_id=assignment_id,
        current_user_id=current_user.id
    )

@router.put('/assignment/{assignment_id:uuid}/mark-skipped',
            response_model=TaskAssignmentResponse)
async def mark_assignment_skipped(
    assignment_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    assignment_repo = TaskAssignmentRepositoryImpl(db)
    use_case = MarkAssignmentSkippedUseCase(assignment_repo)
    return await use_case.execute(
        assignment_id=assignment_id,
        current_user_id=current_user.id,
    )

@router.put('/assignment/{assignment_id:uuid}/reschedule',
            response_model=TaskAssignmentResponse)
async def reschedule_assignment(
    assignment_id: UUID,
    request: TaskAssignmentUpdateRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    assignment_repo = TaskAssignmentRepositoryImpl(db)
    use_case = RescheduleAssignmentUseCase(assignment_repo)
    return await use_case.execute(
        assignment_id=assignment_id,
        request=request,
        current_user_id=current_user.id,
    )

@router.put('/assignment/{assignment_id:uuid}/reassign',
            response_model=TaskAssignmentResponse)
async def update_assigned_user(
    assignment_id: UUID,
    request: TaskAssignmentUpdateRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    assignment_repo = TaskAssignmentRepositoryImpl(db)
    use_case = UpdateAssignedUserUseCase(assignment_repo)
    return await use_case.execute(
        assignment_id=assignment_id,
        request=request,
        current_user_id=current_user.id
    )

