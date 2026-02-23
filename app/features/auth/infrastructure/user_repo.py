from uuid import UUID
from sqlalchemy.orm import Session

from app.features.auth.application.ports.user_repository import (
    IUserRepository
)
from app.models import User as UserModel

class UserRepositoryImpl(IUserRepository):

    def __init__(
            self,
            db: Session    
        ):
            self.db = db

    def get_by_id(self, user_id):
        return self.db.query(UserModel).filter(
                    UserModel.id == user_id
                ).first()
    
    
    def get_by_google_id(self, google_id):
        return self.db.query(UserModel).filter(
                    UserModel.google_id == google_id
                ).first()
    
    
    def get_by_email_id(self, email_id):
        return self.db.query(UserModel).filter(
                    UserModel.email == email_id
                ).first()
    
    
    
    def create(self, request):
        user = UserModel(
            email=request.email,
            name=request.name,
            google_id=request.google_id,
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
