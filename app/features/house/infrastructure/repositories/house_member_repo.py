from sqlalchemy.orm import Session
from app.models import HouseMember, User
from sqlalchemy import func
from app.features.house.application.ports.house_member_repository import (
    IHouseMemberRepository)


class HouseMemberRepositoryImpl(IHouseMemberRepository):
    def __init__(self, db: Session):
        self.db = db

    # add a new member
    def add_member(self, house_member):
        # Get current max order for this house and increment
        max_order = self.db.query(func.max(HouseMember.order)).filter(
            HouseMember.house_id == house_member.house_id
        ).scalar() or 0
        member_model = HouseMember(
            house_id=house_member.house_id,
            user_id=house_member.user_id,
            role=house_member.role,
        )
        self.db.add(member_model)
        self.db.commit()
        return member_model

    # check if the user is a member of the house
    def is_member(self, house_id, user_id):
        return (
            self.db.query(HouseMember)
            .filter(
                HouseMember.house_id == house_id,
                HouseMember.user_id == user_id,
            )
            .first()
        )

    def get_member(self, house_id, user_id):
        return (
            self.db.query(HouseMember)
            .filter(
                HouseMember.house_id == house_id,
                HouseMember.user_id == user_id,
            )
            .first()
        )

    # delete all members
    def delete_all_members(self, house_id):
        self.db.query(HouseMember).filter(
            HouseMember.house_id == house_id
        ).delete(synchronize_session=False)
        self.db.commit()

    # get house members with thier roles
    def get_house_members(self, house_id):
        results = (
            self.db.query(User, HouseMember.role)
            .join(HouseMember, HouseMember.user_id == User.id)
            .filter(HouseMember.house_id == house_id)
            .all()
        )
        # Transform tuples into dictionaries that match the MemberInfo schema
        return [
            {
                "id": str(user.id),
                "name": user.name,
                "email": user.email,
                "role": role,
            }
            for user, role in results
        ]

    # update role of a member
    def update_member_role(self, house_id, user_id, new_role):
        member = (
            self.db.query(HouseMember)
            .filter(
                HouseMember.house_id == house_id,
                HouseMember.user_id == user_id,
            )
            .first()
        )
        if member:
            member.role = new_role
            self.db.commit()
        return member

    # count user is a member in how many houses
    def count_members(self, user_id):
        return (
            self.db.query(HouseMember)
            .filter(HouseMember.user_id == user_id)
            .count()
        )
