from fastapi import HTTPException

from app.features.house.application.ports.house_repository import IHouseRepository


class GetHouseByKeyUseCase:
    def __init__(self, house_repository: IHouseRepository):
        self.house_repository = house_repository

    def execute(self, house_key):
        house = self.house_repository.get_active_by_house_key(house_key)
        if not house:
            raise HTTPException(status_code=404, detail="House not found")
        return house