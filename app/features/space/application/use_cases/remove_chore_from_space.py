from fastapi import HTTPException

from app.features.space.application.ports.space_repository import (
    ISpaceRepository       
)

class RemoveChoreFromSpaceUseCase:
    def __init__(self, space_repo: ISpaceRepository):
        self.space_repo = space_repo

    def execute(self, space_id, chore_id):
        space = self.space_repo.get_space_by_id(space_id=space_id)
        if not space:
            raise HTTPException(status_code=404, detail="Space not found")
        return self.space_repo.remove_chore_from_space(
            space_id=space_id,
            chore_id=chore_id
        )