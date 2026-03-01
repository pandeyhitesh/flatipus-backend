from google.oauth2 import id_token
from google.auth.transport import requests
from fastapi import HTTPException
import os

from app.shared.utils.jwt_utils import create_access_token
from app.features.auth.application.ports.user_repository import (
    IUserRepository
)
from app.features.auth.application.dto.user_requests import (
    CreateUserRequest
)
from app.features.auth.application.dto.user_responses import (
    AuthResponse, AuthUserResponse
)

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_ANDROID_CLIENT_ID = os.getenv("GOOGLE_ANDROID_CLIENT_ID")

class GoogleLoginUseCase:
    def __init__(
        self,
        user_repo: IUserRepository
    ):
        self.user_repo = user_repo

    def execute(
        self,
        google_id_token: str
    ):
        try:
            # try veryfying against the web client ID first
            id_info = None
            for client_id in filter(None, [GOOGLE_CLIENT_ID, GOOGLE_ANDROID_CLIENT_ID]):
                try:
                    id_info = id_token.verify_oauth2_token(
                        google_id_token,
                        requests.Request(),
                        client_id
                    )
                    break
                except ValueError:
                    continue  # try the next client ID

            if not id_info:
                raise ValueError("Token verification failed for all client IDs")

            if id_info["iss"] not in ["accounts.google.com", "https://accounts.google.com"]:
                raise ValueError("Wrong issuer")
            
            google_id = id_info["sub"]
            email = id_info["email"]
            name = id_info.get("name")
            photoURL = id_info.get("picture")

        except ValueError as e:
            print(f"Token verification failed: {e}, client_id used: {GOOGLE_CLIENT_ID}")
            raise HTTPException(
                status_code=401,
                detail="Invalid Google token"
            )
        
        user = self.user_repo.get_by_google_id(
            google_id=google_id
        )
        if not user:
            user = self.user_repo.create(
                request=CreateUserRequest(
                    email=email, 
                    google_id=google_id, 
                    name=name,
                    photoURL=photoURL,
                )
            )
        access_token = create_access_token(data={"sub": str(user.id)})

        return AuthResponse(
            access_token=access_token,
            token_type="bearer",
            user=AuthUserResponse(
                id=str(user.id),
                name=user.name,
                email=user.email,
                photoURL=user.photoURL
            )
        )