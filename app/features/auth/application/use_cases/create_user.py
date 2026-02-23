from fastapi import HTTPException

from app.features.auth.application.dto.user_responses import (
    UserResponse
)
from app.features.auth.application.dto.user_requests import (
     CreateUser
)
from app.features.auth.application.ports.user_repository import (
    IUserRepository
)


class CreateUserUseCase:
    
    def __init__(
        self,
        user_repo: IUserRepository
    ):
        self.user_repo = user_repo
    
    def execute(
        self,
        request: CreateUser
    ) -> UserResponse:
        user = self.user_repo.create(
            request=request
        )
        if not user:
            raise HTTPException(
                status_code=400,
                detail="Failed to create user."
            )
        return user
    