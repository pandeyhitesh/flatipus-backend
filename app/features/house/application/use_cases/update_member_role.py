from fastapi import HTTPException

from app.features.house.application.ports.house_repository import (
    IHouseRepository)
from app.features.house.application.ports.house_member_repository import (
    IHouseMemberRepository)
from app.shared.utils.enums import UserRole


class UpdateMemberRoleUseCase:
    def __init__(
        self,
        house_repo: IHouseRepository,
        house_member_repo: IHouseMemberRepository,
    ):
        self.house_repo = house_repo
        self.house_member_repo = house_member_repo

    def execute(self, house_id, target_user_id, new_role, current_user_id):
        house = self.house_repo.get_active_by_id(house_id)
        if not house or not house.active:
            raise HTTPException(status_code=404, detail="House not found")

        current_member = self.house_member_repo.get_member(
            house_id=house_id,
            user_id=current_user_id
        )
        if (not current_member
                or current_member.role != UserRole.ADMIN.value):
            raise HTTPException(
                status_code=403,
                detail="Not authorized to update roles")
        if current_member.user_id == target_user_id:
            raise HTTPException(
                status_code=400,
                detail="Cannot change your own role")

        member = self.house_member_repo.get_member(
            house_id=house_id,
            user_id=target_user_id)
        if not member:
            raise HTTPException(
                status_code=404,
                detail="Member not found in the house")

        member.role = new_role
        self.house_member_repo.update_member_role(
            house_id=house.id,
            user_id=target_user_id,
            new_role=new_role
        )

        return {"message": "Member role updated successfully"}
