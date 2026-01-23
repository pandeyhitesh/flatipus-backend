from app.features.space.application.ports.space_repository import (
    ISpaceRepository)
from app.features.house.application.ports.house_repository import (
    IHouseRepository)
from app.features.house.application.ports.house_member_repository import (
    IHouseMemberRepository)
from app.features.space.application.dto.space_responses import (
    GetSpaceResponse)


class CreateSpaceUseCase:
    def __init__(
        self,
        space_repo: ISpaceRepository,
        house_repo: IHouseRepository,
        member_repo: IHouseMemberRepository
    ):
        self.space_repo = space_repo
        self.house_repo = house_repo
        self.member_repo = member_repo

    def execute(self, space_request, current_user) -> GetSpaceResponse:
        # If house_id is not provided, use the user's first house
        house_id = space_request.house_id
        if not house_id:
            # Get the first house the user is a member of
            user_houses = self.member_repo.get_user_houses(current_user.id)
            if not user_houses:
                raise ValueError("User is not a member of any house")
            house_id = user_houses[0].house_id
            space_request.house_id = house_id
        
        space = self.space_repo.create_space(space_request)
        return space
