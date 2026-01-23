import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from app.shared.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    google_id = Column(String, unique=True, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    houses = relationship("HouseMember", back_populates="user")


class House(Base):
    __tablename__ = 'houses'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    house_name = Column(String, nullable=False)
    house_key = Column(String(6), unique=True, nullable=False)
    address = Column(String, nullable=True)
    created_by = Column(
        UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean, default=True)

    members = relationship("HouseMember", back_populates="house")
    spaces = relationship("Space", back_populates="house")


class HouseMember(Base):
    __tablename__ = 'house_members'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    house_id = Column(
        UUID(as_uuid=True), ForeignKey('houses.id'), nullable=False)
    joined_at = Column(DateTime, default=datetime.utcnow)
    role = Column(String, default="MEMBER")  # Possible roles: MEMBER, ADMIN

    user = relationship("User", back_populates="houses")
    house = relationship("House", back_populates="members")


class Space(Base):
    __tablename__ = 'spaces'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    house_id = Column(
        UUID(as_uuid=True), ForeignKey('houses.id'), nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    chores = Column(Text, nullable=True)  # JSON string of chores

    house = relationship("House", back_populates="spaces")


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    house_id = Column(UUID(as_uuid=True), ForeignKey('houses.id'), nullable=False)
    space_id = Column(UUID(as_uuid=True), ForeignKey('spaces.id'), nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    repeat = Column(String, nullable=False)  # Values from TaskRepeat enum
    is_completed = Column(Boolean, default=False)
    updated_on = Column(DateTime, nullable=True)
    updated_by = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=True)
    

class TaskAssignment(Base):
    __tablename__ = 'task_assignments'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_id = Column(UUID(as_uuid=True), ForeignKey('tasks.id'), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    scheduled_on = Column(DateTime, nullable=False)
    completed_on = Column(DateTime, nullable=True)
    status = Column(String, nullable=False)  # Values from TaskAssignmentStatus enum
    is_completed = Column(Boolean, default=False)