from fastapi import HTTPException
from app.features.house.application.ports.house_repository import (
    IHouseRepository)
from app.features.house.application.ports.house_member_repository import (
    IHouseMemberRepository)
from app.features.house.domain.entities.house_member import HouseMember
from app.shared.utils.enums import UserRole


class JoinHouseUserCase:
    def __init__(
        self,
        house_repo: IHouseRepository,
        house_member_repo: IHouseMemberRepository,
    ):
        self.house_repo = house_repo
        self.house_member_repo = house_member_repo

    def execute(self, house_key, current_user_id):
        house = self.house_repo.get_active_by_house_key(house_key)
        if not house or not house.active:
            raise HTTPException(status_code=404, detail="House not found")

        existing = self.house_member_repo.is_member(
            house_id=house.id,
            user_id=current_user_id)
        if existing:
            return {"message": "Already a member"}

        self.house_member_repo.add_member(
            HouseMember(
                house_id=house.id,
                user_id=current_user_id,
                role=UserRole.MEMBER.value,
                joined_at=None,
            )
        )

        return {"message": "Successfully Joined"}
