from uuid import UUID
from fastapi import HTTPException

from app.features.auth.application.dto.user_responses import (
    UserResponse
)
from app.features.auth.application.ports.user_repository import (
    IUserRepository
)


class GetUserUseCase:
    
    def __init__(
        self,
        user_repo: IUserRepository,
    ):
        self.user_repo = user_repo

    def execute(
        self,
        user_id: UUID
    ) -> UserResponse:
        user = self.user_repo.get_by_id(
            user_id=user_id
        ) 
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found."
            )
        return user
        
    