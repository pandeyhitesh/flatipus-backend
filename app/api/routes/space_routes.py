from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.api.dependencies import get_current_user, get_db
from app.features.space.application.dto.space_responses import (
    GetSpaceResponse
)
from app.features.space.application.dto.space_requests import (
    AddChoreRequest,
    CreateSpaceRequest,
    UpdateSpaceRequest
)
from app.features.space.application.use_cases.add_chore_to_space import AddChoreToSpaceUseCase
from app.features.space.application.use_cases.remove_chore_from_space import RemoveChoreFromSpaceUseCase
from app.features.space.infrastructure.repositories.space_repository import (
    SpaceRepositoryImpl
)
from app.features.house.infrastructure.repositories.house_member_repo import (
    HouseMemberRepositoryImpl
)
from app.features.house.infrastructure.repositories.house_repo import (
    HouseRepositoryImpl
)
from app.features.space.application.use_cases.get_space import (
    GetSpaceUseCase
)
from app.features.space.application.use_cases.create_space import (
    CreateSpaceUseCase
)
from app.features.space.application.use_cases.delete_space import (
    DeleteSpaceUseCase
)
from app.features.space.application.use_cases.get_all_spaces import (
    GetAllSpacesUseCase
)
from app.features.space.application.use_cases.update_space import (
    UpdateSpaceUseCase
)


router = APIRouter(prefix='/space', tags=['space'])

@router.get('/{space_id:uuid}')
def get_space(
    space_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    space_repo = SpaceRepositoryImpl(db)
    house_repo = HouseRepositoryImpl(db)
    member_repo = HouseMemberRepositoryImpl(db)
    use_case = GetSpaceUseCase(space_repo, house_repo, member_repo)
    return use_case.execute(space_id, current_user.id)


@router.post('/create', response_model=GetSpaceResponse)
def create_space(
    request: CreateSpaceRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    space_repo = SpaceRepositoryImpl(db)
    house_repo = HouseRepositoryImpl(db)
    member_repo = HouseMemberRepositoryImpl(db)
    use_case = CreateSpaceUseCase(space_repo, house_repo, member_repo)
    return use_case.execute(request, current_user)

@router.delete('/{space_id:uuid}/delete')
def delete_space(
    space_id: UUID,
    db: Session =Depends(get_db),
    current_user=Depends(get_current_user),
):
    space_repo= SpaceRepositoryImpl(db)
    use_case=DeleteSpaceUseCase(space_repo)
    return use_case.execute(space_id)


@router.get('/house/{house_id:uuid}/all', response_model=list[GetSpaceResponse])
def get_all_spaces_in_house(
    house_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    space_repo = SpaceRepositoryImpl(db)
    house_repo = HouseRepositoryImpl(db)
    member_repo = HouseMemberRepositoryImpl(db)
    use_case = GetAllSpacesUseCase(space_repo, house_repo, member_repo)
    return use_case.execute(house_id, current_user.id)


@router.put('/{space_id:uuid}/update', response_model=GetSpaceResponse)
def update_space(
    space_id: UUID,
    request: UpdateSpaceRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    space_repo = SpaceRepositoryImpl(db)
    house_repo = HouseRepositoryImpl(db)
    member_repo = HouseMemberRepositoryImpl(db)
    use_case = UpdateSpaceUseCase(space_repo)
    return use_case.execute(space_id, request)


@router.post('/{space_id:uuid}/add-chore', response_model=GetSpaceResponse)
def add_chore_to_space(
    space_id: UUID,
    chore_request: AddChoreRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    space_repo = SpaceRepositoryImpl(db)
    house_repo = HouseRepositoryImpl(db)
    member_repo = HouseMemberRepositoryImpl(db)
    use_case = AddChoreToSpaceUseCase(space_repo)
    return use_case.execute(space_id, chore_request)


@router.delete('/{space_id:uuid}/remove-chore/{chore_id:uuid}', response_model=GetSpaceResponse)
def remove_chore_from_space(
    space_id: UUID,
    chore_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    space_repo = SpaceRepositoryImpl(db)
    house_repo = HouseRepositoryImpl(db)
    member_repo = HouseMemberRepositoryImpl(db)
    use_case = RemoveChoreFromSpaceUseCase(space_repo)
    return use_case.execute(space_id, chore_id)