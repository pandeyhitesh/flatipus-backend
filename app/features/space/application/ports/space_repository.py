from uuid import UUID
from abc import ABC, abstractmethod
from typing import List

from app.features.space.application.dto.space_requests import (
    CreateSpaceRequest)
from app.features.space.application.dto.space_responses import (
    GetSpaceResponse)


class ISpaceRepository(ABC):
    @abstractmethod
    def create_space(
        self,
        space: CreateSpaceRequest,
        owner_id: UUID
    ) -> GetSpaceResponse:
        pass

    @abstractmethod
    def get_space_by_id(self, space_id: UUID) -> GetSpaceResponse | None:
        pass

    @abstractmethod
    def delete_space(self, space_id: UUID):
        pass

    @abstractmethod
    def get_all_spaces_in_house(self, house_id: UUID) -> List[GetSpaceResponse] | None:
        pass