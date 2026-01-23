from enum import Enum


# enum
class UserRole(str, Enum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"
