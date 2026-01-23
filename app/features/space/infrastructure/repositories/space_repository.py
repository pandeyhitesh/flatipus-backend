from sqlalchemy.orm import Session
import json
import uuid

from app.features.space.application.ports.space_repository import (
    ISpaceRepository)
from app.models import Space as SpaceModel
from app.features.space.infrastructure.mappers.space_mapper import (
    SpaceMapper)


class SpaceRepositoryImpl(ISpaceRepository):
    def __init__(self, db: Session):
        self.db = db

    # Create a new space
    def create_space(self, space_request):
        space_model = SpaceMapper.to_model(space_request)
        self.db.add(space_model)
        self.db.commit()
        self.db.refresh(space_model)
        return space_model

    # Get space by ID
    def get_space_by_id(self, space_id):
        model = self.db.query(SpaceModel).filter(
                    SpaceModel.id == space_id
                ).first()
        return SpaceMapper.to_entity(model)

    # delete space by ID
    def delete_space(self, space_id):
        space = (
            self.db.query(SpaceModel)
            .filter(
                SpaceModel.id == space_id
            ).first()
        )
        if space:
            self.db.delete(space)
            self.db.commit()
        return space

    # get all spaces in a house
    def get_all_spaces_in_house(self, house_id):
        models = self.db.query(SpaceModel).filter(
                    SpaceModel.house_id == house_id
                ).all()
        return models