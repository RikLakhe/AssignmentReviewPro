from typing import List

from models.user import User
from models.user_dto import UserDTO
from database import get_db

class UserService:
    def __init__(self):
        pass

    def get_users(self) -> List[UserDTO]:
        db = get_db()
        users = db.query(User).all()
        return [UserDTO(**user.__dict__) for user in users]  # Convert to DTOs

    # Add other user service methods (create, update, delete)
