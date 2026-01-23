from enum import Enum


# enum
class UserRole(str, Enum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"

class TaskRepeat(str, Enum):
    ONCE = "ONCE"
    DAILY = "DAILY"
    CUSTOM_WEEK = "CUSTOM_WEEK"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"

class TaskAssignmentStatus(str, Enum):
    ACTIVE = "ACTIVE"
    UPCOMING = "UPCOMING"
    SKIPPED = "SKIPPED"
    COMPLETED = "COMPLETED"
