from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Query
from uuid import UUID

from app.features.house.application.dto.house_requests import (
    CreateHouseRequest,
    JoinHouseRequest,
    UpdateMemberRoleRequest)
from app.features.house.application.dto.house_responses import (
    HouseResponse,
    GetHouseResponse,
    MyHousesResponse)
from app.features.house.application.use_cases.create_house import (
    CreateHouseUseCase
)
from app.features.house.application.use_cases.get_house_by_key import GetHouseByKeyUseCase
from app.features.house.application.use_cases.join_house import (
    JoinHouseUserCase
)
from app.features.house.application.use_cases.delete_house import (
    DeleteHouseUseCase
)
from app.features.house.application.use_cases.get_my_houses import (
    GetMyHousesUseCase
)
from app.features.house.application.use_cases.get_house_details import (
    GetHouseDetailsUseCase
)
from app.features.house.application.use_cases.update_member_role import (
    UpdateMemberRoleUseCase
)
from app.features.house.infrastructure.repositories.house_repo import (
    HouseRepositoryImpl
)
from app.features.house.infrastructure.repositories.house_member_repo import (
    HouseMemberRepositoryImpl
)
from app.api.dependencies import get_db, get_current_user


router = APIRouter(prefix="/house", tags=["house"])


@router.post("/create", response_model=HouseResponse)
def create_house(
    request: CreateHouseRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    house_repo = HouseRepositoryImpl(db)
    member_repo = HouseMemberRepositoryImpl(db)
    use_case = CreateHouseUseCase(house_repo, member_repo)
    return use_case.execute(
        request.house_name,
        request.address,
        current_user.id)


@router.post("/join")
def join_house(
    request: JoinHouseRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    house_repo = HouseRepositoryImpl(db)
    member_repo = HouseMemberRepositoryImpl(db)
    use_case = JoinHouseUserCase(house_repo, member_repo)
    return use_case.execute(
        house_key=request.house_key,
        current_user_id=current_user.id
    )


@router.get("/{house_id:uuid}", response_model=GetHouseResponse)
def get_house_details(
    house_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    house_repo = HouseRepositoryImpl(db)
    member_repo = HouseMemberRepositoryImpl(db)
    use_case = GetHouseDetailsUseCase(house_repo, member_repo)
    return use_case.execute(
        house_id=house_id,
        current_user_id=current_user.id
    )


@router.get("/key/{house_key}", response_model=GetHouseResponse)
def get_house_details_by_key(
    house_key: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    house_repo = HouseRepositoryImpl(db)
    use_case = GetHouseByKeyUseCase(house_repo)
    return use_case.execute(
        house_key=house_key
    )


@router.get("/mine", response_model=MyHousesResponse)
def get_my_houses(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    house_repo = HouseRepositoryImpl(db)
    member_repo = HouseMemberRepositoryImpl(db)
    use_case = GetMyHousesUseCase(house_repo, member_repo)
    return use_case.execute(
        current_user_id=current_user.id,
        limit=limit,
        offset=offset
    )


@router.delete("/delete/{house_id:uuid}")
def delete_house(
    house_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    house_repo = HouseRepositoryImpl(db)
    member_repo = HouseMemberRepositoryImpl(db)
    use_case = DeleteHouseUseCase(house_repo, member_repo)
    return use_case.execute(
        house_id=house_id,
        current_user_id=current_user.id
    )


@router.put(
    "/update-member-role/{house_id:uuid}/{user_id:uuid}",
    summary="Update the role of a member in a house",
    description="Update the role of a member in a house."
                "Only admins can update roles."
)
def update_member_role(
    house_id: UUID,
    user_id: UUID,
    request: UpdateMemberRoleRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    house_repo = HouseRepositoryImpl(db)
    member_repo = HouseMemberRepositoryImpl(db)
    use_case = UpdateMemberRoleUseCase(house_repo, member_repo)
    return use_case.execute(
        house_id=house_id,
        target_user_id=user_id,
        new_role=request.new_role,
        current_user_id=current_user.id
    )
