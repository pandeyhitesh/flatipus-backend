from app.features.house.domain.entities.house import House
from app.features.house.domain.entities.house_member import HouseMember
from app.features.house.application.ports.house_repository import (
    IHouseRepository)
from app.features.house.application.ports.house_member_repository import (
    IHouseMemberRepository)
from app.shared.utils.enums import UserRole
from app.features.house.domain.value_objects.house_key import HouseKey


def generate_house_key():
    return HouseKey()


class CreateHouseUseCase:
    def __init__(
        self,
        house_repo: IHouseRepository,
        house_member_repo: IHouseMemberRepository,
    ):
        self.house_repo = house_repo
        self.house_member_repo = house_member_repo

    def execute(
        self,
        house_name, address, current_user_id
    ):
        house = House(
            id=None,
            name=house_name,
            key=generate_house_key(),
            address=address,
            created_by=current_user_id,
            created_at=None,
            active=True,
        )

        created_house = self.house_repo.create(house)

        # add the creator as admin member
        self.house_member_repo.add_member(
            HouseMember(
                id=None,
                house_id=created_house.id,
                user_id=current_user_id,
                role=UserRole.ADMIN.value,
                joined_at=None,
            )
        )

        return created_house
