from uuid import UUID
from datetime import datetime

from app.features.house.domain.value_objects.house_key import HouseKey


class House:
    def __init__(
        self,
        id: UUID,
        name: str,
        key: HouseKey,
        address: str,
        created_at: datetime,
        created_by: UUID,
        active: bool,
    ):
        self.id = id
        self.name = name
        self.key = key
        self.address = address
        self.created_at = created_at
        self.created_by = created_by
        self.active = active
