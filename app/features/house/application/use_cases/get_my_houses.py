from app.features.house.application.ports.house_repository import (
    IHouseRepository)
from app.features.house.application.ports.house_member_repository import (
    IHouseMemberRepository)


class GetMyHousesUseCase:
    def __init__(
        self,
        house_repo: IHouseRepository,
        member_repo: IHouseMemberRepository
    ):
        self.house_repo = house_repo
        self.member_repo = member_repo

    def execute(self, current_user_id, limit, offset):
        total = self.member_repo.count_members(current_user_id)
        houses = self.house_repo.get_associated_houses_of_user(
            current_user_id, limit, offset)
        return {
            "total": total,
            "limit": limit,
            "offset": offset,
            "houses": houses,
        }
