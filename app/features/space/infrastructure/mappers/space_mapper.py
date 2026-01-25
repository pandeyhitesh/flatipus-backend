import json
from uuid import UUID
import uuid

from app.features.space.domain.entities.space import Space
from app.features.space.domain.entities.chores import Chores
from app.features.space.application.dto.space_requests import (
    CreateSpaceRequest
)
from app.models import Space as SpaceModel


class SpaceMapper:

    @staticmethod
    def to_entity(space_model: SpaceModel) -> Space | None:
        if space_model is None:
            return None
        print(f'@@@ space model: {space_model}')
        
        # --- extract strongly typed Chores from JSON string ---
        space_id: UUID = space_model.id
        house_id: UUID = space_model.house_id
        name: str = space_model.name


        chore_list = []

        raw_chores: str | None = space_model.chores
        if raw_chores:
            chores_dict = json.loads(raw_chores)
            

            for c in chores_dict:
                
                chore_list.append(Chores(
                    id=UUID(c['id']),
                    space_id=space_id,
                    title=c['title'],
                    items=c.get('items', []),
                ))

        return Space(
            id=space_id,
            house_id=house_id,
            name=name,
            chores=chore_list,
        )


    @staticmethod
    def to_json(space_entity: Space) -> dict:
        chores_json = None

        if space_entity.chores:
            
            chores_json = json.dumps([{
                "id": str(c.id),
                "space_id": str(c.space_id),
                "title": c.title,
                "items": c.items,
            } for c in space_entity.chores
            ])
        

        return {
            "house_id": str(space_entity.house_id),
            "name": space_entity.name,
            "chores": chores_json,
        }
    
    @staticmethod
    def to_model(space_request: CreateSpaceRequest) -> SpaceModel:
        chores_json = None
        space_id = str(uuid.uuid4())

        if space_request.chores:
            chores_json = json.dumps([{
                "id": str(uuid.uuid4()),
                "space_id": space_id,
                "title": c.title,
                "items": c.items,
            } for c in space_request.chores
            ])
        
        return SpaceModel(
            id=space_id,
            house_id=space_request.house_id,
            name=space_request.space_name,
            chores=chores_json,
        )