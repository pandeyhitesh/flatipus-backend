from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.shared.auth import oauth
from app.models import User
from app.shared.utils.jwt_utils import create_access_token
from app.api.dependencies import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/login")
async def login(request: Request):
    redirect_uri = "http://localhost:8000/auth/callback"
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/callback")
async def auth_callback(request: Request, db: Session = Depends(get_db)):
    token = await oauth.google.authorize_access_token(request)
    user_info = token.get("userinfo")

    email = user_info["email"]
    name = user_info["name"]
    google_id = user_info["sub"]

    # Check if user exists
    user = db.query(User).filter(User.email == email).first()

    if not user:
        # Create new user
        user = User(email=email, name=name, google_id=google_id)
        db.add(user)
        db.commit()
        db.refresh(user)

    # Generate JWT token
    access_token = create_access_token(data={"sub": user.email})

    return {
        "message": "User authenticated successfully",
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "email": user_info["email"],
            "name": user_info["name"],
            "google_id": user_info["sub"]
        }
    }
