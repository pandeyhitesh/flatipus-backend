from fastapi import HTTPException

from app.features.space.application.ports.space_repository import (
    ISpaceRepository
)
from app.features.house.application.ports.house_repository import (
    IHouseRepository
)
from app.features.house.application.ports.house_member_repository import (
    IHouseMemberRepository
)



class GetSpaceUseCase:
    def __init__(
            self,
            space_repo: ISpaceRepository,
            house_repo: IHouseRepository,
            house_member_repo: IHouseMemberRepository,
            ):
        self.space_repo = space_repo
        self.house_repo = house_repo
        self.house_member_repo = house_member_repo

    def execute(
        self,
        space_id,
        current_user_id
    ):
        space = self.space_repo.get_space_by_id(space_id=space_id)
        if not space:
            raise HTTPException(status_code=404, detail="Space not found")
        house = self.house_repo.get_active_by_id(space.house_id)
        if not house:
            raise HTTPException(status_code=404, detail="House not found")
        is_member = self.house_member_repo.is_member(
            house_id=house.id,
            user_id=current_user_id
        )
        if not is_member:
            raise HTTPException(status_code=403, detail="You are not a member of the house")
        return space
        