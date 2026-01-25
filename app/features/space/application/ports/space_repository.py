from uuid import UUID
from abc import ABC, abstractmethod
from typing import List

from app.features.space.application.dto.space_requests import (
    CreateSpaceRequest, UpdateSpaceRequest)
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

    @abstractmethod
    def update(
        self,
        space_id: UUID,
        request: UpdateSpaceRequest
    ) -> GetSpaceResponse:
        pass

    @abstractmethod
    def add_chore_to_space(
        self,
        space_id: UUID,
        chore_request
    ):
        pass

    @abstractmethod
    def remove_chore_from_space(
        self,
        space_id: UUID,
        chore_id: UUID
    ):
        pass