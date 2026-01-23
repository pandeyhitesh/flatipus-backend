from app.features.space.application.ports.space_repository import (
    ISpaceRepository
)


class DeleteSpaceUseCase:
    def __init__(
        self,
        space_repo: ISpaceRepository
    ):
        self.space_repo = space_repo
    
    def execute(self, space_id):
        return self.space_repo.delete_space(space_id=space_id)