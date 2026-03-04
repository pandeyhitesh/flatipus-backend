from fastapi import HTTPException
from app.features.auth.application.ports.user_repository import IUserRepository
from app.features.house.application.dto.house_responses import HouseDetailResponse, HouseMemberResponse
from app.features.house.application.ports.house_repository import (
    IHouseRepository)
from app.features.house.application.ports.house_member_repository import (
    IHouseMemberRepository)


class GetHouseDetailsUseCase:
    def __init__(
        self,
        house_repo: IHouseRepository,
        member_repo: IHouseMemberRepository,
        user_repo: IUserRepository
    ):
        self.house_repo = house_repo
        self.member_repo = member_repo
        self.user_repo = user_repo

    def execute(
        self,
        house_id, current_user_id
    )->HouseDetailResponse:
        house = self.house_repo.get_active_by_id(house_id)
        if not house:
            raise HTTPException(status_code=404, detail="House not found")
        is_member = self.member_repo.is_member(house_id, current_user_id)
        if not is_member:
            raise HTTPException(status_code=403, detail="Access denied")

        members = self.member_repo.get_house_members(house.id)
        user = self.user_repo.get_user_by_id(house.created_by)
        members_response = []
        for member in members:
            mbr = HouseMemberResponse(
                id=member.id,
                user_id=member.user_id,
                house_id=member.house_id,
                name=user.name,
                joined_at=member.joined_at.isoformat(),
                role=member.role,
                order=member.order,
                photo_url=user.photo_url
            )
            members_response.append(mbr)
        # return {
        #     "house": house,
        #     "members": members_response,
        # }
        return HouseDetailResponse(
            house=house, 
            members=members_response,
        )

