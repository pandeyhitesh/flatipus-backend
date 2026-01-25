from fastapi import HTTPException
from uuid import UUID

from app.features.space.application.ports.space_repository import (
    ISpaceRepository
)
from app.features.space.application.dto.space_requests import (
    AddChoreRequest
)



class AddChoreToSpaceUseCase:
    def __init__(self, space_repo: ISpaceRepository):
        self.space_repo = space_repo

    def execute(self, space_id: UUID, chore_request: AddChoreRequest):
        space = self.space_repo.get_space_by_id(space_id=space_id)
        if not space:
            raise HTTPException(status_code=404, detail="Space not found")
        return self.space_repo.add_chore_to_space(
            space_id=space_id,
            chore_request=chore_request
        )