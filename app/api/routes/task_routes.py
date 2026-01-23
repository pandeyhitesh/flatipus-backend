from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.api.dependencies import get_current_user, get_db
from app.features.task.application.dto.task_requests import (
    CreateTaskRequest,
    UpdateTaskRequest, UpdateTaskStatusRequest
)
from app.features.task.application.use_cases.create_task import CreateTaskUseCase
from app.features.task.application.use_cases.get_task_by_id import GetTaskByIdUseCase
from app.features.task.application.use_cases.get_tasks_by_house import GetTasksByHouseUseCase
from app.features.task.application.use_cases.get_tasks_by_house import GetTasksByHouseUseCase
from app.features.task.application.use_cases.get_tasks_by_space import GetTasksBySpaceUseCase
from app.features.task.application.use_cases.update_task import UpdateTaskUseCase
from app.features.task.application.use_cases.delete_task import DeleteTaskUseCase
from app.features.task.application.use_cases.update_task_status import UpdateTaskStatusUseCase
from app.features.task.infrastructure.repositories.task_repo import (
    TaskRepositoryImpl
)
from app.features.task.infrastructure.repositories.task_assignment_repo import (
    TaskAssignmentRepositoryImpl
)


router = APIRouter(prefix='/task', tags=['task'])


@router.post('/create')
async def create_task(
    request: CreateTaskRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task_repo = TaskRepositoryImpl(db)
    task_assignment_repo = TaskAssignmentRepositoryImpl(db)
    use_case = CreateTaskUseCase(task_repo, task_assignment_repo)
    return await use_case.execute(request, current_user.id)


@router.get('/{task_id:uuid}')
async def get_task_by_id(
    task_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task_repo = TaskRepositoryImpl(db)
    task_assignment_repo = TaskAssignmentRepositoryImpl(db)
    use_case = GetTaskByIdUseCase(task_repo, task_assignment_repo)
    return await use_case.execute(task_id)


@router.get('/house/{house_id}')
async def get_tasks_by_house(
    house_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task_repo = TaskRepositoryImpl(db)
    use_case = GetTasksByHouseUseCase(task_repo)
    return await use_case.execute(house_id)


@router.get('/space/{space_id}')
async def get_tasks_by_space(
    space_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task_repo = TaskRepositoryImpl(db)
    use_case = GetTasksBySpaceUseCase(task_repo)
    return await use_case.execute(space_id)


@router.put('/update/{task_id:uuid}')
async def update_task(
    task_id: UUID,
    request: UpdateTaskRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task_repo = TaskRepositoryImpl(db)
    use_case = UpdateTaskUseCase(task_repo)
    return await use_case.execute(request, task_id)


@router.delete('/delete/{task_id:uuid}')
async def delete_task(
    task_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task_repo = TaskRepositoryImpl(db)
    use_case = DeleteTaskUseCase(task_repo)
    result = await use_case.execute(task_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return result
    

@router.put('/update-status')
async def update_status(
    request: UpdateTaskStatusRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task_repo = TaskRepositoryImpl(db)
    use_case = UpdateTaskStatusUseCase(task_repo)
    return await use_case.execute(request)