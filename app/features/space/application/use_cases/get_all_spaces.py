from fastapi import HTTPException

from app.features.space.infrastructure.repositories.space_repository import (
    SpaceRepositoryImpl)
from app.features.house.infrastructure.repositories.house_member_repo import (
    HouseMemberRepositoryImpl)
from app.features.house.infrastructure.repositories.house_repo import (
    HouseRepositoryImpl)

class GetAllSpacesUseCase:
    def __init__(
        self,
        space_repo: SpaceRepositoryImpl,
        house_repo: HouseRepositoryImpl,
        member_repo: HouseMemberRepositoryImpl
    ):
        self.space_repo = space_repo
        self.house_repo = house_repo
        self.member_repo = member_repo

    def execute(self, house_id, current_user_id):
        house = self.house_repo.get_active_by_id(house_id)
        if not house:
            raise HTTPException(status_code=404, detail="House not found")
        is_member = self.member_repo.is_member(house_id, current_user_id)
        if not is_member:
            raise HTTPException(
                status_code=403,
                detail="Not authorized to access spaces in this house")
        return self.space_repo.get_all_spaces_in_house(house_id=house_id)