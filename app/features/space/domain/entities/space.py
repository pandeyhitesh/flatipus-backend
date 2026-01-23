from uuid import UUID
from app.features.space.domain.entities.chores import Chores


class Space:
    def __init__(
        self,
        id: UUID,
        house_id: UUID,
        name: str,
        chores: list[Chores] | None,
    ):
        self.id = id
        self.house_id = house_id
        self.name = name
        self.chores = chores or []
