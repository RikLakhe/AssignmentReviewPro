# from typing import List
#
# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
#
# from models.user_dto import UserDTO
# from services.user_service import UserService
# from database import get_db
#
# router = APIRouter()
#
#
# # Example route to retrieve users (replace with your actual logic)
# @router.get("/users", response_model=List[UserDTO])
# async def get_users(db: Session = Depends(get_db)):
#     """Retrieves a list of users from the database."""
#     user_service = UserService()
#     return user_service.get_users()


from fastapi import APIRouter

router = APIRouter()

@router.get("/users")  # <-- This should match the requested URL: GET /api/v1/users
async def get_users():
    return {"message": "Version 1 - Get Users"}
