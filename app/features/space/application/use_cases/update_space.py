from fastapi import HTTPException

from app.features.space.application.ports.space_repository import (
    ISpaceRepository
)
from app.features.space.application.dto.space_requests import (
    UpdateSpaceRequest
)


class UpdateSpaceUseCase:
    def __init__(self, space_repo: ISpaceRepository):
        self.space_repo = space_repo

    def execute(self, space_id, request: UpdateSpaceRequest):
        space = self.space_repo.get_space_by_id(space_id=space_id)
        if not space:
            raise HTTPException(status_code=404, detail="Space not found")
        updated_space = self.space_repo.update(
            space_id=space_id,
            request=request
        )
        return updated_space