from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from app.features.house.domain.entities.house_member import HouseMember


class IHouseMemberRepository(ABC):
    @abstractmethod
    def add_member(self, member: HouseMember) -> None:
        raise NotImplementedError

    @abstractmethod
    def is_member(
                self, house_id: UUID, user_id: UUID) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_member(
                self, house_id: UUID, user_id: UUID) -> Optional[HouseMember]:
        raise NotImplementedError

    @abstractmethod
    def get_member(
                self, house_id: UUID, user_id: UUID) -> Optional[HouseMember]:
        raise NotImplementedError

    @abstractmethod
    def delete_all_members(self, house_id: UUID) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_house_members(self, house_id: UUID) -> List[HouseMember]:
        raise NotImplementedError

    @abstractmethod
    def update_member_role(
            self,
            house_id: UUID,
            user_id: UUID,
            new_role: str) -> Optional[HouseMember]:
        raise NotImplementedError

    @abstractmethod
    def count_members(self, user_id: UUID) -> int:
        raise NotImplementedError
