from uuid import UUID
from datetime import datetime


class User:
    def __init__(
        self,
        id: UUID,
        email: str,
        name: str,
        google_id: str,
        created_at: datetime,
    ):
        self.id = id
        self.email = email
        self.name = name
        self.google_id = google_id
        self.created_at = created_at
