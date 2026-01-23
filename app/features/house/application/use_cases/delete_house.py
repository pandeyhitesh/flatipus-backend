from fastapi import HTTPException

from app.features.house.application.ports.house_repository import (
    IHouseRepository)
from app.features.house.application.ports.house_member_repository import (
    IHouseMemberRepository)


class DeleteHouseUseCase:
    def __init__(
        self,
        house_repo: IHouseRepository,
        member_repo: IHouseMemberRepository,
    ):
        self.house_repo = house_repo
        self.member_repo = member_repo

    def execute(
        self,
        house_id, current_user_id
    ):
        house = self.house_repo.get_active_by_id(house_id=house_id)
        if not house:
            raise HTTPException(status_code=404, detail="House not found")
        is_member = self.member_repo.is_member(
            house_id=house.id, user_id=current_user_id)
        if not is_member:
            raise HTTPException(
                status_code=403, detail="Not authorized for the action")

        self.member_repo.delete_all_members(house_id=house.id)
        self.house_repo.deactivate(house_id=house.id)

        return {"message": "House deleted successfully"}
