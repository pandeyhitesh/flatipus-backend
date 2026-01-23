from uuid import UUID
from datetime import datetime
from app.shared.utils.enums import UserRole


class HouseMember:
    def __init__(
        self,
        id: UUID,
        user_id: UUID,
        house_id: UUID,
        joined_at: datetime,
        role: UserRole,
    ):
        self.id = id
        self.user_id = user_id
        self.house_id = house_id
        self.joined_at = joined_at
        self.role = role
