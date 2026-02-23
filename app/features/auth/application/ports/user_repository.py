from abc import ABC, abstractmethod
from uuid import UUID

from app.features.auth.application.dto.user_requests import (
    CreateUser
)

class IUserRepository(ABC):
    @abstractmethod
    def get_by_id(
        self,
        user_id: UUID
    ):  
        pass

    @abstractmethod
    def get_by_google_id(
        self,
        google_id: UUID
    ):
        pass

    @abstractmethod
    def get_by_email_id(
        self,
        email_id: str
    ):
        pass

    @abstractmethod
    def create(
        self,
        request: CreateUser
    ): 
        pass