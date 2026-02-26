from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
import os

from app.features.auth.application.dto.user_responses import AuthResponse
from app.shared.auth import oauth
from app.models import User
from app.shared.utils.jwt_utils import create_access_token
from app.api.dependencies import get_db
from app.features.auth.infrastructure.user_repo import (
    UserRepositoryImpl
)
from app.features.auth.application.use_cases.google_login import (
    GoogleLoginUseCase
)
from app.features.auth.application.dto.user_requests import (
    GoogleMobileLoginRequest
)

router = APIRouter(prefix="/auth", tags=["auth"])

# -- WEB LOGIN --
@router.get("/login")
async def login(request: Request):
    # redirect_uri = "http://localhost:8000/auth/callback"
    redirect_uri = os.getenv(
        "REDIRECT_URI",
        "https://flatipus-backend-production.up.railway.app/auth/callback"
    )
    return await oauth.google.authorize_redirect(request, redirect_uri)


# -- WEB CALLBACK --
@router.get("/callback")
async def auth_callback(request: Request, db: Session = Depends(get_db)):
    token = await oauth.google.authorize_access_token(request)
    user_info = token.get("userinfo")

    repo = UserRepositoryImpl(db)
    use_case = GoogleLoginUseCase(repo)

    return use_case.execute(token["id_token"])

    # email = user_info["email"]
    # name = user_info["name"]
    # google_id = user_info["sub"]

    # # Check if user exists
    # user = db.query(User).filter(User.email == email).first()

    # if not user:
    #     # Create new user
    #     user = User(email=email, name=name, google_id=google_id)
    #     db.add(user)
    #     db.commit()
    #     db.refresh(user)

    # # Generate JWT token
    # access_token = create_access_token(data={"sub": user.email})

    # return {
    #     "message": "User authenticated successfully",
    #     "access_token": access_token,
    #     "token_type": "bearer",
    #     "user": {
    #         "email": user_info["email"],
    #         "name": user_info["name"],
    #         "google_id": user_info["sub"]
    #     }
    # }


# -- MOBILE LOGIN --
@router.post("/google-mobile", response_model=AuthResponse)
def google_mobile_login(
    request: GoogleMobileLoginRequest,
    db: Session = Depends(get_db)
):
    repo = UserRepositoryImpl(db)
    use_case = GoogleLoginUseCase(repo)
    return use_case.execute(request.id_token)