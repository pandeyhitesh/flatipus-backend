from uuid import UUID
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from app.features.house.domain.entities.house import House


class IHouseRepository(ABC):
    @abstractmethod
    def create(self, house: House) -> House:
        pass

    @abstractmethod
    def get_active_by_id(self, house_id: UUID) -> Optional[House]:
        pass

    @abstractmethod
    def get_active_by_house_key(self, house_key: str) -> Optional[House]:
        pass

    @abstractmethod
    def update(
        self, house_id: UUID,
        house_name: str | None,
        address: str | None
    ) -> House:
        pass

    @abstractmethod
    def deactivate(self, house_id: UUID) -> None:
        pass

    @abstractmethod
    def get_associated_houses_of_user(
        self, user_id: UUID, limit: int, offset: int
    ) -> List[Tuple[House, str, int, str]]:
        """
        Returns: (House, joined_at, member_count, role)
        """
        pass
