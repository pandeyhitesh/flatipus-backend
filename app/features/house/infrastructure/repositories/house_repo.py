from sqlalchemy.orm import Session
from app.features.house.application.ports.house_repository import (
    IHouseRepository)
from app.models import House as HouseModel
from app.models import HouseMember as HouseMemberModel
from app.features.house.domain.entities.house import House
from sqlalchemy import func


class HouseRepositoryImpl(IHouseRepository):

    def __init__(self, db: Session):
        self.db = db

    # Create a new house
    def create(self, house: House) -> House:
        house_model = HouseModel(
            house_name=house.name,
            house_key=house.key.value,
            address=house.address,
            created_by=house.created_by,
        )
        self.db.add(house_model)
        self.db.commit()
        self.db.refresh(house_model)
        return house_model

    # Get active house by ID
    def get_active_by_id(self, house_id):
        return (
            self.db.query(HouseModel)
            .filter(
                HouseModel.id == house_id,
                HouseModel.active.is_(True)
            ).first())

    # get active house by key
    def get_active_by_house_key(self, house_key):
        return (
            self.db.query(HouseModel)
            .filter(
                HouseModel.house_key == house_key,
                HouseModel.active.is_(True)
            ).first())

    # Update house
    def update(
        self,
        house_id,
        house_name=None,
        address=None
    ):
        house = (
            self.db.query(HouseModel)
            .filter(
                HouseModel.id == house_id,
                HouseModel.active.is_(True)
            ).first()
        )
        if not house:
            return None
        if house_name is not None:
            house.house_name = house_name
        if address is not None:
            house.address = address
        self.db.commit()
        self.db.refresh(house)
        return house

    # make the house inactive
    def deactivate(self, house_id):
        house = self.db.query(HouseModel).filter(
            HouseModel.id == house_id, HouseModel.active.is_(True)
        ).first()
        if house:
            house.active = False
            self.db.commit()

    # get associated houses for a user
    def get_associated_houses_of_user(self, user_id, limit, offset):
        results = (
            self.db.query(
                HouseModel,
                HouseMemberModel.joined_at,
                HouseMemberModel.role,
                func.count(HouseMemberModel.user_id).label("member_count"),
            )
            .join(HouseMemberModel, HouseMemberModel.house_id == HouseModel.id)
            .filter(
                HouseMemberModel.user_id == user_id,
                HouseModel.active.is_(True))
            .group_by(
                HouseModel.id,
                HouseMemberModel.joined_at,
                HouseMemberModel.role)
            .limit(limit)
            .offset(offset)
            .all()
        )

        # Transform tuples into dictionaries that match the schema
        return [
            {
                "id": house.id,
                "house_name": house.house_name,
                "house_key": house.house_key,
                "address": house.address,
                "joined_at": joined_at,
                "member_count": member_count,
                "role": role,
            }
            for house, joined_at, role, member_count in results
        ]
