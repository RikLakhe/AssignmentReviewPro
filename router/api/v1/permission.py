# from fastapi import APIRouter
#
# from models.message_dto import MessageDTO
#
# router = APIRouter()
#
#
# @router.get("/permission", response_model=MessageDTO)
# async def root():
#     """Returns a simple message."""
#     return MessageDTO(message="Hello, world! permission v2")
from fastapi import APIRouter

router = APIRouter()

@router.get("/permissions")
async def get_permissions():
    return {"message": "Version 1 - Get Permissions"}
