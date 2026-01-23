from uuid import UUID


class Chores:
    def __init__(
        self,
        id: UUID,
        space_id: UUID,
        title: str,
        items: list[str],
    ):
        self.id = id
        self.space_id = space_id
        self.title = title
        self.items = items
